import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ""


setup(
    name="django-favicon",
    version=__import__("favicon").__version__,
    author="Evgeny Demchenko",
    author_email="little_pea@list.ru",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/littlepea/django-favicon",
    license="BSD",
    description=u" ".join(__import__("favicon").__doc__.splitlines()).strip(),
    classifiers=[
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
    ],
    long_description=read_file("README.rst"),
    test_suite="runtests.runtests",
    zip_safe=False,
)
