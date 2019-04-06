select strftime('%Y-%m-%d %H:%M:%S', datetime(start, 'unixepoch')) as start, open, high, low, close, volume, trades
from candles_USDT_BTC
order by start asc