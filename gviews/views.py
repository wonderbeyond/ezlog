#coding=utf-8
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template
from django.http import QueryDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import importlib
from django.db.models import Q
import re, json

def Gviews(app, templates,
           template_object_name='entry', # 在模板中引用词条所使用的变量名称,
                                         # 引用列表的变量为:
                                         # template_object_name + '_list'
           items_per_page=10,   # 列表页面中每页列出项目数.
           common_context = {}, # 提供给App中所有视图使用的通用模板变量.
           search_fields = ('title', 'content'),
           models_map={'entry': 'Entry',
                       'category': 'Category',
                       'tag': 'Tag',
                      }):
    '''适用于Blog/CMS应用的通用视图

    要求应用的 models 模块中包含 Entry, Category, Tag 的对应模型.
    其中Entry是用于显示和查找的词条, Category是Entry的分类, Tag是Entry的标签.

    要求词条模型属性使用如下标准:
            public
            category(ForeignKey)
            tags(ManyToManyField)
            created(DateTimeField)
            ...
    
    templates用来提供各个视图使用的模板:
        get: 用于单个词条
        query: 用于词条列表
    '''

    # 导入app的模型
    models = importlib.import_module('%s.models' % app)

    default_models_map = {'entry': 'Entry',
                          'category': 'Category',
                          'tag': 'Tag',
                         }
    default_models_map.update(models_map)
    models_map = default_models_map

    Entry    = getattr(models, models_map['entry'])
    Category = getattr(models, models_map['category'], None)
    Tag      = getattr(models, models_map['tag'], None)

    def _base_context(request):
        return common_context

    def get(request, eid):
        entry = get_object_or_404(Entry, pk=eid, public=True)
        context = { template_object_name: entry, }
        return render_to_response(templates['get'], context,
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

        paginator = Paginator(entries, items_per_page)
        try:
            entries = paginator.page(page)
        except (EmptyPage, PageNotAnInteger):
            entries = paginator.page(paginator.num_pages)

        context = {
            template_object_name+'_list': entries,
            'paginator': paginator,
            'current_page': entries.number,
            'current_url': request.get_full_path(), # 当前页面URL
            #'query_dict': json.dumps(request.GET), # GET参数(JSON).
        }
        return render_to_response(templates['query'], context,
                context_instance=RequestContext(request, processors=[_base_context]))

    return {
        'get': get,
        'query': query,
    }


