# coding=utf-8
from django.contrib import admin
from django.db import models
from plog.models import *
from plog.forms import *

from filebrowser.widgets import FileInput

class PhotoLogInline(admin.StackedInline):
    model = PhotoLog
    form = PhotoLogForm
    formfield_overrides = {
        models.ImageField: {'widget': FileInput},
    }

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PhotoLogInline]

class PhotoLogAdmin(admin.ModelAdmin):
    form = PhotoLogForm
    formfield_overrides = {
        models.ImageField: {'widget': FileInput},
    }
    def save_model(self, request, obj, form, change):
        '''通过admin界面添加图志时, 自动把作者设为当前用户'''
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(PhotoLog, PhotoLogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)

