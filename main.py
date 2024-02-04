import re
import telebot
from telebot import types
from ConvertToBold import *
from CheckPremium import *
from PHILBOSS17 import *
from PHILBossCommand import *

TOKEN = #BOT_TOKEN
bot = telebot.TeleBot(TOKEN)

# Dictionary to store active commands and their queues
active_commands = {}

# Function to add a user to the queue for a specific command
def add_to_queue(user_id, command):
    if command in active_commands:
        active_commands[command].append(user_id)
    else:
        active_commands[command] = [user_id]

# Function to remove a user from the active command dictionary
def remove_from_active(user_id, command):
    if command in active_commands:
        active_commands[command].remove(user_id)

def lowercase_text(text):
    return text.lower()

active_users_messages = {}
    
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Get user ID and username
    sender_username = message.from_user.username
    sender_id = message.from_user.id
    is_premium = CheckPremiumUSER(str(sender_id))
    isGROUP = message.chat.type == "group" or message.chat.type == "supergroup"
    success_info = ""
    failed_info = ""
    progress = 0
    success = 0
    failed = 0
    telegram_message = message.text
    if is_premium[0]:
        title_user = f"{ConvertToBold('By ↯ ')}@{sender_username}|{ConvertToBold('PREMIUM')}"
        limit_count = 50
    else:
        title_user = f"{ConvertToBold('By ↯ ')}@{sender_username}|{ConvertToBold('FREE')}"
        limit_count = 15
    
    if lowercase_text(telegram_message).startswith("/phlboss17"):
        if "PHLBoss17" in active_commands:
            add_to_queue(sender_id, "PHLBoss17")
            bot.send_message(sender_id, f"@{sender_username} currently using this command. you are in the queue please wait")
        else:
            PHLBoss17Command(bot, message, isGROUP, is_premium, limit_count, title_user, success_info, failed_info, progress, success, failed)
            remove_from_active(sender_id, "PHLBoss17")

bot.polling()
