# coding=utf-8
from ezconf import ezsettings
from ezconf.models import *
from pages.models import Page

def settings(request):
    return {'ezsettings': ezsettings.as_dict(),}

def nav_pages(request):
    return {'nav_pages': Page.objects.filter(public=True, in_navigation=True),}

def friend_links(request):
    return {'friend_links': FriendLink.objects.all(),}
