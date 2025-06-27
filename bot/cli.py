import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Crypto Trading Bot (Binance Futures Testnet)")

    parser.add_argument("--api_key", help="Binance API Key")
    parser.add_argument("--api_secret", help="Binance API Secret")
    parser.add_argument("--symbol", default="BTCUSDT", help="Trading pair symbol")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", choices=["MARKET", "LIMIT", "STOP_LIMIT", "OCO_SIM"], help="Order type")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit/Stop price")

    # ✅ OCO Simulated only
    parser.add_argument("--take_profit", type=float, help="Take profit price (for OCO_SIM only)")
    parser.add_argument("--stop_price", type=float, help="Stop price for stop loss (for OCO_SIM only)")

    # ✅ Optional utilities
    parser.add_argument("--check_balance", action="store_true", help="Check Futures USDT balance")
    parser.add_argument("--show_orders", action="store_true", help="Show open orders for symbol")

    return parser.parse_args()
