# main.py
# File nay la diem chinh de chay he thong

from exchange import exchange
from database import db_manager
from telegram_bot import telegram_bot
from websocket_client import ws_client
import threading

def run_websocket():
    """Chay WebSocket trong thread rieng"""
    ws_client.connect()

if __name__ == "__main__":
    # Ket noi database va tao bang
    db_manager.connect()
    db_manager.create_table()

    # Lay du lieu thi truong
    market_data = exchange.get_market_data()
    print("Du lieu thi truong:", market_data)

    # Gui thong bao Telegram
    telegram_bot.send_message("Bot da khoi dong!")

    # Chay WebSocket
    ws_thread = threading.Thread(target=run_websocket)
    ws_thread.start()

    # Giua he thong chay
    ws_thread.join()
    db_manager.disconnect()