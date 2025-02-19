import os
import time
import telebot
import platform

# Telegram Bot Token (from BotFather)
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# IP or hostname to monitor
TARGET_IP = "YOUR_TARGET_IP_OR_HOSTNAME"

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

def is_online(ip):
    """Check if the IP is online using ICMP ping."""
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {param} {ip} > /dev/null 2>&1")
    return response == 0  # Returns True if ping is successful

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
