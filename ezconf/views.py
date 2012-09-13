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
        'title': _('EZLog Settings'),
    }
    return render_to_response('ezconf/index.html', context,
                             context_instance=RequestContext(request))

@staff_member_required
@require_POST
def save_settings(request):
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

@staff_member_required
def export_settings(request):
    return HttpResponse(ezsettings.as_readable_json(),
                        content_type='application/json; charset=utf-8')
    
@staff_member_required
def import_settings(request):
    from forms import ImportSettingsForm
    title = _('Import Settings')
    if request.method == 'POST':
        form = ImportSettingsForm(request.POST, request.FILES)
        if form.is_valid():
            ezsettings.reset_settings_with_json_data(request.FILES['file'].read())
            return HttpResponseRedirect(reverse('ezconf.index'))
    else:
        form = ImportSettingsForm()
    return render_to_response('ezconf/import_settings.html', locals(),
                             context_instance=RequestContext(request))    

def update_setting_items(request):
    from forms import UpdateSettingItemsForm
    title = _('Update setting items')
    if request.method == 'POST':
        form = UpdateSettingItemsForm(request.POST, request.FILES)
        if form.is_valid():
            ezsettings.update_setting_items_with_json_data(request.FILES['file'].read())
            return HttpResponseRedirect(reverse('ezconf.index'))
    else:
        form = UpdateSettingItemsForm()
    return render_to_response('ezconf/update_setting_itmes.html', locals(),
                             context_instance=RequestContext(request))    
