# Orange Trading Bot mit Backtesting

Ein webbasierter Trading-Bot mit Backtesting-Funktionen, entwickelt mit Flask und Backtrader.

## Features

- 📊 **Backtesting-Engine**: Teste deine Trading-Strategien mit historischen Daten
- 🔐 **Multi-User-System**: Login und Registrierung für mehrere Benutzer
- 📈 **Yahoo Finance Integration**: Automatischer Download von Kursdaten
- 🎯 **Beispiel-Strategie**: SMA-Crossover-Strategie als Vorlage
- 🌐 **Web-Interface**: Einfache Bedienung über den Browser

## Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

### Schritte

1. Repository klonen:
```bash
git clone https://github.com/txfffs2fnb-ui/Orange2terversuch.git
cd Orange2terversuch
```

2. Virtuelle Umgebung erstellen:
```bash
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Anwendung starten:
```bash
python app.py
```

5. Browser öffnen und zu `http://localhost:5000` navigieren

## Projektstruktur

```
orange-trading-bot/
├── app.py                  # Flask Web-Anwendung
├── backtest_engine.py      # Backtesting-Logik
├── strategy_sample.py      # Beispiel-Strategien
├── config.py               # Konfiguration
├── requirements.txt        # Python-Abhängigkeiten
├── templates/              # HTML-Templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── backtest.html
└── static/                 # CSS und statische Dateien
    └── style.css
```

## Nutzung

1. **Registrieren**: Erstelle einen neuen Account
2. **Einloggen**: Melde dich mit deinen Zugangsdaten an
3. **Backtest starten**: 
   - Symbol eingeben (z.B. AAPL, MSFT, BTC-USD)
   - Zeitraum festlegen (Start- und Enddatum)
   - Startkapital angeben
   - Backtest ausführen
4. **Ergebnisse ansehen**: Sieh dir die Performance deiner Strategie an

## Eigene Strategien entwickeln

Du kannst eigene Strategien in `strategy_sample.py` hinzufügen. Beispiel:

```python
import backtrader as bt

class MeineStrategie(bt.Strategy):
    params = dict(
        period=20
    )
    
    def __init__(self):
        self.sma = bt.ind.SMA(self.data.close, period=self.p.period)
    
    def next(self):
        if not self.position:
            if self.data.close[0] > self.sma[0]:
                self.buy()
        else:
            if self.data.close[0] < self.sma[0]:
                self.sell()
```

## Deployment

### Auf Render.com deployen:

1. `render.yaml` erstellen
2. Repository mit Render verbinden
3. Environment Variables setzen:
   - `SECRET_KEY`: Sicherer Schlüssel für Sessions
4. Deployment starten

### Auf Railway deployen:

1. Repository mit Railway verbinden
2. `Procfile` erstellen: `web: gunicorn app:app`
3. Deployment starten

## Technologie-Stack

- **Backend**: Flask (Python)
- **Backtesting**: Backtrader
- **Datenquelle**: yfinance (Yahoo Finance)
- **Datenbank**: SQLite
- **Frontend**: HTML, CSS
- **Auth**: Flask-Login

## Sicherheitshinweise

- Ändere den `SECRET_KEY` in `config.py` vor dem Deployment
- Nutze HTTPS im Production-Modus
- Verwende eine sichere Datenbank (PostgreSQL) für Production
- Aktiviere CSRF-Protection für Forms

## Lizenz

MIT License

## Kontakt

Bei Fragen oder Problemen öffne ein Issue auf GitHub.

---

**Hinweis**: Dies ist ein Bildungsprojekt. Trading birgt erhebliche Risiken. Nutze dieses Tool nicht mit echtem Geld ohne gründliche Tests und Risikoabwägung.
