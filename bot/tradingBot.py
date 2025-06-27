# tradingBot.py

from binance.client import Client
from binance.enums import (
    SIDE_BUY, SIDE_SELL,
    ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC
)
import logging

class TradingBot:
    def __init__(self, api_key: str, api_secret: str, use_testnet: bool = True):
        self.client = Client(api_key, api_secret)
        if use_testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, limit_price: float = None):
        try:
            side_enum = SIDE_BUY if side.upper() == "BUY" else SIDE_SELL

            if order_type.upper() == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type.upper() == "LIMIT":
                if limit_price is None:
                    raise ValueError("Price must be specified for LIMIT orders")
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type="LIMIT",
                    quantity=quantity,
                    price=str(limit_price),
                    timeInForce=TIME_IN_FORCE_GTC
                )

            elif order_type.upper() == "STOP_LIMIT":
                if limit_price is None:
                    raise ValueError("Price must be specified for STOP-LIMIT orders")
                stop_price = float(limit_price) * 0.995
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type="STOP_MARKET",
                    stopPrice=str(stop_price),
                    quantity=quantity,
                    timeInForce=TIME_IN_FORCE_GTC
                )

            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            logging.info("\u2705 Order placed: %s", order)
            return order

        except Exception as e:
            logging.error("\u274c Failed to place order: %s", str(e))
            return None

    def place_oco_simulated(self, symbol: str, quantity: float, take_profit_price: float, stop_price: float):
        try:
            tp_order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_SELL,
                type="LIMIT",
                quantity=quantity,
                price=str(take_profit_price),
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info("\u2705 Take Profit order placed: %s", tp_order)

            sl_order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_SELL,
                type="STOP_MARKET",
                stopPrice=str(stop_price),
                closePosition=False,
                quantity=quantity,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info("\u2705 Stop Loss order placed: %s", sl_order)

            return {"take_profit_order": tp_order, "stop_loss_order": sl_order}

        except Exception as e:
            logging.error("\u274c Failed to place simulated OCO: %s", str(e))
            return None

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            usdt_balance = next((item for item in balance if item['asset'] == 'USDT'), None)
            return usdt_balance
        except Exception as e:
            logging.error("\u274c Failed to fetch balance: %s", str(e))
            return None

    def get_open_orders(self, symbol: str):
        try:
            orders = self.client.futures_get_open_orders(symbol=symbol)
            return orders
        except Exception as e:
            logging.error("\u274c Failed to fetch open orders: %s", str(e))
            return None

    def calculate_pnl(self, entry_price: float, exit_price: float, quantity: float, side: str):
        try:
            if side.upper() == "BUY":
                pnl = (exit_price - entry_price) * quantity
            else:
                pnl = (entry_price - exit_price) * quantity
            logging.info(f"\u2705 PnL Calculated: {pnl}")
            return pnl
        except Exception as e:
            logging.error("\u274c Failed to calculate PnL: %s", str(e))
            return None
