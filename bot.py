import requests
import time
import socket
import telebot
import os

# Telegram Bot Token (from BotFather)
BOT_TOKEN=os.getenv("BOT_TOKEN")
CHAT_ID=os.getenv("CHAT_ID")
TARGET_IP=os.getenv("TARGET_IP")

bot = telebot.TeleBot(BOT_TOKEN)

def is_online(ip):
    """Check if the IP is online using ICMP ping."""
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {param} {ip} > /dev/null 2>&1")
    return response == 0  # Returns True if ping is successful

# Send startup message
bot.send_message(CHAT_ID, "🚀 Bot is up and running!")

# Track last known status
last_status = None

while True:
    current_status = is_online(TARGET_IP)

    if last_status != current_status:
        status_msg = "ONLINE ✅" if current_status else "OFFLINE ❌"
        bot.send_message(CHAT_ID, f"🔔 IP {TARGET_IP} is now {status_msg}")
        last_status = current_status

    time.sleep(30)  # Check every 30 seconds
