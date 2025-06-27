# 🧠 Crypto Trading Bot (Binance Futures Testnet)

This is a simplified **crypto trading bot** built using Python and Binance's USDT-M Futures Testnet. It allows users to place **market** and **limit** orders with clear CLI-based input and robust logging and error handling.



## ✅ Features

- ✔️ Place **market** and **limit** orders
- ✔️ Supports **BUY** and **SELL** sides
- ✔️ Command-line interface (CLI)
- ✔️ Logs requests and errors to console
- ✔️ Built on **Binance Futures Testnet**
- ✔️ Clean and modular code structure



## ⚙️ Requirements

- Python 3.8+
- [Binance Testnet API Key & Secret](https://testnet.binancefuture.com)
- Internet connection

Install required packages:
pip install -r requirements.txt
🚀 How to Use
🔐 Step 1: Setup Binance Testnet
Go to: https://testnet.binancefuture.com

Register and get your API key & secret

Replace your credentials in config.py:
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"


🧾 Step 2: Run the Bot
🧪 ✅ Test Commands for the Bot
1. Market Order – BUY
python main.py --symbol BTCUSDT --order_type MARKET --side BUY --quantity 0.001
2. Market Order – SELL
python main.py --symbol BTCUSDT --order_type MARKET --side SELL --quantity 0.001
3. Limit Order – BUY
python main.py --symbol BTCUSDT --order_type LIMIT --side BUY --quantity 0.001 --price 50000
4. Limit Order – SELL
python main.py --symbol BTCUSDT --order_type LIMIT --side SELL --quantity 0.001 --price 60000
5. Invalid Symbol Test
python main.py --symbol INVALIDCOIN --order_type MARKET --side BUY --quantity 0.001
6. Missing Required Argument
python main.py --symbol BTCUSDT --order_type MARKET --side BUY
# This should raise an error about missing quantity
🛠️ If You Implemented Bonus
7. Stop-Limit Order 
python main.py --symbol BTCUSDT --order_type STOP_LIMIT --side BUY --quantity 0.001 --price 50000 --stop_pric

Crypto_trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── tradingBot.py            # Basic order logic
│   ├── ExtendedTradingBot.py    # Bonus features (optional)
│   ├── cli.py                   # Command-line interface handler
│   ├── config.py                # API credentials
│   └── logger_config.py         # Logging setup
│
├── main.py                      # Entry point
├── requirements.txt
└── README.md
