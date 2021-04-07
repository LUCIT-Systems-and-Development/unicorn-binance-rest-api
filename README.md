[![GitHub release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-binance-rest-api.svg)](https://pypi.org/project/unicorn-binance-rest-api/)
[![GitHub](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-binance-rest-api.svg?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn-binance-rest-api.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/unicorn-binance-rest-api)](https://pepy.tech/project/unicorn-binance-rest-api)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn-binance-rest-api.svg?label=PyPI%20wheel)](https://pypi.org/project/unicorn-binance-rest-api/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn-binance-rest-api.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues)
[![Build Status](https://travis-ci.com/oliver-zehentleitner/unicorn-binance-rest-api.svg?branch=master)](https://travis-ci.com/oliver-zehentleitner/unicorn-binance-rest-api)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/oliver-zehentleitner/unicorn-binance-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/unicorn-binance-rest-api/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/oliver-zehentleitner/unicorn-binance-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/unicorn-binance-rest-api/context:python)
[![Coverage Status](https://coveralls.io/repos/github/oliver-zehentleitner/unicorn-binance-rest-api/badge.svg?branch=master)](https://coveralls.io/github/oliver-zehentleitner/unicorn-binance-rest-api?branch=master)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow.svg)](https://t.me/unicorndevs)
[![Donations/week](http://img.shields.io/liberapay/receives/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)
[![Patrons](http://img.shields.io/liberapay/patrons/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)

# UNICORN Binance REST API

[Description](#description) | [Installation](#installation-and-upgrade) | [How To](#howto) |
[Documentation](#documentation) | [Examples](#examples) | [Change Log](#change-log) | [Wiki](#wiki) | [Social](#social) |
[Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Commercial Support](#commercial-support) | [Donate](#donate)

An unofficial Python API to use the Binance REST API`s in a easy, fast, flexible, robust and 
fully-featured way. 

Part of ['UNICORN Binance Suite'](https://github.com/oliver-zehentleitner/unicorn-binance-suite).

## Description
This is a fork of Sam McHardy`s [python-binance v0.7.10](https://github.com/sammchardy/python-binance) - package. 
cleaned up and reduced to pure REST tasks, with PRs added and improved, but still 100% compatible with 
[python-binance v0.7.10](https://github.com/sammchardy/python-binance).

```
from unicorn_binance_rest_api.unicorn_binance_rest_api_manager import BinanceRestApiManager

api_key = "aaa"
api_secret = "bbb"
ubra = BinanceRestApiManager(api_key, api_secret)

# get market depth
depth = ubra.get_order_book(symbol='BNBBTC')
print(f"{depth}")

# get all symbol prices
prices = ubra.get_all_tickers()
print(f"{prices}")
```

## Installation and Upgrade
The current dependencies are listed 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki/Installation).

### A wheel of the latest release with PIP from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
`pip install unicorn-binance-rest-api --upgrade`
### From source of the latest release with PIP from [Github](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`
#### Windows
Use the below command with the version (such as 1.0.0) you determined 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/archive/1.0.0.tar.gz --upgrade`
### From the latest source (dev-stage) with PIP from [Github](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://docs.python.org/2/install/)
Download the [latest release](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest) 
or the [current master branch](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/archive/master.zip)
 and use:
- ./environment.yml
- ./requirements.txt
- ./setup.py

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/CHANGELOG.html](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/CHANGELOG.html)

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api)
- [Modules](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html)

## Examples
- [example_client.py](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/example_client.py)
- [example_version_of_this_package.py](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/example_version_of_this_package.py)

## Howto

## Project Homepage
[https://github.com/oliver-zehentleitner/unicorn-binance-rest-api](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki)

## Social
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [Twitter](https://twitter.com/DevsUnicorn)
- [unicorn-coding-club](https://github.com/oliver-zehentleitner/unicorn-coding-club)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/watch.png)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/watchers) 
the repository on [GitHub](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api), write your 
[own script](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/example_version_of_this_package.py) 
with using 
[`is_update_availabe()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_websocket_api.html#unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager.BinanceWebSocketApiManager.is_update_availabe) 
or you use the 
[monitoring API service](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/wiki/UNICORN-Monitoring-API-Service).

To receive news (like inspection windows/maintenance) about the Binance API`s subscribe to their telegram groups: 
- [https://t.me/binance_api_announcements](https://t.me/binance_api_announcements)
- [https://t.me/binance_api_english](https://t.me/binance_api_english)
- [https://t.me/BinanceExchange](https://t.me/BinanceExchange)
- [https://t.me/Binance_Jersey](https://t.me/Binance_Jersey)
- [https://t.me/Binance_USA](https://t.me/Binance_USA)
- [https://t.me/Binance_JEX_EN](https://t.me/Binance_JEX_EN)
- [https://t.me/BinanceDEXchange](https://t.me/BinanceDEXchange)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you dont find an issue related to your topic, please open a new [issue](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues)!

[Report a security bug!](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/security/policy)

## Contributing
[UNICORN Binance REST API](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-binance-rest-api)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/heart.png) open source!

## Commercial Support
Need a Python developer or consulting? 

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding and free consultation via my company 
[LUCIT](https://www.lucit.dev) from Vienna (Austria) or via [Telegram](https://t.me/LUCIT_OZ).

### Donate
Since you are probably a developer yourself, you will understand very well that the creation of open source software is 
not free - it requires technical knowledge, a lot of time and also financial expenditure.

If you would like to help me to dedicate my time and energy to this project, even small donations are very welcome.

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/oliver-zehentleitner/donate)

```
Terra (LUNA, UST, ...): terra1yt34qmmycextztnj9mpt3mnjzqqvl8jtqqq7g9
BTC: 39fS74fvcGnmEk8JUV8bG6P1wkdH29GtsA
DASH: XsRhBuPkXGF9WvifdpkVhTGSmVT4VcuQZ7
ETH: 0x1C15857Bf1E18D122dDd1E536705748aa529fc9C
LTC: LYNzHMFUbee3siyHvNCPaCjqXxjyq8YRGJ
XMR: 85dzsTRh6GRPGVSJoUbFDwAf9uwwAdim1HFpiGshLeKHgj2hVqKtYVPXMZvudioLsuLS1AegkUiQ12jwReRwWcFvF7kDAbF
ZEC: t1WvQMPJMriGWD9qkZGDdE9tTJaawvmsBie
```
