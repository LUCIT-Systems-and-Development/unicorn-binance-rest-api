#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://www.lucit.tech/unicorn-binance-rest-api.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api
# Documentation: https://unicorn-binance-rest-api.docs.lucit.tech/
# PyPI: https://pypi.org/project/unicorn-binance-rest-api/
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2017-2021, Sam McHardy (https://github.com/sammchardy)
# Copyright (c) 2021-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import setuptools
from unicorn_binance_rest_api.manager import BinanceRestApiManager

ubra = BinanceRestApiManager()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='unicorn-binance-rest-api',
     version=str(ubra.get_version()),
     author="LUCIT Systems and Development",
     author_email='info@lucit.tech',
     url="https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api",
     description="An unofficial Python API to use the Binance REST API`s (com+testnet, com-margin+testnet, "
                 "com-isolated_margin+testnet, com-futures+testnet, us, tr) in a easy, fast, flexible, robust and "
                 "fully-featured way. ",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=['certifi', 'colorama', 'cryptography', 'dateparser', 'pyOpenSSL', 'requests', 'service-identity',
                       'ujson', 'regex<=2022.3.2'],
     keywords='',
     project_urls={
         'Documentation': 'https://unicorn-binance-rest-api.docs.lucit.tech/',
         'Changes': 'https://unicorn-binance-rest-api.docs.lucit.tech//CHANGELOG.html',
         'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues',
         'Wiki': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/wiki',
         'Author': 'https://www.lucit.tech',
         'Chat': 'https://gitter.im/unicorn-binance-suite/unicorn-binance-rest-api',
         'Telegram': 'https://t.me/unicorndevs',
     },
     python_requires='>=3.6.1',
     packages=setuptools.find_packages(exclude=["tools", "images", "pypi", "sphinx", "docs", ".github"]),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "License :: OSI Approved :: MIT License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

