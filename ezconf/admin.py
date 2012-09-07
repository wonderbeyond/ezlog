# coding=utf-8
from django.contrib import admin
from ezconf.models import *

class NavPageAdmin(admin.ModelAdmin):
    class Media:
        js = ('ckeditor/ckeditor.js',
              'ckeditor/config.js',
              'admin/pages/js/ckeditor-setup.js',
             )

admin.site.register(NavPage, NavPageAdmin)
admin.site.register(FriendLink)
