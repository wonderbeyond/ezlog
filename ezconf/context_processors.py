# coding=utf-8
from ezconf import ezsettings
from ezconf.models import *

def settings(request):
    return {'ezsettings': ezsettings.as_dict(),}
