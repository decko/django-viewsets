#!/usr/bin/env python

from setuptools import setup, find_packages

from viewsets import __version__


setup(
    name='django-viewsets',
    version=__version__,
    description='',
    url='https://github.com/alexey-grom/django-viewsets',
    author='alxgrmv@gmail.com',
    packages=find_packages(),
    install_requires=['django',
                      'six', ],
)