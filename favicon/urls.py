from django.conf.urls import patterns, url
from django.views.generic import TemplateView, RedirectView
import conf

urlpatterns = patterns('',
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': conf.FAVICON_PATH}, name='favicon'),
)