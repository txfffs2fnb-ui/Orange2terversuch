import backtrader as bt

class SmaCross(bt.Strategy):
    """Simple Moving Average Crossover Strategy"""
    params = dict(
        fast=10,
        slow=30
    )

    def __init__(self):
        sma_fast = bt.ind.SMA(self.data.close, period=self.p.fast)
        sma_slow = bt.ind.SMA(self.data.close, period=self.p.slow)
        self.crossover = bt.ind.CrossOver(sma_fast, sma_slow)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        else:
            if self.crossover < 0:
                self.sell()
