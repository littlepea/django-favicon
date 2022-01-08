from django.urls import path
from django.views.generic import RedirectView
from . import conf

urlpatterns = [
    path(r'^favicon\.ico$', RedirectView.as_view(url=conf.FAVICON_PATH, permanent=True), name='favicon'),
]
