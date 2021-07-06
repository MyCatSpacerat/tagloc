#!/usr/bin/env python

from distutils.core import setup

setup(
        name="Tagloc",
        version='0.1',
        description="Quick-scripting for bs4",
        author="Willem Hunt",
        author_email="willemhhunt@gmail.com",
        packages=["tagloc"],
        scripts=["scripts/tagloc"],
        install_requires=['bs4','requests'],
)
