import datetime
import backtrader as bt
import yfinance as yf
import pandas as pd

class BacktestResult:
    def __init__(self, final_value, start_value, trades, equity_curve):
        self.final_value = final_value
        self.start_value = start_value
        self.trades = trades
        self.equity_curve = equity_curve

def download_data(symbol, start, end):
    """Download historical data from Yahoo Finance"""
    data = yf.download(symbol, start=start, end=end)
    data.dropna(inplace=True)
    return data

def run_backtest(strategy_cls, symbol="AAPL", start="2020-01-01", end="2021-01-01", cash=10000):
    """Run a backtest with the given strategy"""
    # Download data
    data = download_data(symbol, start, end)
    
    # Convert to Backtrader format
    data_bt = bt.feeds.PandasData(dataname=data)
    
    # Initialize Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.adddata(data_bt)
    cerebro.addstrategy(strategy_cls)
    cerebro.broker.setcash(cash)
    
    # Run backtest
    start_value = cerebro.broker.getvalue()
    cerebro.run()
    final_value = cerebro.broker.getvalue()
    
    # Create equity curve
    equity_curve = [
        {"date": start, "equity": start_value},
        {"date": end, "equity": final_value},
    ]
    
    trades = []  # Could be enhanced to collect actual trade data
    
    return BacktestResult(
        final_value=final_value,
        start_value=start_value,
        trades=trades,
        equity_curve=equity_curve,
    )
