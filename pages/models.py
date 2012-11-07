# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Page(MPTTModel):
    '''简单页面'''
    title = models.CharField(verbose_name=u'标题', max_length=50, unique=True)
    parent = TreeForeignKey('self', verbose_name=u'父级页面', null=True,
                            blank=True, related_name='children',
                            help_text=u'置空该选项即可创建顶级页面。')
    content = models.TextField(verbose_name=u'内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    public = models.BooleanField(verbose_name=u'发布', default=False)
    allow_comment = models.BooleanField(verbose_name=u'允许评论', default=True)
    in_navigation = models.BooleanField(verbose_name=u'添加到导航', default=False)

    class Meta:
        verbose_name = u'简单页面'
        verbose_name_plural = u'简单页面'
        ordering = ['title']

    class MPTTMeta:
        order_insertion_by=['title']

    @models.permalink
    def get_absolute_url(self):
        return('pages.get', [str(self.id)])

    def __unicode__(self):
        return self.title
    
