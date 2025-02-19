import requests
import time
import socket
import telebot

# Telegram Bot Token (from BotFather)
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# IP or hostname to monitor
TARGET_IP = "YOUR_TARGET_IP_OR_HOSTNAME"

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

def is_online(ip):
    """Check if the IP is online by trying to connect to it."""
    try:
        socket.create_connection((ip, 80), timeout=3)
        return True
    except OSError:
        return False

# Send startup message
bot.send_message(CHAT_ID, "🚀 Bot is up and running!")

# Track last known status
last_status = is_online(TARGET_IP)

while True:
    current_status = is_online(TARGET_IP)

    if last_status != current_status:
        status_msg = "ONLINE ✅" if current_status else "OFFLINE ❌"
        bot.send_message(CHAT_ID, f"🔔 IP {TARGET_IP} is now {status_msg}")
        last_status = current_status

    time.sleep(30)  # Check every 30 seconds
