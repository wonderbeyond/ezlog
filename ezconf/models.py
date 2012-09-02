# coding=utf-8
from django.db import models
from pages.models import Page

class NavPage(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=50, unique=True)
    page = models.ForeignKey(Page, verbose_name=u'页面')

    class Meta:
        verbose_name = u'导航页面'
        verbose_name_plural = u'导航页面'

    def __unicode__(self):
        return self.title

class FriendLink(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=100, unique=True)
    desc = models.CharField(verbose_name=u'简单描述', max_length=200, null=True, blank=True)
    link = models.URLField(verbose_name=u'链接', max_length=200, unique=True)

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'

    def __unicode__(self):
        return self.name
