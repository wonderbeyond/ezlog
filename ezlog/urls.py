from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site

urlpatterns = patterns('',
    #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/',  include('django.contrib.admindocs.urls')),
    url(r'^admin/',      include(admin.site.urls)),
    url(r'^grappelli/',  include('grappelli.urls')),

    url(r'^',            include('blog.urls')),
    url(r'^i/',          include('plog.urls')),
    url(r'^p/',          include('pages.urls')),
    url(r'^ezsettings/', include('ezconf.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)
