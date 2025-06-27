
import csv
import os
import logging
from datetime import datetime

from binance import TIME_IN_FORCE_GTC, SIDE_SELL

from bot.tradingBot import TradingBot


class ExtendedTradingBot(TradingBot):
    def __init__(self, api_key, api_secret, use_testnet=True):
        super().__init__(api_key, api_secret, use_testnet)
        self.order_map = {}  # To keep track of simulated OCO pairs

    def place_oco_simulated(self, symbol, quantity, take_profit_price, stop_price):
        try:
            # Place TP order
            tp_order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_SELL,
                type="LIMIT",
                quantity=quantity,
                price=str(take_profit_price),
                timeInForce=TIME_IN_FORCE_GTC
            )

            # Place SL order
            sl_order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_SELL,
                type="STOP_MARKET",
                stopPrice=str(stop_price),
                quantity=quantity,
                timeInForce=TIME_IN_FORCE_GTC
            )

            # Store mapping for potential cancellation
            self.order_map[tp_order['orderId']] = sl_order['orderId']

            logging.info("✅ TP & SL placed. Monitoring for execution to cancel remaining.")
            print("✅ OCO Simulated Orders Placed Successfully:")
            print("📈 Take Profit:", tp_order)
            print("🛑 Stop Loss:", sl_order)

            # Save to CSV
            self.log_order_to_csv(tp_order)
            self.log_order_to_csv(sl_order)

            return {"take_profit_order": tp_order, "stop_loss_order": sl_order}

        except Exception as e:
            logging.error(f"❌ OCO placement failed: {e}")
            return None

    def log_order_to_csv(self, order):
        fieldnames = ["orderId", "symbol", "type", "side", "price", "stopPrice", "quantity", "status", "time"]
        filepath = "order_log.csv"

        write_header = not os.path.exists(filepath)

        with open(filepath, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if write_header:
                writer.writeheader()
            writer.writerow({
                "orderId": order.get("orderId"),
                "symbol": order.get("symbol"),
                "type": order.get("type"),
                "side": order.get("side"),
                "price": order.get("price"),
                "stopPrice": order.get("stopPrice", "-"),
                "quantity": order.get("origQty"),
                "status": order.get("status"),
                "time": datetime.now().isoformat()
            })

    def calculate_pnl(self, entry_price, exit_price, quantity, is_long=True):
        entry = float(entry_price)
        exit = float(exit_price)
        qty = float(quantity)
        pnl = (exit - entry) * qty if is_long else (entry - exit) * qty
        return round(pnl, 2)
