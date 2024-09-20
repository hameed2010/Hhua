import telebot

from telebot import types

import time

import re

import json

import threading

import requests 

from googletrans import Translator

translator = Translator()

CHANNEL_USERNAME = '@zzz666h'

CHANNEL_ID = '@tmx778'

bot = telebot.TeleBot("7375134394:AAF6BxIBL3xs-gsJIygB8sEKQjf9L4KUuWU")



@bot.message_handler(commands=['start'])

def start(message):
    chat_id = message.chat.id

    is_subscribed = bot.get_chat_member(CHANNEL_USERNAME, chat_id).status != 'left'

    if is_subscribed:
        print('&')
    else:
        user_name = message.chat.first_name

        keyboaryd = telebot.types.InlineKeyboardMarkup(row_width=1)

        no_button = telebot.types.InlineKeyboardButton(" زياده متابعين ", url="https://t.me/blum/app?startapp=ref_0cElJW7yMf")
        no_button2 = telebot.types.InlineKeyboardButton("زياده لايكات", url="http://t.me/catsgang_bot/join?startapp=iU6HBfwBGZiwUZN2039iU")
        no_button3 = telebot.types.InlineKeyboardButton(" زيادة مشاهدات", url="https://t.me/theYescoin_bot/Yescoin?startapp=EswZ7k")

        keyboaryd.add(no_button, no_button3, no_button2)

        text_message = (
        "- مرحبًا    أنا بوت رشق متابعين إنستجرام مجانًا"
              )

        bot.send_message(chat_id=chat_id, text=text_message, reply_markup=keyboaryd)



bot.polling()

