"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'ezlog.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

from django.core.urlresolvers import reverse

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('EZLog Content Management'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*', 'ezconf.*'),
        ))

        self.children.append(modules.ModelList(
            _('Nav and Links'),
            column=1,
            collapsible=False,
            models=('ezconf.*',),
        ))

        
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('Django Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        # EZLog settings
        self.children.append(modules.LinkList(
            _('EZLog Settings'),
            column=2,
            collapsible=False,
            children=[{
                'title': _('Site Parameters'),
                'url': reverse('ezconf.index'),
                'external': False,
            }]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            collapsible=False,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Quick Links'),
            column=2,
            collapsible=False,
            children=[
                {
                    'title': _('Site Home'),
                    'url': reverse('site.index'),
                    'external': False,
                },
                {
                    'title': _('Plog'),
                    'url': reverse('plog.index'),
                    'external': False,
                },
            ]
        ))
        
        # Feedback & Support
        self.children.append(modules.LinkList(
            _('Feedback and Support'),
            column=2,
            collapsible=False,
            children=[
                {
                    'title': _('EZLog official blog'),
                    'url': 'http://ezlog.sinaapp.com/',
                    'external': True,
                },
                {
                    'title': _('EZLog Author\'s Micro-blog'),
                    'url': 'http://weibo.com/wber/',
                    'external': True,
                },
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


