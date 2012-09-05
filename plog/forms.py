# coding=utf-8
from django import forms
from plog.models import *

class PhotoLogForm(forms.ModelForm):
    class Meta:
        model = PhotoLog
