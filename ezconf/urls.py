# coding=utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('ezconf.views',
    url(r'^$',      'index', name='ezconf.index'),
    url(r'^save_settings/$', 'save_settings',  name='ezconf.save_settings'),
    url(r'^export/ezsettings.json$', 'export_settings',  name='ezconf.export_settings'),
    url(r'^import/$', 'import_settings',  name='ezconf.import_settings'),
)
