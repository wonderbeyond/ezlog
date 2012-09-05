# coding=utf-8
from django import forms
from blog.models import *

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry


