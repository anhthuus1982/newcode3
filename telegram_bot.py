# telegram_bot.py
# File nay giao tiep voi Telegram API

import requests
from config import Config

class TelegramBot:
    def __init__(self):
        self.token = Config.TELEGRAM_TOKEN
        self.chat_id = Config.TELEGRAM_CHAT_ID

    def send_message(self, message):
        """Gui tin nhan den Telegram"""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            print("Gui tin nhan thanh cong")
        except requests.RequestException as e:
            print(f"Loi gui tin nhan Telegram: {e}")

# Khoi tao instance
telegram_bot = TelegramBot()