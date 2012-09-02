# coding=utf-8
from django.conf.urls import patterns, include, url
from plog.models import *
from gviews.views import Gviews

views = Gviews(app='plog', models_map={ 'entry': 'PhotoLog', },
               templates={
                   'query': 'plog/list.html',
                   'get': 'plog/get.html',
               },
               template_object_name='photo',
               items_per_page = 20,
               common_context={
                   'categories': Category.objects.all(),
                   'tags': Tag.objects.all(),
               },)

urlpatterns = patterns('plog.views',
    url(r'^$',                      views['query'], name='plog.index'),
    url(r'^cate/(?P<cate>\d+)/$',   views['query'], name='plog.query'),
    url(r'^tag/(?P<tag>\d+)/$',     views['query'], name='plog.query'),
    url(r'^year/(?P<year>\d+)/$',   views['query'], name='plog.query'),
    url(r'^month/(?P<month>\d+)/$', views['query'], name='plog.query'),
    url(r'^day/(?P<day>\d+)/$',     views['query'], name='plog.query'),
    url(r'^ym/(?P<ym>\d+)/$',       views['query'], name='plog.query'),
    url(r'^ymd/(?P<ymd>\d+)/$',     views['query'], name='plog.query'),

    url(r'^(?P<eid>\d+)/$',         views['get'],   name='plog.get'),
)


