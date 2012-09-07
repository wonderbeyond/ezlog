# coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template
from django.core.urlresolvers import reverse

from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST, require_GET

from ezconf import ezsettings

from ezconf.models import *

@staff_member_required
@never_cache
@require_GET
def index(request):
    context = {
        'settings': ezsettings.settings,
        'title': _('EZLog settings'),
    }
    return render_to_response('ezconf/index.html', context,
                             context_instance=RequestContext(request))

@staff_member_required
@require_POST
def save(request):
    '''save settings from user form'''
    for g in ezsettings.settings:
        for f in g['fields']:
            form_name = '%s.%s' % (g['name'], f['name'])
            f['value'] = request.POST[form_name]
    ezsettings.save()

    if request.POST.get('_continue'):
        redirect_to = reverse('ezconf.index')
    else:
        redirect_to = reverse('admin:index')

    return HttpResponseRedirect(redirect_to)

def get_nav_page(request, pid):
    page = get_object_or_404(NavPage, pk=pid)
    context = {
        'page': page,
    }
    return render_to_response('ezconf/nav-page.html', context,
                              context_instance=RequestContext(request))
