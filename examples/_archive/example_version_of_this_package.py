#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: example_version_of_this_package.py
#
# Part of ‘UNICORN Binance REST API’
# Project website: https://www.lucit.tech/unicorn-binance-rest-api.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api
# Documentation: https://unicorn-binance-rest-api.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-rest-api
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2024, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

from unicorn_binance_rest_api import BinanceRestApiManager

with BinanceRestApiManager(warn_on_update=False) as ubra:
    if ubra.is_update_available():
        print(f"Please upgrade to {ubra.get_latest_version()} you are on {ubra.get_version()}")
        latest_release_info = ubra.get_latest_release_info()
        if latest_release_info:
            print(f"Please download the latest release or run `pip install unicorn-binance-rest-api --upgrade`"
                  f":\r\n\ttar: {latest_release_info['tarball_url']}\r\n\tzip: {latest_release_info['zipball_url']}\r\n"
                  f"release info:\r\n{latest_release_info['body']}")
    else:
        print(ubra.get_version(), "is the latest version!")

