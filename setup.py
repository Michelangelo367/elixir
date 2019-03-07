#!/usr/bin/python3

import sys
import os

if sys.version_info < (3,0):
    sys.exit("elixir requires python 3.")

from setuptools import setup

VERSION = "0.2.8"

options = dict(
    name="elixir",
    version=VERSION,
    description="Youtube Navigator",
    keywords=["video", "music", "audio", "youtube", "stream", "download"],
    author="np1",
    author_email="loouis@gmail.com",
    url="https://github.com/loouislow81/elixir",
    download_url="https://github.com/loouislow81/elixir/archive/v%s.tar.gz" % VERSION,
    packages=['elixir_yt', 'elixir_yt.commands', 'elixir_yt.listview', 'elixir_yt.players'],
    entry_points={'console_scripts': ['elixir = elixir_yt:main.main']},
    install_requires=['pafy >= 0.3.82, != 0.4.0, != 0.4.1, != 0.4.2'],
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Multimedia :: Video",
        "Environment :: Console",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    options={
        "py2exe": {
            "excludes": ("readline, win32api, win32con, dbus, gi,"
                         " urllib.unquote_plus, urllib.urlencode,"
                         " PyQt4, gtk"),
            "bundle_files": 1
        }
    },
    package_data={"": ["LICENSE"]},
    long_description=open("README.rst").read()
)

if sys.platform.startswith('linux'):
    # Install desktop file. Required for mpris on Ubuntu
    options['data_files'] = [('share/applications/', ['elixir.desktop'])]

if os.name == "nt":
    try:
        import py2exe
        # Only setting these when py2exe imports successfully prevents warnings
        # in easy_install
        options['console'] = ['elixir']
        options['zipfile'] = None
    except ImportError:
        pass

setup(**options)
