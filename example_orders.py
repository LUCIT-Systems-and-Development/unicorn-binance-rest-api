#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_orders.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://www.lucit.tech/unicorn-binance-rest-api.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api
# Documentation: https://unicorn-binance-rest-api.docs.lucit.tech/
# PyPI: https://pypi.org/project/unicorn-binance-rest-api/
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2021-2023, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
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

from unicorn_binance_rest_api.manager import BinanceRestApiManager
import logging
import os

# https://docs.python.org/3/library/logging.html#logging-levels
logging.getLogger("unicorn_binance_rest_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

api_key = ""
api_secret = ""

# To use this library you need a valid UNICORN Binance Suite License: https://medium.lucit.tech/87b0088124a8
ubra = BinanceRestApiManager(api_key=api_key, api_secret=api_secret, tld="com")

# uncomment to access testnet endpoints
# spot:
# ubra.API_URL = 'https://testnet.binance.vision/api'
# futures:
# ubra.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

print(ubra.get_all_orders(symbol='BTCUSDT', limit=10))

print(ubra.get_account())

print(ubra.get_asset_balance(asset='BTC'))

print(ubra.get_symbol_ticker(symbol="BTCUSDT"))

print(ubra.get_open_orders(symbol='BTCUSDT'))

# ubra.create_order(symbol='ETHUSDT', side="BUY", quantity=2, stopPrice='2000', type='STOP_LOSS')

# buy_limit_order = ubra.order_limit_buy(symbol='BTCUSDT', quantity=2, price='0.0001')

# sell_limit_order = ubra.order_limit_sell(symbol='BTCUSDT', quantity=2, price='0.0003')

existing_orders = ubra.get_open_orders(symbol='BTCUSDT')

for order in existing_orders:
    print(ubra.cancel_order(symbol="BTCUSDT", orderId=order['orderId']))

ubra.stop_manager()