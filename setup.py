#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import find_packages, setup

import cla_common


version = cla_common.__version__

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open("README.rst").read()

setup(
    name="cla_common",
    version=version,
    description="""common code for CLA""",
    long_description=readme,
    author="MOJ",
    author_email="kotecha.ravi@gmail.com",
    url="https://github.com/ministryofjustice/cla_common",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-dateutil",
        "django-extended-choices==0.3.0",
        "requests",
        "speaklater==1.3",
        "pytz==2021.1",
    ],
    license="MIT",
    zip_safe=False,
    keywords="cla_common",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ],
)
