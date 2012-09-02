# coding=utf-8
from django.db import models
from django import forms

from blog.widgets import *

class RichTextField(models.TextField):
    def formfield(self, **kwargs):
        print kwargs
        defaults = { 'form_class': RichTextFormField, }
        defaults.update(kwargs)
        return super(RichTextField, self).formfield(**defaults)

class RichTextFormField(forms.fields.Field):
    def __init__(self, *args, **kwargs):
        kwargs.update({'widget': RichTextWidget()})
        super(RichTextFormField, self).__init__(*args, **kwargs)
