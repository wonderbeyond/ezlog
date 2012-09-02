# coding=utf-8
from django.db import models

from plog.forms import *

class TagsField(models.ManyToManyField):
    pass
    #def formfield(self, **kwargs):
    #    defaults = {'form_class': TagsFormField}
    #    defaults.update(kwargs)
    #    return TagsFormField(**defaults)
