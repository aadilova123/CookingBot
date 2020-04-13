from pydoc import text

import dp as dp
import telebot
import random

from telebot import types
from telebot.types import Message

TOKEN = '795813628:AAGfh-sl1k1wMf-t8OjC5GUVHksEtTnAI0g'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет,друг) Я Бот-Кухонная книга! Найди интересующий тебя рецепт через - Поиск, также со мной ты научишься готовить самые изысканные блюда начиная с простых до самых сложнейших!")
    keyboard = types.InlineKeyboardMarkup()
    key_search = types.InlineKeyboardButton(text='Поиск', callback_data='menu')
    keyboard.add(key_search)
    key_categories = types.InlineKeyboardButton(text='Категории', callback_data='menu')
    keyboard.add(key_categories)
    key_saves = types.InlineKeyboardButton(text='Избранные', callback_data='menu')
    keyboard.add(key_saves)
    key_random = types.InlineKeyboardButton(text='Рецепты', callback_data='menu')
    keyboard.add(key_random)
    key_support = types.InlineKeyboardButton(text='Настройка и помощь', callback_data='menu')
    keyboard.add(key_support)



    bot.send_message(message.from_user.id, text='Выбери то, что тебе нужно:', reply_markup=keyboard)
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши Привет")
  else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")



bot.polling(none_stop=True, interval=0)
