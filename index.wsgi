import os
import django.core.handlers.wsgi
import sae

HERE = os.path.dirname(os.path.abspath(__file__))
TO_ABS_PATH = lambda p: os.path.join(HERE, p)

sys.path.insert(0, HERE)
sys.path.insert(0, TO_ABS_PATH('lib'))


os.environ['DJANGO_SETTINGS_MODULE'] = 'ezlog.settings'

application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())
