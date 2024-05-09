#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_easy_migration_from_python-binance.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://www.lucit.tech/unicorn-binance-rest-api.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api
# Documentation: https://unicorn-binance-rest-api.docs.lucit.tech/
# PyPI: https://pypi.org/project/lucit-licensing-python
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2017-2021, Sam McHardy (https://github.com/sammchardy)
# Copyright (c) 2021-2023, LUCIT Systems and Development (https://www.lucit.tech)
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

from unicorn_binance_rest_api.manager import BinanceRestApiManager as Client
import logging
import os

# https://docs.python.org/3/library/logging.html#logging-levels
logging.getLogger("unicorn_binance_rest_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

api_key = "aaa"
api_secret = "bbb"

# To use this library you need a valid UNICORN Binance Suite License: https://medium.lucit.tech/87b0088124a8
client = Client(api_key, api_secret, tld="com")

# get market depth
depth = client.get_order_book(symbol='BNBBTC')
print(f"{depth}")

# get all symbol prices
prices = client.get_all_tickers()
print(f"{prices}")

client.stop_manager()

