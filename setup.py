#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import cla_common

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = cla_common.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='cla_common',
    version=version,
    description="""common code for CLA""",
    long_description=readme + '\n\n' + history,
    author='MOJ',
    author_email='kotecha.ravi@gmail.com',
    url='https://github.com/ministryofjustice/cla_common',
    packages=[
        'cla_common',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='cla_common',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
