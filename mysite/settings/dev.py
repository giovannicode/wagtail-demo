from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zdj5o%izc51%a20juibqgnd09mcci#lq+ai81!=w%^ccn0qc@_'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
