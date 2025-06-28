# 🪙 Crypto Trading Bot (Binance Futures Testnet)

This is a simplified **crypto trading bot** built using Python and Binance's USDT-M Futures Testnet. It supports:

- Market orders
- Limit orders
- Stop-Market orders
- Simulated OCO (One-Cancels-the-Other) orders
- Fetching balance and open orders

---

## 🚀 Features

- ✅ Place `MARKET`, `LIMIT`, `STOP_MARKET`, `OCO_SIMULATED` orders
- ✅ View `BALANCE` and `OPEN_ORDERS`
- ✅ Interactive CLI with `questionary`
- ✅ Logs all actions to `bot.log`
- ✅ Built on **Binance Futures Testnet**
- ✅ Clean and modular codebase

---

## 📦 Requirements

- Python 3.8+
- Internet connection
- Install dependencies:
  
```bash
pip install -r requirements.txt
Dependencies include:

python-binance

questionary

🔐 Binance Testnet Setup
Go to: https://testnet.binancefuture.com

Register and create your API Key + Secret

Fund your testnet account with USDT

💻 How to Run
python -m bot.ui
You will be prompted to:

Enter your Testnet API Key and Secret

Choose order type

Provide trading parameters

📘 Sample Flow
? Enter your Binance Testnet API Key: ****
? Enter your Binance Testnet Secret Key: ****
? Choose order type: MARKET
? Trading pair (e.g., BTCUSDT): BTCUSDT
? Quantity (e.g., 0.01): 0.01
? Order side: BUY
Order Result: {...}
📊 Supported Order Types
Order Type	Prompted Fields
MARKET	symbol, quantity, side
LIMIT	symbol, quantity, side, limit price
STOP_MARKET	symbol, quantity, side, stop + limit
OCO_SIMULATED	symbol, quantity, TP price, SL price
BALANCE	Displays USDT balance
OPEN_ORDERS	Displays all open orders

🧾 Logging
All events are logged to bot.log:

2025-06-28 11:00:00 - ✅ Order placed: {...}
2025-06-28 11:01:00 - ❌ Failed to place order: APIError(code=...)

# 1. Market Order – BUY
python main.py --symbol BTCUSDT --order_type MARKET --side BUY --quantity 0.001

# 2. Limit Order – SELL
python main.py --symbol BTCUSDT --order_type LIMIT --side SELL --quantity 0.001 --price 60000

# 3. Invalid Symbol Test
python main.py --symbol INVALIDCOIN --order_type MARKET --side BUY --quantity 0.001