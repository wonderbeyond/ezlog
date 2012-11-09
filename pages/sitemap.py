# coding=utf-8
from django.contrib.sitemaps import Sitemap
from pages.models import Page

class PageSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Page.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.modified
