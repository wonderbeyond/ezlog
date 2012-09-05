#coding=utf-8
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template
from django.http import QueryDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import importlib
from django.db.models import Q
import re

from ezconf import ezsettings
from blog.models import *

search_fields = ('title', 'content')

def _base_context(request):
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    }

def get(request, eid):
    entry = get_object_or_404(Entry, pk=eid, public=True)
    context = { 'entry': entry, }
    return render_to_response('blog/article.html', context,
            context_instance=RequestContext(request, processors=[_base_context]))

def query(request, **kwargs):
    entries = Entry.objects.filter(public=True)

    queries = QueryDict('').copy()
    queries.update(kwargs)
    queries.update(request.GET)

    for k,v in queries.items():
        if k in ('cate', 'cat', 'c', 'category'):
            entries = entries.filter(category=int(v))

        if k in ('tag', 't'):
            entries = entries.filter(tags=int(v))
        
        if k in ('year', 'y'):
            entries = entries.filter(created__year=v)

        if k in ('month', 'm'):
            entries = entries.filter(created__month=v)

        if k in ('day', 'd'):
            entries = entries.filter(created__day=v)

        if k in ('ym', 'ymd'):
            parts = re.split('[-\.\/]', v)
            year,month,day = parts[0],parts[1],len(parts) is 3 and parts[2] or None
            entries = entries.filter(created__year=year, created__month=month)
            if day:
                entries = entries.filter(created__day=day)

        if k == 'search':
            q = Q(pk=-1) # empty queryset
            for f in search_fields:
                q |= Q(**{'%s__contains' %  f: v})
            entries = entries.filter(q)

    try:
        page = int(queries.get('page', 1))
        if page == 0: page = 1
    except ValueError:
        page = 1

    paginator = Paginator(entries, ezsettings.get('blog.articles_per_page', 10))
    try:
        entries = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        entries = paginator.page(paginator.num_pages)

    context = {
        'entry_list': entries,
        'paginator': paginator,
        'current_page': entries.number,
        'current_url': request.get_full_path(), # 当前页面URL
    }
    return render_to_response('blog/list.html', context,
            context_instance=RequestContext(request, processors=[_base_context]))
