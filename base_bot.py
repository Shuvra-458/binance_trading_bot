# bot/base_bot.py
from binance.client import Client
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT
ORDER_TYPE_STOP = 'STOP'
ORDER_TYPE_STOP_MARKET = 'STOP_MARKET'
import logging
import os
import traceback


class TradingBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com'
            self.client.API_URL = 'https://testnet.binancefuture.com'
        logging.basicConfig(filename='logs/bot.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Bot initialized")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == ORDER_TYPE_LIMIT:
                params.update({
                    "timeInForce": TIME_IN_FORCE_GTC,
                    "price": price
                })
            elif order_type == ORDER_TYPE_STOP_MARKET:
                params["stopPrice"] = stop_price
            elif order_type == ORDER_TYPE_STOP:
                params.update({
                    "stopPrice": stop_price,
                    "price": price,
                    "timeInForce": TIME_IN_FORCE_GTC
                })

            order = self.client.futures_create_order(**params)
            logging.info(f"Order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")
            traceback.print_exc()  
            return {"error": str(e)}

    def grid_strategy(self, symbol, side, start_price, end_price, step, quantity):
        """
        Place a series of LIMIT orders between start and end price.
        """
        try:
            price = start_price
            while (price <= end_price if side == SIDE_BUY else price >= end_price):
                self.place_order(symbol, side, ORDER_TYPE_LIMIT, quantity, price)
                price = round(price + step if side == SIDE_BUY else price - step, 2)
            logging.info("Grid orders placed successfully.")
        except Exception as e:
            logging.error(f"Grid strategy failed: {str(e)}")
