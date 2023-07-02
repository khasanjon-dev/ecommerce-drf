from root.settings import *  # noqa

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecommerce',
        'USER': 'postgres',
        'PASSWORD': 1,
        'HOST': 'localhost',
        'PORT': 5432
    }
}
