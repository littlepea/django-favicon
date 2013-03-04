django-favicon
========================

A reusable app to add simple favicon.ico handling for your site.

Installation
------------------------------------

Install "django-favicon" using pip or easy_install::

    pip install django-favicon

Add "favicon" to your INSTALLED_APPS in settings.py::

      INSTALLED_APPS = (
          ...
          'favicon',
      )

Add favicon URL patterns to urls.py::

      urlpatterns = patterns('',
          ...
          url(r'^', include('favicon.urls')),
      )

Usage
------------------------------------

Put favicon.ico into your STATIC_ROOT. and you good to go, /favicon.ico will automatically redirect to /static/favicon.ico if your STATIC_URL = '/static/'.

Otherwise you can set a custom path to your favicon using FAVICON_PATH setting. For example::

     FAVICON_PATH = STATIC_URL + 'images/favicon.png'

Running the Tests
------------------------------------

You can run the tests with via::

    python setup.py test

or::

    python runtests.py

Credits
------------------------------------

* Developed and maintained under supervision of `Evgeny Demchenko`_

.. _Evgeny Demchenko: https://github.com/littlepea