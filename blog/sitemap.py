# coding=utf-8
from django.contrib.sitemaps import Sitemap
from blog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Entry.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.modified
