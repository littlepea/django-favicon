from django.urls import re_path
from django.views.generic import RedirectView
from . import conf

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=conf.FAVICON_PATH, permanent=True), name='favicon'),
]
