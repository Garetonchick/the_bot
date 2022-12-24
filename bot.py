# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from telebot.async_telebot import AsyncTeleBot
import asyncio
import os
import dbconnect
import requests
import random
from sqlalchemy import text

bot = AsyncTeleBot(os.getenv('TOKEN'))

def run_db_select_statement():
    """Creates a self closing connection to the database after outputting 'Hello World'"""
    with dbconnect.create_connection() as conn:
        result = conn.execute(text("select 'Hello World'"))
        print(result.all())


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    # run_db_select_statement()
    await bot.reply_to(message, """\
        Команды:
        /tyanochku_bi -- получить тяночку\n
        /catgirl_bi -- получить кошкодевочку\n
        /momashu_bi -- получить момашу\n
        /just_want_to_be_happy\n 
        /cringe -- кринж
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# async def echo_message(message):
#     await bot.reply_to(message, message.text)

waifu_types = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'hug', 'awoo', 'kiss', 'smug',
               'bonk', 'blush', 'smile', 'happy', 'dance', 'cringe']


@bot.message_handler(commands=['tyanochku_bi'])
async def tyanochku_bi(m):
    for i in range(6):
        try:
            data = requests.get(url='https://api.waifu.pics/sfw/' 
                                + random.choice(waifu_types)).json()
            await bot.send_photo(m.chat.id, data['url'])
            break
        except:
            pass


@bot.message_handler(commands=['catgirl_bi'])
async def catgirl_bi(m):
    for i in range(6):
        try:
            data = requests.get(url='https://api.waifu.pics/sfw/' 
                                + "neko").json()
            await bot.send_photo(m.chat.id, data['url'])
            break
        except:
            pass

@bot.message_handler(commands=['momashu_bi'])
async def momashu_bi(m):
    for i in range(6):
        try:
            data = requests.get(url='https://api.waifu.pics/sfw/' 
                                + "waifu").json()
            await bot.send_photo(m.chat.id, data['url'])
            break
        except:
            pass

@bot.message_handler(commands=['just_want_to_be_happy'])
async def just_want_to_be_happy(m):
    for i in range(6):
        try:
            data = requests.get(url='https://api.waifu.pics/sfw/' 
                                + "happy").json()
            await bot.send_photo(m.chat.id, data['url'])
            break
        except:
            pass

@bot.message_handler(commands=['cringe'])
async def cringe(m):
    for i in range(6):
        try:
            data = requests.get(url='https://api.waifu.pics/sfw/' 
                                + "cringe").json()
            await bot.send_photo(m.chat.id, data['url'])
            break
        except:
            pass

asyncio.run(bot.polling())