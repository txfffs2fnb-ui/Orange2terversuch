#!/usr/bin/env python3
"""
Test-Skript fuer Telekom-Aktie (DTE.DE) mit SMA-Crossover-Strategie

Dieses Skript testet die vorhandene SmaCross-Strategie direkt mit der
Deutsche Telekom Aktie, ohne die Flask-App zu starten.

Usage:
    python test_telekom.py
"""

import sys
import datetime

from backtest_engine import run_backtest
from strategy_sample import SmaCross


def main():
    """Fuehrt einen Backtest mit der Telekom-Aktie durch"""
    print("=" * 60)
    print("Backtest: Deutsche Telekom AG (DTE.DE)")
    print("Strategie: SMA-Crossover (20/50 Tage)")
    print("=" * 60)
    print()

    # Parameter
    symbol = "DTE.DE"
    start = "2022-01-01"
    # end als String uebergeben (yfinance erwartet einen String, kein date-Objekt)
    end = datetime.date.today().strftime("%Y-%m-%d")
    initial_cash = 10000.0

    print(f"Symbol:       {symbol}")
    print(f"Zeitraum:     {start} bis {end}")
    print(f"Startkapital: EUR {initial_cash:,.2f}")
    print()
    print("Lade Daten und fuehre Backtest aus...")
    print()

    try:
        # Backtest ausfuehren
        # strategy_cls= wird in run_backtest als Alias fuer strategy= akzeptiert
        result = run_backtest(
            strategy_cls=SmaCross,
            symbol=symbol,
            start=start,
            end=end,
            cash=initial_cash,
        )

        # Ergebnisse anzeigen
        print("=" * 60)
        print("ERGEBNISSE")
        print("=" * 60)
        print(f"Startkapital:  EUR {result.start_value:>12,.2f}")
        print(f"Endkapital:    EUR {result.final_value:>12,.2f}")
        print()

        profit = result.final_value - result.start_value
        profit_pct = (profit / result.start_value) * 100

        if profit > 0:
            print(f"[OK] Gewinn:   EUR {profit:>12,.2f}  ({profit_pct:+.2f}%)")
        elif profit < 0:
            print(f"[!!] Verlust:  EUR {profit:>12,.2f}  ({profit_pct:+.2f}%)")
        else:
            print("Keine Aenderung")

        print()
        print(f"Anzahl Trades: {len(result.trades)}")
        print("=" * 60)

    except Exception as e:
        print(f"\nFEHLER: {e}")
        print("\nMoegliche Ursachen:")
        print("- Keine Internetverbindung")
        print("- Yahoo Finance API nicht erreichbar")
        print("- Ungueltiges Symbol oder Datumsbereich")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
