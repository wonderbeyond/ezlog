# coding=utf-8
from django import forms
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class RichTextWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        '''负责生成逗号列表'''
        final_attrs = self.build_attrs(attrs, name=name)
        
        class_ = 'richtext ckeditor'
        if final_attrs.get('class'):
            final_attrs['class'] += (' ' + class_)
        else:
            final_attrs['class'] = class_

        return super(RichTextWidget, self).render(name, value, final_attrs)
