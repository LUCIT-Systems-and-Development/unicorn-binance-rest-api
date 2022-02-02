[![GitHub release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-binance-rest-api.svg)](https://pypi.org/project/unicorn-binance-rest-api/)
[![GitHub](https://img.shields.io/github/license/LUCIT-Systems-and-Development/unicorn-binance-rest-api.svg?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn-binance-rest-api.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/unicorn-binance-rest-api)](https://pepy.tech/project/unicorn-binance-rest-api)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn-binance-rest-api.svg?label=PyPI%20wheel)](https://pypi.org/project/unicorn-binance-rest-api/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn-binance-rest-api.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues)
[![Python application](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/actions/workflows/python-app.yml)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/LUCIT-Systems-and-Development/unicorn-binance-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LUCIT-Systems-and-Development/unicorn-binance-rest-api/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/LUCIT-Systems-and-Development/unicorn-binance-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LUCIT-Systems-and-Development/unicorn-binance-rest-api/context:python)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-binance-rest-api/branch/master/graph/badge.svg?token=P7XILPPSLU)](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-rest-api)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-binance-rest-api.docs.lucit.tech/)
[![Github](https://img.shields.io/badge/source-github-yellow)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow)](https://t.me/unicorndevs)

# UNICORN Binance REST API

[Description](#description) | [Installation](#installation-and-upgrade) | [How To](#howto) |
[Documentation](#documentation) | [Examples](#examples) | [Change Log](#change-log) | [Wiki](#wiki) | [Social](#social) |
[Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Commercial Support](#commercial-support)

An unofficial Python API to use the Binance REST API`s (com+testnet, com-margin+testnet, com-isolated_margin+testnet, 
com-futures+testnet, us, tr) in a easy, fast, flexible, robust and fully-featured way. 

Part of ['UNICORN Binance Suite'](https://www.lucit.tech/unicorn-binance-suite.html).

```
import unicorn_binance_rest_api

api_key = "aaa"
api_secret = "bbb"
ubra = unicorn_binance_rest_api.BinanceRestApiManager(api_key, api_secret, exchange="binance.com")

# get market depth
depth = ubra.get_order_book(symbol='BNBBTC')
print(f"{depth}")

# get all symbol prices
prices = ubra.get_all_tickers()
print(f"{prices}")

# get the used weight: 
# https://github.com/binance-us/binance-official-api-docs/blob/master/rest-api.md#limits
print(f"Used weight: {ubra.get_used_weight()}")
```

### Get the right [logger](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_logging.py):
```
logging.getLogger("unicorn_binance_rest_api")
```

## Description
This is a fork of Sam McHardy`s [python-binance 0.7.10](https://github.com/sammchardy/python-binance) - package. 
Extended, cleaned up and reduced to pure REST tasks, with PRs added and improved. No asyncio support!!

The Python module [UNICORN Binance REST API](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api) 
provides an API to the Binance REST API`s of 
[Binance](https://github.com/binance-exchange/binance-official-api-docs) 
([+Testnet](https://testnet.binance.vision/)), 
[Binance Margin](https://binance-docs.github.io/apidocs/spot/en/#user-data-streams) 
([+Testnet](https://testnet.binance.vision/)), 
[Binance Isolated Margin](https://binance-docs.github.io/apidocs/spot/en/#listen-key-isolated-margin)
([+Testnet](https://testnet.binance.vision/)), 
[Binance Futures](https://binance-docs.github.io/apidocs/futures/en/#websocket-market-streams) 
([+Testnet](https://testnet.binancefuture.com)), 
[Binance COIN-M Futures](https://binance-docs.github.io/apidocs/delivery/en/#change-log),
[Binance US](https://github.com/binance-us/binance-official-api-docs), 
[Binance TR](https://www.trbinance.com/apidocs) and 
[Binance JEX](https://jexapi.github.io/api-doc/spot.html#web-socket-streams) and needs to be used with a valid api_key and api_secret from the Binance Exchange 
[www.binance.com](https://www.binance.com/userCenter/createApi.html), 
[testnet.binance.vision](https://testnet.binance.vision/), 
[www.binance.us](https://www.binance.us/userCenter/createApi.html) or 
[www.jex.com](https://www.jex.com/userCenter/createApi.html).

Be aware that the Binance REST API is request based. if you want to receive high frequency and high volume data, you can use the [UNICORN Binance Websocket API](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api) in combination. 

### What are the benefits of the UNICORN Binance REST API?
- Supported exchanges: 

| Exchange | Exchange string | 
| -------- | --------------- | 
| [Binance](https://www.binance.com) | `BinanceRestApiManager(exchange="binance.com")` |
| [Binance Testnet](https://testnet.binance.vision/) | `BinanceRestApiManager(exchange="binance.com-testnet")` |
| [Binance Margin](https://www.binance.com) |  `BinanceRestApiManager(exchange="binance.com-margin")` |
| [Binance Margin Testnet](https://testnet.binance.vision/) | `BinanceRestApiManager(exchange="binance.com-margin-testnet")` |
| [Binance Isolated Margin](https://www.binance.com) | `BinanceRestApiManager(exchange="binance.com-isolated_margin")` |
| [Binance Isolated Margin Testnet](https://testnet.binance.vision/) | `BinanceRestApiManager(exchange="binance.com-isolated_margin-testnet")` |
| [Binance USD-M Futures](https://www.binance.com) | `BinanceRestApiManager(exchange="binance.com-futures")` |
| [Binance USD-M Futures Testnet](https://testnet.binancefuture.com) | `BinanceRestApiManager(exchange="binance.com-futures-testnet")` |
| [Binance Coin-M Futures](https://www.binance.com) | `BinanceRestApiManager(exchange="binance.com-coin-futures")` |
| [Binance US](https://www.binance.us) | `BinanceRestApiManager(exchange="binance.us")` |
| [Binance TR](https://www.trbinance.com) | `BinanceRestApiManager(exchange="trbinance.com")` |

- Helpful management features like 
[`get_used_weight()`](https://unicorn-binance-rest-api.docs.lucit.tech/unicorn_binance_rest_api.html#unicorn_binance_rest_api.manager.BinanceRestApiManager.get_used_weight), 

## Installation and Upgrade
The current dependencies are listed 
[here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/wiki/Installation).

### A wheel of the latest release with PIP from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
`pip install unicorn-binance-rest-api --upgrade`
### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-rest-api/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`
#### Windows
Use the below command with the version (such as 1.3.0) you determined 
[here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/releases/latest):

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/archive/1.3.0.tar.gz --upgrade`
### From the latest source (dev-stage) with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://docs.python.org/2/install/)
Download the [latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/releases/latest) 
or the [current master branch](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/archive/master.zip)
 and use:
- ./environment.yml
- ./requirements.txt
- ./setup.py

## Change Log
[https://unicorn-binance-rest-api.docs.lucit.tech/CHANGELOG.html](https://unicorn-binance-rest-api.docs.lucit.tech/CHANGELOG.html)

## Documentation
- [General](https://unicorn-binance-rest-api.docs.lucit.tech/)
- [Modules](https://unicorn-binance-rest-api.docs.lucit.tech/unicorn_binance_rest_api.html)

## Examples
- [example_doing_something.py](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_doing_something.py)
- [example_easy_migration_from_python-binance.py](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_easy_migration_from_python-binance.py)
- [example_logging.py](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_logging.py)
- [example_orders.py](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_orders.py)
- [example_version_of_this_package.py](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_version_of_this_package.py)

## Howto
- [Howto: UNICORN Binance REST API](https://www.technopathy.club/2021/09/21/howto-unicorn-binance-rest-api/)

## Project Homepage
[https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api)

## Wiki
[https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/wiki](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/wiki)

## Social
- [Discussions](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-rest-api/master/images/misc/watch.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/watchers) 
the repository on [GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api), write your 
[own script](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/example_version_of_this_package.py) 
with using 
[`is_update_availabe()`](https://unicorn-binance-rest-api.docs.lucit.tech/unicorn_binance_rest_api.html?highlight=is_update_availabe#unicorn_binance_rest_api.manager.BinanceRestApiManager.is_update_availabe).

Follow us on [Twitter](https://twitter.com/LUCIT_SysDev) or on [Facebook](https://www.facebook.com/lucit.systems.and.development) for general news about the [unicorn-binance-suite](https://www.lucit.tech/unicorn-binance-suite.html)!

To receive news (like inspection windows/maintenance) about the Binance API`s subscribe to their telegram groups: 
- [https://t.me/binance_api_announcements](https://t.me/binance_api_announcements)
- [https://t.me/binance_api_english](https://t.me/binance_api_english)
- [https://t.me/BinanceExchange](https://t.me/BinanceExchange)
- [https://t.me/Binance_USA](https://t.me/Binance_USA)
- [https://t.me/BinanceDEXchange](https://t.me/BinanceDEXchange)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-rest-api/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you dont find an issue related to your topic, please open a new [issue](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues)!

[Report a security bug!](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/security/policy)

## Contributing
[UNICORN Binance REST API](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-binance-rest-api)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/graphs/contributors)

We ![love](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-rest-api/master/images/misc/heart.png) open source!

## Commercial Support
[![LUCIT](https://www.lucit.tech/files/images/logos/LUCIT-LOGO.png)](https://www.lucit.tech)

***Do you need a developer, operator or consultant?***

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding initial consultation via my company 
[LUCIT](https://www.lucit.tech) from Vienna (Austria) or via [Telegram](https://t.me/LUCIT_OZ).
