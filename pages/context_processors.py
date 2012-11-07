# coding=utf-8
from pages.models import Page

def nav_pages(request):
    return {'nav_pages': Page.objects.filter(public=True, in_navigation=True),}
