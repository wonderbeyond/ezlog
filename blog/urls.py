#!/usr/bin/python
# coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^(?P<eid>\d+)/$',         'get',   name='blog.get'),

    url(r'^$',                      'query', name='site.index'),
    url(r'^blog/$',                 'query', name='blog.index'),
    url(r'^cate/(?P<cate>\d+)/$',   'query', name='blog.query'),
    url(r'^tag/(?P<tag>\d+)/$',     'query', name='blog.query'),
    url(r'^year/(?P<year>\d+)/$',   'query', name='blog.query'),
    url(r'^month/(?P<month>\d+)/$', 'query', name='blog.query'),
    url(r'^day/(?P<day>\d+)/$',     'query', name='blog.query'),
    url(r'^ym/(?P<ym>\d+)/$',       'query', name='blog.query'),
    url(r'^ymd/(?P<ymd>\d+)/$',     'query', name='blog.query'),
)
