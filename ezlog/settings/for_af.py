# coding=utf-8
import os

if 'VCAP_SERVICES' not in os.environ:
    raise ExpectedInAppFogEnvironment

import json
vcap_services = json.loads(os.environ['VCAP_SERVICES'])
mysql_srv = vcap_services['mysql-5.1'][0]
cred = mysql_srv['credentials']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': cred['name'],
        'USER': cred['user'],
        'PASSWORD': cred['password'],
        'HOST': cred['hostname'],
        'PORT': cred['port'],
        }
    }
