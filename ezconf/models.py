# coding=utf-8
from django.db import models

class EZSettingsData(models.Model):
    '''存储配置数据, 仅一行数据. 数据一json形式存储在data字段中'''
    data = models.TextField()
    mtime = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
