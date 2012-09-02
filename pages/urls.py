# coding=utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('pages.views',
    url(r'^(?P<pid>\d+)/$', 'get', name='pages.get'),
)
