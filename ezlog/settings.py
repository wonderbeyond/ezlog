# coding='utf-8'
import os

PROJECT_ROOT = os.path.abspath( os.path.dirname(os.path.dirname(__file__)) )
TO_ABS_PATH = lambda p: os.path.join(PROJECT_ROOT, p)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

COMPRESS_ENABLED = not DEBUG
#COMPRESS_PARSER = 'compressor.parser.LxmlParser'
COMPRESS_OFFLINE = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATA_DIR = TO_ABS_PATH('data') # may used for storage of various data.

DB_SQLITE3 = {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': TO_ABS_PATH('data/ezlog.sqlite3'),
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
}

DB_MYSQL = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'ezlog',
    'USER': 'wonder',
    'PASSWORD': 'wo',
    'HOST': 'localhost',
    'PORT': '3306',
}

DATABASES = {
    'default': DB_SQLITE3,
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

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = TO_ABS_PATH('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_VERSIONS_BASEDIR = 'thumbnails/'

FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big',]
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': '100x100', 'width': 100, 'height': 100, 'opts': 'crop'},
    'small': {'verbose_name': 'Small(140)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium(320)', 'width': 320, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big(460)', 'width': 460, 'height': '', 'opts': ''},
    #'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
}

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = TO_ABS_PATH('static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TO_ABS_PATH('common/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1fjx4f(s+f+7+q#vst*p@ft^&amp;m6f7j@g8lrnjvu(hzd8242x@%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    "ezconf.context_processors.settings",
    "ezconf.context_processors.friend_links",
    "ezconf.context_processors.nav_pages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ezlog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ezlog.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TO_ABS_PATH('common/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'south',
    'compressor',
    'ezconf',
    'pages',
    'blog',
    'plog',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'kama',
        'height': 460,
        #'filebrowserWindowWidth' : '900',
        #'filebrowserWindowHeight' : '600',
        'toolbar': 'MyToolbar',
        'toolbar_MyToolbar': [
            { 'name': 'clipboard',
             'items' : [ 'Paste','PasteText','PasteFromWord','-',
                        'Undo','Redo','-','Find', ]
            },


            { 'name': 'basicstyles',
             'items' : [ 'Bold','Italic','Underline','Strike',
                        'Subscript','Superscript','-','RemoveFormat' ]
            },

            { 'name': 'colors',
             'items' : [ 'TextColor','BGColor' ]
            },


            { 'name': 'styles',
             'items' : [ 'Styles','Format','Font','FontSize' ]
            },

            '/',

            { 'name': 'paragraph',
             'items' : [ 'NumberedList','BulletedList','-',
                        'Outdent','Indent','-','Blockquote','CreateDiv',
                        '-','JustifyLeft','JustifyCenter',
                        'JustifyRight','JustifyBlock', ]
            },

            { 'name': 'links',
             'items' : [ 'Link','Unlink' ]
            },

            { 'name': 'insert',
             'items' : [ 'Templates','-','Image','Table',
                        'HorizontalRule','Smiley','SpecialChar',
                        'PageBreak','Iframe' ]
            },

            { 'name': 'tools',
             'items' : [ 'Maximize', '-', 'ShowBlocks',
                        'DocProps','Preview', '-', 'Source']
            },
        ]
    },
}

GRAPPELLI_ADMIN_TITLE = u'EZLog\u7ad9\u70b9\u7ba1\u7406'


if 'DATABASE_URL' in os.environ:
    # Heroku
    from settings_heroku import *

if 'SERVER_SOFTWARE' in os.environ:
    # SAE
    from ezlog.settings_sae import *
