# coding=utf-8
import dj_database_url

def _get_cache():
  import os
  try:
    os.environ['MEMCACHE_SERVERS'] = os.environ['MEMCACHIER_SERVERS']
    os.environ['MEMCACHE_USERNAME'] = os.environ['MEMCACHIER_USERNAME']
    os.environ['MEMCACHE_PASSWORD'] = os.environ['MEMCACHIER_PASSWORD']
    return {
      'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': os.environ['MEMCACHIER_SERVERS'],
        'TIMEOUT': 500,
        'BINARY': True,
      }
    }
  except:
    return {
      'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
      }
    }


DEBUG = False
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
CACHES = _get_cache()
