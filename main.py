from bot.cli import parse_args
from bot.logger_config import init_logging
from bot.config import API_KEY, API_SECRET, DEFAULT_SYMBOL, USE_TESTNET
from bot.tradingBot import TradingBot
import logging

def main():
    init_logging()
    args = parse_args()

    # Use CLI values if provided, otherwise fall back to .env
    api_key = args.api_key or API_KEY
    api_secret = args.api_secret or API_SECRET
    symbol = args.symbol or DEFAULT_SYMBOL

    if not api_key or not api_secret:
        logging.error("❌ API Key and Secret are required.")
        print("❌ API Key and Secret are required.")
        return

    bot = TradingBot(api_key, api_secret, use_testnet=USE_TESTNET)

    if args.check_balance:
        balance = bot.get_balance()
        print(f"🪙 Futures Balance: {balance}")
        return

    if args.show_orders:
        orders = bot.get_open_orders(symbol)
        print(f"📋 Open Orders: {orders}")
        return

    # ✅ Handle Simulated OCO Order
    if args.type == "OCO_SIM":
        if not args.take_profit or not args.stop_price:
            logging.error("❌ --take_profit and --stop_price are required for OCO_SIM orders.")
            print("❌ --take_profit and --stop_price are required for OCO_SIM orders.")
            return

        result = bot.place_oco_simulated(
            symbol=symbol,
            quantity=float(args.quantity),
            take_profit_price=float(args.take_profit),
            stop_price=float(args.stop_price),

        )

        if result:
            print("✅ OCO Simulated Orders Placed Successfully:")
            print("📈 Take Profit:", result["take_profit_order"])
            print("🛑 Stop Loss:", result["stop_loss_order"])
        else:
            print("❌ OCO Simulated Order Failed.")
        return

    # ✅ Handle Regular Order Types (Market, Limit, Stop-Limit)
    if args.side and args.type and args.quantity:
        order = bot.place_order(
            symbol=symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            limit_price=args.price
        )

        if order:
            print(f"✅ Order executed successfully: {order.get('orderId')}")
            print("✅ Order response received.")
        else:
            print("❌ Order failed.")
    else:
        logging.error("❌ Missing required arguments for placing order.")
        print("❌ Missing required arguments for placing order.")

if __name__ == "__main__":
    main()
