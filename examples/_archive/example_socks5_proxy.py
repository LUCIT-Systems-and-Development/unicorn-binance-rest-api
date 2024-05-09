#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_socks5_proxy.py
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

from unicorn_binance_rest_api.manager import BinanceRestApiManager
import logging
import os


# How to:
# https://medium.com/@oliverzehentleitner/how-to-connect-to-binance-com-rest-api-using-python-via-a-socks5-proxy-638dbbecacfd
socks5_proxy = "1.2.3.4:1080"
socks5_user = None
socks5_pass = None
socks5_ssl_verification = True

if __name__ == "__main__":
    logging.getLogger("unicorn_binance_rest_api")
    logging.basicConfig(level=logging.INFO,
                        filename=os.path.basename(__file__) + '.log',
                        format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                        style="{")

    # To use this library you need a valid UNICORN Binance Suite License: https://medium.lucit.tech/87b0088124a8
    ubra = BinanceRestApiManager(exchange="binance.com",
                                 socks5_proxy_server=socks5_proxy,
                                 socks5_proxy_user=socks5_user,
                                 socks5_proxy_pass=socks5_pass,
                                 socks5_proxy_ssl_verification=socks5_ssl_verification)

    klines_1m = ubra.get_historical_klines("BTCUSDT", ubra.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    print(f"klines_1m:\r\n{klines_1m}")

    ubra.stop_manager()