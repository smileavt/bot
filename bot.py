import requests
import time
import socket
import telebot
import os
from ping3 import ping

# Telegram Bot Token (from BotFather)
BOT_TOKEN=os.getenv("BOT_TOKEN")
CHAT_ID=os.getenv("CHAT_ID")
TARGET_IP=os.getenv("TARGET_IP")

# IP or hostname to monitor


# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

def is_online(ip):
    """Check if the IP is online by pinging it."""
    response = ping(ip, timeout=3)
    return response is not None

# Track last known status
last_status = None  # Initialize with the current status

while True:
    current_status = is_online(TARGET_IP)

    if last_status != current_status:
        time.sleep(30)  # Wait for 30 seconds
        confirmed_status = is_online(TARGET_IP)
        if confirmed_status == current_status:
            status_msg = "ONLINE ✅" if current_status else "OFFLINE ❌"
            bot.send_message(CHAT_ID, f"🔔 IP {TARGET_IP} is now {status_msg}")
            last_status = current_status

    time.sleep(30)  # Check every 30 seconds
