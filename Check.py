import requests
import telebot
import os
from telebot import types
import user_agent
from user_agent import generate_user_agent
token = input("[~] Enter Token :")
id = input('ID : ')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(id,f"<strong>Send Instaup ID To check coins\n=== === ===\nBy : @H_c_4</strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def mgit(message):
    text = message.text
    url = f'http://35.181.7.112/check.php?oid={text}&submit=submit'
    headers = {
       "User-Agent": str(generate_user_agent()),
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
       "Sec-Fetch-Site": "none",
       "Sec-Fetch-Mode": "navigate",
       "Sec-Fetch-User": "?1",
       "Sec-Fetch-Dest": "document",
       "Accept-Encoding": "gzip",
       "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    hadi = requests.get(url,headers=headers).text
    try:
		    coin = hadi.split('{"coins":"')[1]
		    coins = coin.split('"}')[0]
		    coin1 = int(coins)
		    bot.send_message(id,f"ID : {text}\nCoins : {coin1}")
    except IndexError:
        bot.send_message(id,f"BaD ID 🥺")
    pass
bot.polling()