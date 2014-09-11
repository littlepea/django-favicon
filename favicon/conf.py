from django.conf import settings

FAVICON_PATH = getattr(settings, 'FAVICON_PATH', '%sfavicon.ico' % settings.STATIC_URL)
