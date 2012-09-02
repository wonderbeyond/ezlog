# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    '''简单页面'''
    title = models.CharField(verbose_name=u'标题', max_length=50, unique=True)
    content = models.TextField(verbose_name=u'内容')
    public = models.BooleanField(verbose_name=u'发布', default=True)

    class Meta:
        verbose_name = u'简单页面'
        verbose_name_plural = u'简单页面'

    @models.permalink
    def get_absolute_url(self):
        return('pages.get', [str(self.id)])

    def __unicode__(self):
        return self.title
    
