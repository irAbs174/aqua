'''DEV : #ABS174'''

from pathlib import Path
import os


ALLOWED_HOSTS = ['8000-irabs174-aqua-5myi5ehxvkr.ws-eu103.gitpod.io']

CSRF_TRUSTED_ORIGINS = ['https://8000-irabs174-aqua-5myi5ehxvkr.ws-eu103.gitpod.io']

WAGTAILADMIN_BASE_URL = '8000-irabs174-aqua-5myi5ehxvkr.ws-eu103.gitpod.io'

BASE_DIR = Path(__file__).resolve().parent.parent

WAGTAIL_SITE_NAME = 'Aqua'

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

SE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'AQU.db',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

SECRET_KEY = 'django-insecure-h^8r%xy*wrme7@v=1*n&&j)mc1b4#^0nfxk-9#gr(do$24xw4z'

DEBUG = True