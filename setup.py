# -*- coding: utf-8 -*-

# pidlockfile/pidlockfile.py

# PID lock file implementation for use with 
# ‘python-daemon’, an implementation of PEP 3143.
#
# Copyright © 2018 Alexei Igonine <aigonine@gmail.com>
#
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the Apache License, version 2.0 as published by the
# Apache Software Foundation.
# No warranty expressed or implied. See the file ‘LICENSE.ASF-2’ for details.

from __future__ import (absolute_import, unicode_literals)

import os
import codecs

from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = 'pidlockfile',
    packages = ['pidlockfile'],
    version = '0.1',
    description = 'PID file implementation for use with python-daemon',
    long_description = long_description,
    author = 'Alexei Igonine',
    author_email = 'aigonine@gmail.com',
    url = 'https://github.com/aigo9/pidlockfile',
    download_url = 'https://github.com/aigo9/pidlockfile/archive/0.1.tar.gz',
    keywords = ['python', 'daemon', 'python-daemon', 'pid', 'lock'],
    license = "Apache-2",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
   ],
)
