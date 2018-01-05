# -*- coding: utf-8 -*-

# pidlockfile/__init__.py
# PID lock file implementation for use with 
# ‘python-daemon’, an implementation of PEP 3143.
#
# Copyright © 2018 Alexei Igonine <aigonine@gmail.com>
#
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the Apache License, version 2.0 as published by the
# Apache Software Foundation.
# No warranty expressed or implied. See the file ‘LICENSE.ASF-2’ for details.

from __future__ import(absolute_import, unicode_literals)

from .pidlockfile import(PIDLockFile, AlreadyLocked, LockTimeout)

