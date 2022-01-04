#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api
# Documentation: https://lucit-systems-and-development.github.io/unicorn-binance-rest-api
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
from unicorn_binance_rest_api.unicorn_binance_rest_api_manager import BinanceRestApiManager

ubra = BinanceRestApiManager()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='unicorn-binance-rest-api',
     version=str(ubra.get_version()),
     author="LUCIT Systems and Development",
     author_email='info@lucit.tech',
     url="https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api",
     description="An unofficial Python API to use the Binance REST API`s.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=['certifi', 'colorama', 'cryptography', 'dateparser', 'pyOpenSSL', 'requests', 'service-identity',
                       'ujson'],
     keywords='',
     project_urls={
        'Documentation': 'https://lucit-systems-and-development.github.io/unicorn-binance-rest-api/',
        'Wiki': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/wiki',
        'Author': 'https://www.lucit.tech',
     },
     python_requires='>=3.6.1',
     packages=setuptools.find_packages(),
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

