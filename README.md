# pidlockfile: PID lock file module for use with python-daemon

This module is a replacement for 'python-daemon' pidfile module. TimeoutPIDLockFile class from pidfile implements "advisory" locking. Essentially, it does not really lock anthing. It simply checks lock file existence and, as a result, it can't detect certain situations like server process crush and release the lock.

This module uses python's fcntl facility to lock the PID file. That means that is if daemon process is terminated unexpectedly, lock is automatically released and daemon can be restarted.

# Installation

```shell
pip install pidlockfile
```

# Running unit tests

From the project top level directory execute:

```shell
python -m unittest discover -v
```
