from django.conf.urls import patterns, url
from django.views.generic import TemplateView, RedirectView
import conf

urlpatterns = patterns('',
    url(r'^favicon.ico$', RedirectView.as_view(url=conf.FAVICON_PATH), name='favicon'),
)
