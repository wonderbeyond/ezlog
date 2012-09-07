from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site

import blog.urls

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^settings/',  include('ezconf.urls')),
    url(r'^i/',         include('plog.urls')),
    url(r'^p/',         include('pages.urls')),
    url(r'^np/(?P<pid>\d+)/$', 'ezconf.views.get_nav_page', name='navpage.get'),
) + blog.urls.urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)
