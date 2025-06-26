import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from base_bot import TradingBot
import streamlit as st
from dotenv import load_dotenv

from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, SIDE_BUY, SIDE_SELL
ORDER_TYPE_STOP = "STOP"
ORDER_TYPE_STOP_MARKET = "STOP_MARKET"


load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

bot = TradingBot(api_key, api_secret)

st.set_page_config(page_title="PrimeTrade Bot", page_icon="📈", layout="centered")

st.title("📈 PrimeTrade Binance Futures Bot")
st.markdown("Place orders directly on Binance Futures Testnet.")

with st.expander("🛠️ Order Configuration", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        symbol = st.text_input("Trading Pair", value="BTCUSDT")
        quantity = st.number_input("Quantity", min_value=0.001, format="%.3f")

    with col2:
        side = st.selectbox("Order Side", ["BUY", "SELL"])
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP"])


price = None
stop_price = None

if order_type == ORDER_TYPE_LIMIT:
    price = st.number_input("Limit Price", min_value=0.0, format="%.2f")
elif order_type == ORDER_TYPE_STOP:
    stop_price = st.number_input("Stop Price", min_value=0.0, format="%.2f")
    price = st.number_input("Limit Price After Trigger", min_value=0.0, format="%.2f")

if st.button("🚀 Place Order"):
    order = bot.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
        stop_price=stop_price
    )

    if "error" in order:
        st.error(f"❌ Order Failed: {order['error']}")
    else:
        st.success("✅ Order Placed Successfully!")
        st.json(order)
st.markdown("---")
st.markdown("🔒 Built with ❤️ for PrimeTrade.ai • Binance Testnet")
