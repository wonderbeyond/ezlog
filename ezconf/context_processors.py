# coding=utf-8
from ezconf import ezsettings
from ezconf.models import *

def settings(request):
    return {'ezsettings': ezsettings.as_dict(),}

def nav_pages(request):
    return {'nav_pages': NavPage.objects.all(),}

def friend_links(request):
    return {'friend_links': FriendLink.objects.all(),}
