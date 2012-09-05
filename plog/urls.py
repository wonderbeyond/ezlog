# coding=utf-8
from django.conf.urls import patterns, include, url
from plog.models import *

urlpatterns = patterns('plog.views',
    url(r'^$',                      'query', name='plog.index'),
    url(r'^cate/(?P<cate>\d+)/$',   'query', name='plog.query'),
    url(r'^tag/(?P<tag>\d+)/$',     'query', name='plog.query'),
    url(r'^year/(?P<year>\d+)/$',   'query', name='plog.query'),
    url(r'^month/(?P<month>\d+)/$', 'query', name='plog.query'),
    url(r'^day/(?P<day>\d+)/$',     'query', name='plog.query'),
    url(r'^ym/(?P<ym>\d+)/$',       'query', name='plog.query'),
    url(r'^ymd/(?P<ymd>\d+)/$',     'query', name='plog.query'),

    url(r'^(?P<eid>\d+)/$',         'get',   name='plog.get'),
)


