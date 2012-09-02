# coding=utf-8
from django.contrib import admin
from pages.models import *

class PageAdmin(admin.ModelAdmin):
    class Media:
        js = ('ckeditor/ckeditor.js',
              'ckeditor/config.js',
              'admin/pages/js/ckeditor-setup.js',
             )

admin.site.register(Page, PageAdmin)
