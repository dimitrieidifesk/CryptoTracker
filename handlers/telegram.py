import telebot
from core.config import project_settings


def send_notify(message):
    bot = telebot.TeleBot(project_settings.TG_BOT_API_KEY)
    bot.send_message(project_settings.TG_USER_ID, message)
