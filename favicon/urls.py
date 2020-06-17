try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
from django.views.generic import TemplateView, RedirectView
from . import conf

urlpatterns = [url(r'^favicon\.ico$', RedirectView.as_view(url=conf.FAVICON_PATH, permanent=True), name='favicon')]
