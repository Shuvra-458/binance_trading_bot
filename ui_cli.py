import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from base_bot import TradingBot
from dotenv import load_dotenv
from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, SIDE_BUY, SIDE_SELL
ORDER_TYPE_STOP = "STOP"
ORDER_TYPE_STOP_MARKET = "STOP_MARKET"


load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

bot = TradingBot(api_key, api_secret)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def main():
    while True:
        print("\n   WELCOME TO PRIMETRADE BOT CLI  ")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. Stop-Limit Order")
        print("4. Grid Strategy")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Try again.")
            continue

        if choice == "5":
            print("Exiting CLI")
            break

        symbol = input("Symbol (e.g. BTCUSDT): ").upper()
        side = input("Side (BUY or SELL): ").upper()
        quantity = get_float("Quantity: ")

        if choice == "1":
            order = bot.place_order(symbol, side, ORDER_TYPE_MARKET, quantity)
        elif choice == "2":
            price = get_float("Limit Price: ")
            order = bot.place_order(symbol, side, ORDER_TYPE_LIMIT, quantity, price=price)
        elif choice == "3":
            stop_price = get_float("Stop Price: ")
            limit_price = get_float("Limit Price: ")
            order = bot.place_order(symbol, side, ORDER_TYPE_STOP, quantity, price=limit_price, stop_price=stop_price)
        elif choice == "4":
            start_price = get_float("Start Price: ")
            end_price = get_float("End Price: ")
            step = get_float("Price Step: ")
            bot.grid_strategy(symbol, side, start_price, end_price, step, quantity)
            continue  # Skip order print

        if "error" in order:
            print(" Error placing order:", order["error"])
        else:
            print("✅ Order placed successfully!")
            print(order)

if __name__ == "__main__":
    main()

