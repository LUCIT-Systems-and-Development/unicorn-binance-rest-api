[![GitHub release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-binance-rest-api.svg)](https://pypi.org/project/unicorn-binance-rest-api/)
[![GitHub](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-binance-rest-api.svg?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn-binance-rest-api.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/unicorn-binance-rest-api)](https://pepy.tech/project/unicorn-binance-rest-api)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn-binance-rest-api.svg?label=PyPI%20wheel)](https://pypi.org/project/unicorn-binance-rest-api/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn-binance-rest-api.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues)
[![Python application](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/actions/workflows/python-app.yml)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/oliver-zehentleitner/unicorn-binance-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/unicorn-binance-rest-api/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/oliver-zehentleitner/unicorn-binance-rest-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/unicorn-binance-rest-api/context:python)
[![codecov](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-rest-api/branch/master/graph/badge.svg?token=P7XILPPSLU)](https://codecov.io/gh/oliver-zehentleitner/unicorn-binance-rest-api)
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
This is a fork of Sam McHardy`s [python-binance](https://github.com/sammchardy/python-binance) - package. 
Extended, cleaned up and reduced to pure REST tasks, with PRs added and improved.

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

# get the used weight: https://github.com/binance-us/binance-official-api-docs/blob/master/rest-api.md#limits
print(f"Used weight: {ubra.get_used_weight()}")
```

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
| [Binance Jersey](https://www.binance.je) | `BinanceRestApiManager(exchange="binance.je")` |
| [Binance US](https://www.binance.us) | `BinanceRestApiManager(exchange="binance.us")` |
| [Binance TR](https://www.trbinance.com) | `BinanceRestApiManager(exchange="trbinance.com")` |
| [Binance JEX](https://www.jex.com) | `BinanceRestApiManager(exchange="jex.com")` |


- Helpful management features like 
[`get_used_weight()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html#unicorn_binance_rest_api.unicorn_binance_rest_api_manager.BinanceRestApiManager.get_used_weight), 
[`get_blah()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html#unicorn_binance_rest_api.unicorn_binance_rest_api_manager.BinanceRestApiManager.get_blah), 

- Auto-selecting fastest endpoints 

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
- [example_doing_something.py](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/example_doing_something.py)
- [example_easy_migration_from_python-binance.py](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/example_easy_migration_from_python-binance.py)
- [example_orders.py](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/example_orders.py)
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
[`is_update_availabe()`](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api/unicorn_binance_rest_api.html?highlight=is_update_availabe#unicorn_binance_rest_api.unicorn_binance_rest_api_manager.BinanceRestApiManager.is_update_availabe).

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

## Donate
Developing, documenting and testing the 
[UNICORN Binance Suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite) and supporting the community 
takes a lot of time and time is a form of cost. I am extremely happy to do this, but need a solution for sharing the 
costs.

I think we are lucky, as our community consists of traders and programmers I expect to find mostly rational thinking 
people who also benefit financially from these libraries.

I would like to create a fair model for funding. My goals are that unicorn-binance-websocket-api, 
unicorn-binance-rest-api and unicorn-fy remain freely available as open source and that I am compensated at least to 
some extent and thus can invest my time more easily.

If you know the hooker principle from negotiation research or game theory, you know about the problem that people don't 
often pay for something out of their own impulse if they have already received it for free. 

So my idea is to give every donor who gives an amount over 50 EUR access to a private Github repository where Python 
classes for trading algos are provided (OrderBook, advanced stop-loss, ...). Moreover, maybe a nice ApiTrader community 
will be formed.

So the donor not only helps to push the open source development but also gets access to a well maintained collection of 
practical code for little money. 

Furthermore community members can help me by donating own developments to make the 
[unicorn-coding-club](https://github.com/oliver-zehentleitner/unicorn-coding-club) repository more attractive to create 
further incentives for new donors. This way we generate added value for all sides in an uncomplicated way.

If you donated at least 50 EUR (without transaction fee), please send me a message with a confirmation and your Github 
username via https://www.lucit-development.co/contact.html, I will invite you to the 
[unicorn-coding-club](https://github.com/oliver-zehentleitner/unicorn-coding-club) as soon as possible.

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/oliver-zehentleitner/donate)

[:heart: Sponsor (GitHub)](https://github.com/sponsors/oliver-zehentleitner/)
```
Terra (LUNA, UST, ...): terra1yt34qmmycextztnj9mpt3mnjzqqvl8jtqqq7g9
BTC: 39fS74fvcGnmEk8JUV8bG6P1wkdH29GtsA
DASH: XsRhBuPkXGF9WvifdpkVhTGSmVT4VcuQZ7
ETH: 0x1C15857Bf1E18D122dDd1E536705748aa529fc9C
LTC: LYNzHMFUbee3siyHvNCPaCjqXxjyq8YRGJ
XMR: 85dzsTRh6GRPGVSJoUbFDwAf9uwwAdim1HFpiGshLeKHgj2hVqKtYVPXMZvudioLsuLS1AegkUiQ12jwReRwWcFvF7kDAbF
ZEC: t1WvQMPJMriGWD9qkZGDdE9tTJaawvmsBie
```
