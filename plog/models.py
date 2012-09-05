#coding=utf-8
from django.db import models
from django.contrib.auth.admin import User
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=100, default=u'视觉盛宴', unique=True)
    desc = models.CharField(verbose_name=u'描述', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = u"图集"
        verbose_name_plural = u"图集"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('plog.query', [], dict(cate=self.id))
    

class PhotoLog(models.Model):
    author = models.ForeignKey(User, verbose_name=u'作者', editable=False)
    photo = models.ImageField(verbose_name=u'图片', max_length=200,
                              upload_to='uploads/plog/%Y/%m/%d')
    title = models.CharField(verbose_name=u'标题', max_length=200, unique=True)
    category = models.ForeignKey(Category, verbose_name=u'所属图集')
    tags = TaggableManager(blank=True)
    desc = models.TextField(verbose_name=u'描述', max_length=500, blank=False)
    created = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    public = models.BooleanField(verbose_name=u'是否公开', default=True)

    
    class Meta:
        verbose_name = '图志'
        verbose_name_plural = '图志'
        ordering = ['-created']

    @models.permalink
    def get_absolute_url(self):
        return ('plog.get', [str(self.id)], {})        
    
    def __unicode__(self):
        return self.title
