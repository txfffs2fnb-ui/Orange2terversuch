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


def run_backtest(symbol="AAPL", start="2020-01-01", end="2021-01-01", strategy=None, cash=10000):
    """Run a backtest with the given strategy"""
    if strategy is None:
        raise ValueError("Eine Strategie muss angegeben werden.")

    # Download data
    data = download_data(symbol, start, end)

    if data.empty:
        raise ValueError(f"Keine Daten fuer {symbol} im Zeitraum {start} bis {end} gefunden.")

    # Convert to Backtrader format
    data_bt = bt.feeds.PandasData(dataname=data)

    # Initialize Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.adddata(data_bt)
    cerebro.addstrategy(strategy)
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

    trades = []  # Kann erweitert werden fuer echte Trade-Daten

    return BacktestResult(
        final_value=final_value,
        start_value=start_value,
        trades=trades,
        equity_curve=equity_curve,
    )
