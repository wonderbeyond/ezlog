# coding=utf-8
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext, Context, Template
from django.shortcuts import render_to_response, get_object_or_404

from pages.models import *

def get(request, pid):
    if request.user.is_superuser:
        page = get_object_or_404(Page, pk=pid)
    else:
        page = get_object_or_404(Page, pk=pid, public=True)

    context = {
        'page': page,
    }
    return render_to_response('pages/page.html', context,
                              context_instance=RequestContext(request))
