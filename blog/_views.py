# coding=utf-8
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template
from django.http import QueryDict

from blog.models import *
