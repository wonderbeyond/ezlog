from django.conf import settings
import os
import imp
from glob import glob

class ActionMount(type):
    '''Action mount meta class'''
    def __init__(mcs, name, bases, dict):
        if not hasattr(mcs, 'actions'):
            mcs.actions = []
        else:
            mcs.actions.append(mcs)

    def bound_actions(cls, *args, **kwargs):
        return [p(*args, **kwargs) for p in cls.actions]

class BaseMountPoint(object):
    '''Base class for action mount point'''
    def __init__(self, *args, **kwargs):
        pass
    def umount(self):
        pass

_extensions_loaded = False
def mount_all():
    def load_extensions_in_path(path):
        for p in glob(os.path.join(path, '*')):
            if os.path.isdir(p):
                module_name = os.path.basename(p)
                pyfile = os.path.join(p, '__init__.py')
                if os.path.exists(pyfile):
                    imp.load_source(module_name, pyfile)
            elif p.endswith('.py'):
                module_name = os.path.basename(p[:-3])
                imp.load_source(module_name, p)

    global _extensions_loaded
    if not _extensions_loaded:
        print "loading all extensions..."
        load_extensions_in_path(path=settings.EXTENSION_PATH)
        _extensions_loaded = True

#==================================================
# Declare action mount points

class PostSave(BaseMountPoint):
    '''an example mount point

    ===============================================
    filter(obj)     change data for obj
    post_save()     callback after save
    ===============================================
    '''
    __metaclass__ = ActionMount

class PostOutputFilter(BaseMountPoint):
    __metaclass__ = ActionMount
    def get(self):
        pass
