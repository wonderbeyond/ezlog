# coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('ezconf.views',
    url(r'^$',      'index', name='ezconf.index'),
    url(r'^save/$', 'save',  name='ezconf.save'),
)
