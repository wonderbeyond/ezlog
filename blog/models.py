# coding=utf-8
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils.html import strip_tags
from django.utils.encoding import force_unicode

import os, re, time, cgi
from pyquery import PyQuery as pq
from filebrowser.base import FileObject
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from taggit.managers import TaggableManager

from blog.fields import *

class BaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = 'blog'


class CategoryManager(models.Manager):
    pass

class Category(BaseModel):
    name = models.CharField(max_length=100, default=u'未分类', unique=True,
                            verbose_name=u'名称')
    desc = models.CharField(max_length=200, null=True, blank=True,
                            verbose_name=u'描述')
    objects = CategoryManager()

    class Meta(BaseModel.Meta):
        verbose_name = "分类"
        verbose_name_plural = "分类"

    @models.permalink
    def get_absolute_url(self):
        return ('blog.query', [], dict(cate=self.id))


    def __unicode__(self):
        return self.name

class EntryManager(models.Manager):
    '''return accessible objects for specified user'''
    def accessibles(self, user):
        #FIXME: 不再区分是否superuser
        if user.is_superuser:
            entries = Entry.objects.all()
        else:
            entries = Entry.objects.filter(public=True)
        return entries

class Entry(BaseModel):
    title = models.CharField(max_length=200, unique=True,
                             verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容')
    author = models.ForeignKey(User, verbose_name=u'作者', editable=False)
    category = models.ForeignKey(Category, verbose_name=u'分类')
    tags = TaggableManager(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    public = models.BooleanField(default=True, verbose_name=u'是否公开')
    views = models.PositiveIntegerField(verbose_name=u'浏览次数', default=0, editable=False)

    objects = EntryManager()

    class Meta(BaseModel.Meta):
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ['-created']

    @models.permalink
    def get_absolute_url(self):
        return ('blog.get', [str(self.id)], {})

    def __unicode__(self):
        return self.title

    def char_count(self):
        return len(strip_tags(self.html_content))

    def tags_cs(self):
        '''Return comma separated tags, used for django-admin'''
        taglist = map(unicode, self.tags.all())
        return ', '.join(taglist)
    
    def tags_list(self):
        '''列出附加到当前对象的标签'''
        return self.tags.all()

    @property
    def html_content(self):
        """Return the entry's content formatted in HTML"""
        import markdown
        def asserted_html(s):
            return ( re.match(r'^\s*<\w+>', s) or
                     re.match(r'^\s*<\w+\s+.*>', s)
                   ) and re.search(r'</\w+>\s*$', s)

        if asserted_html(self.content):
            print "ASSERT HTML"
            return self.content
        elif settings.MARKUP_LANGUAGE == 'markdown':
            return markdown.markdown(self.content, 'abbr,tables,smart_strong'.split(','))
        elif settings.MARKUP_LANGUAGE == 'restructuredtext':
            from docutils.core import publish_parts
            docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
            parts = publish_parts(source=smart_str(self.content),
                                  writer_name="html4css1",
                                  settings_overrides=docutils_settings)
            return force_unicode(parts["fragment"])
        elif '</p>' not in self.content:
            return linebreaks(self.content)
        else:
            return self.content
        

    def generate_summary(self, nchars=200):
        '''提出摘要, 最终返回以HTML片段. 代表插图 + 前N个文字'''
        orig_html = pq(self.html_content)
        # 优先提取带有 cover 类的图片作为封面
        cover = orig_html('img.cover:first') or orig_html('img:first')
        if cover:
            try:
                # 清楚来自图片上传插件(ckeditor)自动添加的属性
                cover.removeAttr('style').removeAttr('width').removeAttr('height')
            except KeyError:
                pass

            cover.addClass('cover')
            orig_src = cover.attr('src')
            # 如果是本地图片, 则封面img标签使用django-filebrowser生成的缩略图
            if orig_src.startswith(settings.MEDIA_URL):
                print "更新封面"
                relative_path = orig_src.replace(settings.MEDIA_URL, '')
                if relative_path.startswith(settings.FILEBROWSER_VERSIONS_BASEDIR):
                    # 如果已经引用的是FileBrowser生成的小尺寸图片,
                    # 则试图推导出原图路径, 并根据原图生成缩略图.
                    relative_path = re.sub(r'^%s' % settings.FILEBROWSER_VERSIONS_BASEDIR,
                                           settings.FILEBROWSER_DIRECTORY, relative_path)
                    
                    # FileBrowser生成图片的后缀模式:
                    postfix_pat = '|'.join(['_'+i for i in settings.FILEBROWSER_ADMIN_VERSIONS])
                    relative_path = re.sub(r'(%s)\.' % postfix_pat, '.', relative_path)
                fileobject = FileObject(relative_path)
                if fileobject.exists():
                    fileobject = fileobject.original
                    thumbnail = fileobject.version_generate('thumbnail')
                    cover.attr('src', thumbnail.url).attr('data-orig-src', orig_src)
                    cover.css(height='100px', width='100px')
                else:
                    print u'引用的图片不存在: %s' % fileobject.path

        summary_text = cgi.escape(orig_html.text()[:int(nchars)])
        return (cover.outerHtml() or "") + \
            (u'<span class="summary-text">%s...</span>' % summary_text) + \
            (u'<a class="more" href="/%d/">阅读全文→</a>' % self.id) + \
            u'<div class="clear"></div>'

    def _cache_version(self):
        '''Used for this instance's current cache version'''
        return time.mktime(self.created.timetuple())

    def _make_summary_cache_key(self, s):
        '''生成缓存summary时使用的key'''
        return 'entry_%s_summary' % (s,)

    def update_summary(self, summary=None):
        '''更新摘要到缓存数据库'''
        key = self._make_summary_cache_key(self.id)
        if not summary:
            summary = self.generate_summary()
        cache.set(key, summary, 60*60*24*30*12,
                  version=self._cache_version()) # cache (almost)for ever.
        return summary
        
    def get_summary(self):
        key = self._make_summary_cache_key(self.id)
        # try get summary in cache first
        summary = cache.get(key, version=self._cache_version())
        if not summary:
            summary = self.update_summary(summary=summary)
        return summary

@receiver(post_save, sender=Entry)
def cache_summary(sender, instance, **kwargs):
    instance.update_summary()
