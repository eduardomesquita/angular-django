from .default import *

DATABASES = {
    'default': {
        'NAME': 'products',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'admin',
        'PASSWORD': 'mysql-server',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}