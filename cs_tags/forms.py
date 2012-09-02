# coding=utf-8

from django import forms
from django.utils.safestring import mark_safe
from django.forms.util import flatatt, to_current_timezone
from django.utils.encoding import StrAndUnicode, force_unicode

import re

class TagsInput(forms.widgets.TextInput):
    input_type = 'text'
    def render(self, name, value, attrs=None):
        '''负责生成逗号列表'''
        if value:
            value = ', '.join([Tag.objects.get(pk=i).name for i in value])
        else:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        
        if value != '':
            final_attrs['value'] = force_unicode(self._format_value(value))
        
        return mark_safe(u'<input%s />' % flatatt(final_attrs))

class TagsFormField(forms.CharField):
    widget = TagsInput
    def clean(self, tags_raw):
        '''根据表单输入的逗号列表生成Tag实例列表'''
        tagwords = [ t.strip() for t in re.split('[\s,，]+', tags_raw) if t ]
        return [ Tag.objects.get_or_create(name=t)[0] for t in set(tagwords) ]
