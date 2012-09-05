#for sae
import os, sys
import django.core.handlers.wsgi
import sae

HERE = os.path.dirname(os.path.abspath(__file__))
TO_ABS_PATH = lambda p: os.path.join(HERE, p)

sys.path.insert(0, HERE)
sys.path.insert(0, TO_ABS_PATH('libs/virtualenv.bundle.zip'))


###! Copied form DPress.sites.index.wsgi
import tempfile
#tempfile.tempdir = 'tempdir'
#tempfile.tempdir = sae.core.get_tmp_dir()
import StringIO
class StringIOExt(StringIO.StringIO):
    name = ""
    size = 0
def TemporaryFile(mode='w+b', bufsize=-1, suffix="",
                   prefix='', dir=None, delete=True):
    #f = StringIO.StringIO()
    f = StringIOExt()
    return f
tempfile.TemporaryFile = TemporaryFile
tempfile.NamedTemporaryFile = TemporaryFile
####! End Copied form DPress.sites.index.wsgi

import sae
import sae.storage
import django.core.handlers.wsgi



os.environ['DJANGO_SETTINGS_MODULE'] = 'ezlog.settings'
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())
