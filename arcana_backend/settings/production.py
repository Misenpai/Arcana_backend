from .base import *

DEBUG = False

ALLOWED_HOSTS = ['arcana', 'localhost', '127.0.0.1', '192.168.29.85','192.168.1.44','172.17.0.1','arcana-backend.onrender.com']

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# HTTPS Settings (uncomment when using HTTPS)
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
