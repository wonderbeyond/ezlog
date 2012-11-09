#!/usr/bin/python
# coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^(?P<eid>\d+)/$',              'get',   name='blog.get'),

    url(r'^$',                           'query', name='site.index'),
    url(r'^blog/$',                      'query', name='blog.index'),
    url(r'^blog/cate/(?P<cate>\d+)/$',   'query', name='blog.query'),
    url(r'^blog/tag/(?P<tag>\d+)/$',     'query', name='blog.query'),
    url(r'^blog/year/(?P<year>\d+)/$',   'query', name='blog.query'),
    url(r'^blog/month/(?P<month>\d+)/$', 'query', name='blog.query'),
    url(r'^blog/day/(?P<day>\d+)/$',     'query', name='blog.query'),
    url(r'^blog/ym/(?P<ym>\d+)/$',       'query', name='blog.query'),
    url(r'^blog/ymd/(?P<ymd>\d+)/$',     'query', name='blog.query'),
)
