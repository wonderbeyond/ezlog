#!/usr/bin/python
# coding=utf-8
from django.conf.urls import patterns, include, url

from ezconf import ezsettings
from blog.models import *
from gviews.views import Gviews

views = Gviews(app='blog',
               templates={
                   'get': 'blog/article.html',
                   'query': 'blog/list.html'
               },
               template_object_name='entry',
               items_per_page = ezsettings.get('blog.articles_per_page', 10),
               common_context={
                   'categories': Category.objects.all(),
                   'tags': Tag.objects.all(),
               },)

urlpatterns = patterns('blog.views',
    url(r'^$',                           views['query'], name='site.index'),
    url(r'^blog/$',                      views['query'], name='blog.index'),
    url(r'^blog/cate/(?P<cate>\d+)/$',   views['query'], name='blog.query'),
    url(r'^blog/tag/(?P<tag>\d+)/$',     views['query'], name='blog.query'),
    url(r'^blog/year/(?P<year>\d+)/$',   views['query'], name='blog.query'),
    url(r'^blog/month/(?P<month>\d+)/$', views['query'], name='blog.query'),
    url(r'^blog/day/(?P<day>\d+)/$',     views['query'], name='blog.query'),
    url(r'^blog/ym/(?P<ym>\d+)/$',       views['query'], name='blog.query'),
    url(r'^blog/ymd/(?P<ymd>\d+)/$',     views['query'], name='blog.query'),

    url(r'^(?P<eid>\d+)/$',              views['get'], name='blog.get'),
)
