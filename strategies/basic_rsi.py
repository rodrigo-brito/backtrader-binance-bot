#!/usr/bin/env python3

import backtrader as bt

from config import ENV, PRODUCTION
from indicators.macd_hist import MACDHistSMA
from indicators.stoch_rsi import StochRSI
from strategies.base import StrategyBase


class BasicRSI(StrategyBase):
    def __init__(self):
        StrategyBase.__init__(self)
        self.log("Using StochRSI strategy")

        self.sma_fast = bt.indicators.MovingAverageSimple(self.data0.close, period=20)
        self.sma_slow = bt.indicators.MovingAverageSimple(self.data0.close, period=200)
        self.rsi = bt.indicators.RelativeStrengthIndex()

        self.profit = 0

    def update_indicators(self):
        self.profit = 0
        if self.buy_price_close and self.buy_price_close > 0:
            self.profit = float(self.data0.close[0] - self.buy_price_close) / self.buy_price_close

    def next(self):
        self.update_indicators()

        if self.status != "LIVE" and ENV == PRODUCTION:
            self.log("%s - $%.2f" % (self.status, self.data0.close[0]))
            return

        if self.order:
            return

        # stop Loss
        if self.profit < -0.03:
            self.log("STOP LOSS: percentage %.3f %%" % self.profit)
            self.short()

        if self.last_operation != "BUY":
            if self.rsi < 30 and self.sma_fast > self.sma_slow:
                self.long()

        if self.last_operation != "SELL":
            if self.rsi > 70:
                self.short()

