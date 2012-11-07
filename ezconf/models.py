# coding=utf-8
from django.db import models
from pages.models import Page

class FriendLink(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=100, unique=True)
    desc = models.CharField(verbose_name=u'简单描述', max_length=200, null=True, blank=True)
    link = models.URLField(verbose_name=u'链接', max_length=200, unique=True)

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'

    def __unicode__(self):
        return self.name

class EZSettingsData(models.Model):
    '''存储配置数据, 仅一行数据. 数据一json形式存储在data字段中'''
    data = models.TextField()
    mtime = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
