from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'circle',
        'USER': 'exemple',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
