# 📈 PrimeTrade Futures Trading Bot

This is a simplified Binance Futures trading bot for PrimeTrade.ai's internship assignment. It allows you to place market, limit, and stop-limit orders on the Binance Futures Testnet via CLI or a web UI.

---

## ⚙️ Features
- ✅ Binance Futures Testnet Integration
- ✅ Place Market, Limit, and Stop Orders
- ✅ Command-Line Interface (CLI)
- ✅ Streamlit-based Web UI
- ✅ Logging and Error Handling
- ✅ Test Mode for Simulated Orders

---

## 📦 Setup

1. Clone the repo:
```bash
git clone https://github.com/Shuvra-458/binance_project.git
cd binance_project

2. Create and activate a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
bash
Copy code
pip install -r requirements.txt

4. Create a file named api.env with your Binance Testnet credentials:
env
Copy code
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here

🚀 Running the Bot
CLI Mode:
Copy code
python bot/ui_cli.py
Web UI:
Copy code
streamlit run ui/web_ui.py

🧪 Test Mode
Set test_mode=True in the code to simulate orders without placing them on Binance.

🔐 Notes
Uses Binance Futures Testnet: https://testnet.binancefuture.com

Make sure to add funds using the testnet faucet.



