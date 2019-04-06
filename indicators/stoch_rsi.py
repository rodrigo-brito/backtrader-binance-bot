#!/usr/bin/env python3

import backtrader as bt


class StochRSI(bt.Indicator):
    lines = ('fastk', 'fastd',)

    params = (
        ('k_period', 3),
        ('d_period', 3),
        ('period', 14),
        ('stoch_period', 14),
        ('upperband', 80.0),
        ('lowerband', 20.0),
    )

    def __init__(self, base_indicator):
        rsi_ll = bt.ind.Lowest(base_indicator, period=self.p.period)
        rsi_hh = bt.ind.Highest(base_indicator, period=self.p.period)
        stochrsi = (base_indicator - rsi_ll) / ((rsi_hh - rsi_ll) + 0.00001)

        self.l.fastk = k = bt.indicators.MovingAverageSimple(100.0 * stochrsi, period=self.p.k_period)
        self.l.fastd = bt.indicators.MovingAverageSimple(k, period=self.p.d_period)
