# coding=utf-8
import sae.const

COMPRESS_ENABLED = True

DEFAULT_FILE_STORAGE = 'saestorage.SaeStorage'
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_VERSIONS_BASEDIR = ''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': sae.const.MYSQL_DB,
        'USER': sae.const.MYSQL_USER,
        'PASSWORD': sae.const.MYSQL_PASS,
        'HOST': sae.const.MYSQL_HOST,
        'PORT': sae.const.MYSQL_PORT,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'ezlog_cache',
        'KEY_PREFIX': 'ezlog',
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
            'CULL_FREQUENCY': 4,
        }
    }
}
