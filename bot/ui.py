from bot.tradingBot import TradingBot
import questionary
import logging

# Configure logging
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    api_key = questionary.text("Enter your Binance Testnet API Key:").ask()
    api_secret = questionary.text("Enter your Binance Testnet Secret Key:").ask()

    bot = TradingBot(api_key, api_secret)

    while True:
        order_type = questionary.select(
            "Choose order type:",
            choices=["MARKET", "LIMIT", "STOP_MARKET", "OCO_SIMULATED", "BALANCE", "OPEN_ORDERS", "EXIT"]
        ).ask()

        if order_type == "EXIT":
            print("Exiting bot.")
            break

        if order_type == "BALANCE":
            balance = bot.get_balance()
            print("USDT Balance:", balance)
            continue

        if order_type == "OPEN_ORDERS":
            symbol = questionary.text("Trading pair (e.g., BTCUSDT):").ask()
            orders = bot.get_open_orders(symbol)
            print("Open Orders:", orders)
            continue

        symbol = questionary.text("Trading pair (e.g., BTCUSDT):").ask()
        quantity = float(questionary.text("Quantity (e.g., 0.01):").ask())

        result = None  # Declare result to avoid UnboundLocalError

        if order_type == "OCO_SIMULATED":
            take_profit = float(questionary.text("Take Profit Price:").ask())
            stop_loss = float(questionary.text("Stop Loss Price:").ask())
            result = bot.place_oco_simulated(
                symbol=symbol,
                quantity=quantity,
                take_profit_price=take_profit,
                stop_price=stop_loss
            )
        else:
            side = questionary.select("Order side:", choices=["BUY", "SELL"]).ask()

            if order_type == "LIMIT":
                limit_price = float(questionary.text("Limit Price:").ask())
                result = bot.place_order(symbol, side, order_type, quantity, limit_price)

            elif order_type == "STOP_MARKET":
                stop_price = float(questionary.text("Stop Price:").ask())
                result = bot.place_order(symbol, side, order_type, quantity, stop_price=stop_price)

            elif order_type == "MARKET":
                result = bot.place_order(symbol, side, order_type, quantity)

        print("Order Result:", result)

if __name__ == "__main__":
    main()
