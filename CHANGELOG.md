# unicorn-binance-rest-api Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to 
[Semantic Versioning](http://semver.org/).

[Discussions about unicorn-binance-rest-api releases!](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/discussions/categories/releases)

[How to upgrade to the latest version!](https://unicorn-binance-rest-api.docs.lucit.tech/README.html#installation-and-upgrade)

## 1.6.0.dev (development stage/unreleased/unstable)
### Added
- SOCKS5 proxy support to [`BinanceRestApiManager()`](https://unicorn-binance-rest-api.docs.lucit.tech/unicorn_binance_rest_api.html#unicorn_binance_rest_api.manager.BinanceRestApiManager) - 
  New parameter: socks5_proxy_server, socks5_proxy_user, socks5_proxy_pass, socks5_proxy_ssl_verification

## 1.6.0
### Added
- New kline interval: 1s `KLINE_INTERVAL_1SECOND`
- `futures_place_batch_order()` - Placing batch orders for USD-M API. Thx [@hawkeye-bot](https://github.com/hawkeye-bot) 
[PR#42](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/pull/42)
### Changed
- Dependency regex no specific version anymore

## 1.5.0
### Added 
- `cancel_all_open_margin_orders()`
- `futures_auto_cancel_all_open_orders()`

## 1.4.3
Codebase equal to 1.4.2, testing azure pipe

## 1.4.2
### Changed 
- Dependency regex to <= 2022.3.2 [issue#24](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues/24)

## 1.4.1
### Fixed
- Binance Futures Testnet URL [issue#20](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues/20)

## 1.4.0
### Adding
- `futures_commission_rate()` [issue#18](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues/18)
### Changed
- Moved from https://github.com/oliver-zehentleitner to https://github.com/LUCIT-Systems-and-Development/
- removed "unicorn_binance_rest_api_"-part of the module file names (more info: [Discussions](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/discussions/19))
- Correctly scope loggers so that it plays nicely with others. [PR#17](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/pull/17)
- renamed logger name of all modules to "unicorn_binance_rest_api", in the implementation of 
[PR#17](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/pull/17) every module has had 
its own logger name.

## 1.3.0
### Added
- `exchange` parameter to manager class to replace `tld` parameter
- support for new endpoints: trbinance.com 
- `disable_colorama` parameter to manager class
- `cancel_all_open_orders()` to cancel all orders of a symbol with one request. Thx @mfurlend 
[issue#3](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues/3)
### Changed
- `tld` is now obsolete
### Fixed
- ValueError in `get_used_weight()`
- get_open_margin_orders()
### Removed
- double definition of `make_universal_transfer()`
- binance.je support (Binance Jersey has ceased operations.)

## 1.2.0
### Added
- get_used_weight()
- futures_coin_place_batch_order() 
### Changed
- Migrate from WAPI to SAPI [issue#7](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/issues/7)
- URLs to Biannce Docs

## 1.1.1
### Fixed
- changed FUTURES_COIN_URL [PR#5](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-rest-api/pull/5) - 
Thanks to [flo-rian](https://github.com/flo-rian)

## 1.1.0
### Added
- logging
- update check

## 1.0.0
forked from Sam McHardy [python-binance v0.7.10](https://github.com/sammchardy/python-binance)
### Added
- get_latest_release_info()
- get_latest_version()
- is_update_availabe()
- get_version()
- get_user_agent()
- colorama as requirement
### Removed
- Websocket support from python-binance and dependencies
