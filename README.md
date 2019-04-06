# Backtrader Binance Bot
A example of bot using Backtrader to trade Bitcoins in Binance Exchange.


### Installation

Activating [Virtualenv](https://virtualenv.pypa.io/en/latest/)
```
make init
source venv/bin/activate
```

Installing dependencies
```
make install
```

Start application
```
./main.py
```

## Results

![alt text](screenshot.png "Backtrader Simulation")


```
Starting Portfolio Value: 100000.00
Final Portfolio Value: 110135.28

Profit 10.135%
Trade Analysis Results:
               Total Open     Total Closed   Total Won      Total Lost     
               0              20             12             8              
               Strike Rate    Win Streak     Losing Streak  PnL Net        
               1              3              2              10135.28       
SQN: 0.64

```