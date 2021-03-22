import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES = {
    'default': {}
}

DATABASES['default'].update(db_from_env)

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'https://lunch-front-dev.herokuapp.com'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
