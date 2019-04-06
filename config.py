import os

PRODUCTION = "production"
DEVELOPMENT = "development"

COIN_TARGET = "BTC"
COIN_REFER = "USDT"

ENV = os.getenv("ENVIRONMENT", DEVELOPMENT)
DEBUG = True

BINANCE = {
  "key": "<YOUR KEY HERE>",
  "secret": "<YOUR SECRET HERE>"
}

TELEGRAM = {
  "channel": "<CHANEL ID>",
  "bot": "<BOT KEY HERE>"
}

print("ENV = ", ENV)