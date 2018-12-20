from .base import *  # @UnusedWildImport


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3'),
    }
}

INSTALLED_APPS += ['storages']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

AWS_STORAGE_BUCKET_NAME = 'zappa-leadbook-static-3incchlv8'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_USE_SSL = True

AWS_HEADERS = {'Cache-Control': 'max-age=86400', }

STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# enf of file
