# -*- coding: utf-8 -*-

# test/test_pidlockfile.py

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

import unittest
import string
import random
import os
import time

from pidlockfile import PIDLockFile, LockTimeout, AlreadyLocked
from multiprocessing import Process, Queue

class LockAndSleep(object):

    def __init__(self, lock_file_name, sleep_time, out_queue):
        self.sleep_time = sleep_time
        self.out_queue = out_queue
        self.lock_file_name = lock_file_name

    def run(self):
        with PIDLockFile(self.lock_file_name):
            self.out_queue.put(True)
            time.sleep(self.sleep_time)
        self.out_queue.put(True)

def start_process(lock_file_name, sleep_time, out_queue):
    sleeper = LockAndSleep(lock_file_name, sleep_time, out_queue)
    sleeper_proc = Process(
        target=sleeper.run,
        args=()
    )
    sleeper_proc.daemon = True
    sleeper_proc.start()
    return sleeper_proc.pid

def tmp_dir_generator():
    chars = string.ascii_letters + string.digits
    return os.path.join('/tmp', ''.join(random.choice(chars) for _ in range(12)))

class TestPLF(unittest.TestCase):

    def setUp(self):
        self.work_dir = tmp_dir_generator()
        os.mkdir(self.work_dir)
        self.pid_file = os.path.join(self.work_dir, 'pidfile')

    def test_pid_file_created(self):
        with PIDLockFile(self.pid_file):
            self.assertTrue(os.path.exists(self.pid_file))

    def test_compare_pid(self):
        with PIDLockFile(self.pid_file):
            with open(self.pid_file) as f:
                file_pid = int(f.read())
                self.assertEqual(file_pid, os.getpid())

    def test_lock_no_timeout(self):
        sleep_time = 1.0
        q = Queue()
        t1 = time.time()
        start_process(self.pid_file, sleep_time, q)
        q.get()
        with PIDLockFile(self.pid_file):
            t2 = time.time()
            self.assertTrue(os.path.exists(self.pid_file))
            with open(self.pid_file) as f:
                file_pid = int(f.read())
                self.assertEqual(file_pid, os.getpid())
            self.assertGreater(t2 - t1, sleep_time)

    def test_lock_with_timeout(self):
        sleep_time = 1.0
        timeout = 2.0
        q = Queue()
        t1 = time.time()
        start_process(self.pid_file, sleep_time, q)
        q.get()
        with PIDLockFile(self.pid_file, timeout):
            t2 = time.time()
            self.assertTrue(os.path.exists(self.pid_file))
            with open(self.pid_file) as f:
                file_pid = int(f.read())
                self.assertEqual(file_pid, os.getpid())
            self.assertGreater(t2 - t1, sleep_time)
            self.assertLess(t2 - t1, timeout)

    def test_lock_with_timeout_fail(self):
        sleep_time = 2.0
        timeout = 1.0
        q = Queue()
        t1 = time.time()
        start_process(self.pid_file, sleep_time, q)
        q.get()
        with self.assertRaises(LockTimeout):
            with PIDLockFile(self.pid_file, timeout):
                pass
        t2 = time.time()
        self.assertGreater(t2 - t1, timeout)
        self.assertLess(t2 - t1, sleep_time)

    def test_lock_with_0_timeout_fail(self):
        sleep_time = 1.0
        timeout = 0.0
        q = Queue()
        t1 = time.time()
        start_process(self.pid_file, sleep_time, q)
        q.get()
        with self.assertRaises(AlreadyLocked):
            with PIDLockFile(self.pid_file, timeout):
                pass
        t2 = time.time()
        self.assertGreater(t2 - t1, timeout)
        self.assertLess(t2 - t1, sleep_time)

    def test_is_locked_true(self):
        sleep_time = 1.0
        q = Queue()
        locker_pid = start_process(self.pid_file, sleep_time, q)
        q.get()
        plf = PIDLockFile(self.pid_file)
        is_locked = plf.is_locked()
        self.assertEqual(locker_pid, is_locked)

    def test_is_locked_false(self):
        sleep_time = 0.0
        q = Queue()
        start_process(self.pid_file, sleep_time, q)
        q.get()
        q.get()
        plf = PIDLockFile(self.pid_file)
        is_locked = plf.is_locked()
        self.assertIsNone(is_locked)

    def tearDown(self):
        os.remove(self.pid_file)
        os.rmdir(self.work_dir)
        self.pid_file = None
        self.work_dir = None

if __name__ == '__main__':
    unittest.main()

