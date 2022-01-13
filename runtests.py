#!/usr/bin/env python
import os
import sys
import django

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'favicon',
        ),
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
        STATIC_URL='/static/',
        STATIC_ROOT=os.path.join(BASE_DIR, "static"),
        STATICFILES_DIRS=(
            os.path.join(BASE_DIR, "favicon", "static")
        ),
    )

django.setup()
from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['favicon', ])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
