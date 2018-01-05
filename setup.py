from distutils.core import setup

setup(
    name = 'pidlockfile',
    packages = ['pidlockfile'],
    version = '0.1',
    description = 'PID file implementation for use with python-daemon',
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
