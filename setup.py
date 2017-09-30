#!/usr/bin/env python
#coding=utf-8

from setuptools import setup, find_packages


import sys
import re


if sys.version_info < (2, 6):
    sys.exit('Python 2.5 or greater is required.')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as fp:
    readme = fp.read()


setup(
    name = 'Alcman',
    version = '1.0.0',
    keywords = ('Alcman', 'paramiko','ansible'),
    description = 'devops use Alcman to  Batch Management System and Production Application ',

    long_description = readme,

    license = 'Apache Licence 2.0',

    url = 'https://github.com/x0fengluo/Alcman',
    author = 'x0fengluo@gmail.com',
    author_email = 'x0fengluo@gmail.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['paramiko','PyYAML'],
)
