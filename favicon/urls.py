from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from . import conf

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url=conf.FAVICON_PATH, permanent=True), name='favicon'),
]
