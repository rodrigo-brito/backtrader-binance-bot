#!/usr/bin/env python3

import backtrader as bt

from config import ENV, PRODUCTION
from strategies.base import StrategyBase


class BasicRSI(StrategyBase):
    params = dict(
        period_ema_fast=10,
        period_ema_slow=100
    )

    def __init__(self):
        StrategyBase.__init__(self)
        self.log("Using RSI/EMA strategy")

        self.ema_fast = bt.indicators.EMA(period=self.p.period_ema_fast)
        self.ema_slow = bt.indicators.EMA(period=self.p.period_ema_slow)
        self.rsi = bt.indicators.RelativeStrengthIndex()

        self.profit = 0

    def update_indicators(self):
        self.profit = 0
        if self.buy_price_close and self.buy_price_close > 0:
            self.profit = float(self.data0.close[0] - self.buy_price_close) / self.buy_price_close

    def next(self):
        self.update_indicators()

        if self.status != "LIVE" and ENV == PRODUCTION:  # waiting for live status in production
            return

        if self.order:  # waiting for pending order
            return

        # stop Loss
        if self.profit < -0.03:
            self.log("STOP LOSS: percentage %.3f %%" % self.profit)
            self.short()

        if self.last_operation != "BUY":
            if self.rsi < 30 and self.ema_fast > self.ema_slow:
                self.long()

        if self.last_operation != "SELL":
            if self.rsi > 70:
                self.short()

