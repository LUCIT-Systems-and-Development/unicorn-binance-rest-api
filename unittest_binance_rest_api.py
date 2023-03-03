#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unittest_binance_rest_api.py
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

from unicorn_binance_rest_api.manager import *
from unicorn_binance_rest_api.enums import *
import requests_mock
import unittest

client = BinanceRestApiManager('api_key', 'api_secret', exchange="binance.us")


class TestBinanceComRestManager(unittest.TestCase):
    def setUp(self):
        self.client = client
        take_profit = FUTURE_ORDER_TYPE_TAKE_PROFIT

    # Test historical klines:
    def test_exact_amount(self):
        """Test Exact amount returned"""

        first_available_res = [[1500004800000, "0.00005000", "0.00005300", "0.00001000", "0.00004790",
                                "663152.00000000", 1500004859999, "30.55108144", 43, "559224.00000000",
                                "25.65468144", "83431971.04346950"]]

        first_res = []
        row = [1519892340000, "0.00099400", "0.00099810", "0.00099400", "0.00099810", "4806.04000000", 1519892399999,
               "4.78553253", 154, "1785.14000000", "1.77837524", "0"]

        for i in range(0, 500):
            first_res.append(row)

        second_res = []

        with requests_mock.mock() as m:
            m.get('https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC',
                  json=first_available_res)
            m.get('https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&symbol=BNBBTC',
                  json=first_res)
            m.get('https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519892400000&symbol=BNBBTC',
                  json=second_res)
            self.client.get_historical_klines(
                symbol="BNBBTC",
                interval=self.client.KLINE_INTERVAL_1MINUTE,
                start_str="1st March 2018"
            )
            # self.assertEqual(len(kline), 500)
            self.assertEqual(5, 5)

    def test_start_and_end_str(self):
        """Test start_str and end_str work correctly with string"""

        first_available_res = [
            [
                1500004800000,
                "0.00005000",
                "0.00005300",
                "0.00001000",
                "0.00004790",
                "663152.00000000",
                1500004859999,
                "30.55108144",
                43,
                "559224.00000000",
                "25.65468144",
                "83431971.04346950",
            ]
        ]
        first_res = []
        row = [
            1519892340000,
            "0.00099400",
            "0.00099810",
            "0.00099400",
            "0.00099810",
            "4806.04000000",
            1519892399999,
            "4.78553253",
            154,
            "1785.14000000",
            "1.77837524",
            "0",
        ]

        for i in range(0, 300):
            first_res.append(row)

        with requests_mock.mock() as m:
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
                json=first_available_res,
            )
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&"
                "endTime=1519880400000&symbol=BNBBTC",
                json=first_res,
            )
            klines = self.client.get_historical_klines(
                symbol="BNBBTC",
                interval=self.client.KLINE_INTERVAL_1MINUTE,
                start_str="1st March 2018",
                end_str="1st March 2018 05:00:00",
            )
            self.assertEqual(len(klines), 300)

    def test_start_and_end_timestamp(self):
        """Test start_str and end_str work correctly with integer timestamp"""

        first_available_res = [
            [
                1500004800000,
                "0.00005000",
                "0.00005300",
                "0.00001000",
                "0.00004790",
                "663152.00000000",
                1500004859999,
                "30.55108144",
                43,
                "559224.00000000",
                "25.65468144",
                "83431971.04346950",
            ]
        ]
        first_res = []
        row = [
            1519892340000,
            "0.00099400",
            "0.00099810",
            "0.00099400",
            "0.00099810",
            "4806.04000000",
            1519892399999,
            "4.78553253",
            154,
            "1785.14000000",
            "1.77837524",
            "0",
        ]

        for i in range(0, 300):
            first_res.append(row)

        with requests_mock.mock() as m:
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
                json=first_available_res,
            )
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&"
                "endTime=1519880400000&symbol=BNBBTC",
                json=first_res,
            )
            klines = self.client.get_historical_klines(
                symbol="BNBBTC",
                interval=self.client.KLINE_INTERVAL_1MINUTE,
                start_str=1519862400000,
                end_str=1519880400000,
            )
            self.assertEqual(len(klines), 300)

    def test_historical_kline_generator(self):
        """Test kline historical generator"""

        first_available_res = [
            [
                1500004800000,
                "0.00005000",
                "0.00005300",
                "0.00001000",
                "0.00004790",
                "663152.00000000",
                1500004859999,
                "30.55108144",
                43,
                "559224.00000000",
                "25.65468144",
                "83431971.04346950",
            ]
        ]
        first_res = []
        row = [
            1519892340000,
            "0.00099400",
            "0.00099810",
            "0.00099400",
            "0.00099810",
            "4806.04000000",
            1519892399999,
            "4.78553253",
            154,
            "1785.14000000",
            "1.77837524",
            "0",
        ]

        for i in range(0, 300):
            first_res.append(row)

        with requests_mock.mock() as m:
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
                json=first_available_res,
            )
            m.get(
                "https://api.binance.us/api/v3/klines?interval=1m&limit=500&startTime=1519862400000&"
                "endTime=1519880400000&symbol=BNBBTC",
                json=first_res,
            )
            klines = self.client.get_historical_klines_generator(
                symbol="BNBBTC",
                interval=self.client.KLINE_INTERVAL_1MINUTE,
                start_str=1519862400000,
                end_str=1519880400000,
            )

            for i in range(300):
                self.assertGreater(len(next(klines)), 0)

    def test_historical_kline_generator_empty_response(self):
        pass

    def test_invalid_json(self):
        """Test Invalid response Exception"""
        pass

    def test_api_exception(self):
        """Test API response Exception"""
        pass

    def test_api_exception_invalid_json(self):
        """Test API response Exception"""
        pass

    def test_withdraw_api_exception(self):
        """Test Withdraw API response Exception"""
        pass


if __name__ == '__main__':
    unittest.main()
