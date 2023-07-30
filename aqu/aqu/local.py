from pathlib import Path
import os


SECRET_KEY = 'django-insecure-o(vuj0!vodjeqp9cw3$-=_s%^_5%(_if=&s78+dbc5s*fhoqc1'

DEBUG = True

CSRF_TRUSTED_ORIGINS = ['https://8005-irabs174-aqua-80ao813mqf1.ws-eu102.gitpod.io',]

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['8005-irabs174-aqua-80ao813mqf1.ws-eu102.gitpod.io',]
