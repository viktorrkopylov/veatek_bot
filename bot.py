#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio
import os
from googletrans import Translator
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(os.environ["TELEGRAM_TOKEN"])


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am Veatek_bot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    translator = Translator()
    result = await translator.translate(message.text, dest = 'en')
    await bot.reply_to(message, f'{message.text}\n\n{result.text}')

if __name__ == '__main__':
    asyncio.run(bot.polling())
