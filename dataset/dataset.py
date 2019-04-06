import backtrader as bt


class CustomDataset(bt.feeds.GenericCSVData):
    params = (
        ('time', -1),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', 6),
    )
