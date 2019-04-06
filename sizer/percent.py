from backtrader.sizers import PercentSizer


class FullMoney(PercentSizer):
    params = (
        ('percents', 99),
    )
