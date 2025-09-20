**Module 1 – Signal Source**

Task: Kết nối Involio → lấy tín hiệu.

Risk: có thể không có API → cần scraping hoặc reverse engineer.

Output: hàm get_signals() trả về JSON {symbol, side, size, leverage}.

**Module 2 – Trade Execution**

Task: kết nối Binance/Bybit API (ccxt), web3 (ví).

Output: hàm execute_trade(signal) → mở/đóng lệnh.

Risk: mapping lệnh từ Involio sang exchange.

**Module 3 – Risk Management**

Task: stop-loss, max position, leverage cap, kill-switch.

Output: middleware kiểm tra trước khi gọi API execute_trade.

**Module 4 – Logging & Monitoring**

Task: log trades vào DB (Mongo/Postgres).

Output: collection trades + balances.

**Module 5 – Dashboard
**
Task: UI đơn giản (Streamlit/React).

Output: trang hiển thị balance, PnL, trades, error logs.

**Module 6 – Deployment & Docs**

Task: Dockerize, deploy server, viết docs.

Output: bot chạy 24/7, hướng dẫn setup.
