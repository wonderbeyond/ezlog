# coding=utf-8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from pages.models import *

class PageAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    fields = ('title', 'parent', 'public', 'in_navigation', 'allow_comment',
    'content',)
    list_display = ('title', 'created', 'modified',
                    'public', 'allow_comment', 'in_navigation')
    list_filter = ('created', 'modified', 'public')
    search_fields = ('title', 'content')

    change_list_template = 'admin/pages/page/change_list.html'

    class Media:
        js = ('ckeditor/ckeditor.js',
              'ckeditor/config.js',
              'js/ckeditor-setup.js',
             )

admin.site.register(Page, PageAdmin)
