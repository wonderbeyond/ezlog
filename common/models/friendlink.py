# coding=utf-8
from django.db import models
from common.models.base import BaseModel

class FriendLink(BaseModel):
    name = models.CharField(verbose_name=u'名称', max_length=100, unique=True,
                           help_text=u'将作为链接显示文字')
    desc = models.CharField(verbose_name=u'描述', max_length=200, null=True, blank=True)
    link = models.URLField(verbose_name=u'链接', max_length=200, unique=True)

    class Meta(BaseModel.Meta):
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'

    def __unicode__(self):
        return self.name


