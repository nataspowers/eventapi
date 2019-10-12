from .settings import *

# Static storage in S3 from django_s3_storage
DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
S3_BUCKET = "eventapi-static"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET
STATIC_URL = "https://%s.s3.amazonaws.com/" % S3_BUCKET


#Use S3 backed sqlite DB from zappa_django_utils
DATABASES = {
    'default': {
        'ENGINE': 'zappa_django_utils.db.backends.s3sqlite',
        'NAME': 'sqlite.db',
        'BUCKET': 'eventapi-db'
    }
}
