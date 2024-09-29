import requests
from datetime import datetime
import telebot
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def hello(message):
        bot.send_message(message.chat.id, "Hi! Type 'ton' or 'btc' to know this crypto price")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "ton":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/ton_usd")
                response = req.json()
                ton_price = response["ton_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d.%m.%y %H:%M')}\nTON price is: ${ton_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Request is incorrect. Type 'ton' to have correct response"
                )
        elif message.text.lower() == "btc":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                btc_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d.%m.%y %H:%M')}\nBTC price is: ${btc_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Request is incorrect. Type 'btc' to have correct response"
                )

        elif message.text.lower() == "eth":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response = req.json()
                eth_price = response["eth_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d.%m.%y %H:%M')}\nETH price is: ${eth_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Request is incorrect. Type 'eth' to have correct response"
                )
        else:
            bot.send_message(message.chat.id, "Check that you sent correct command, guy...")

    bot.polling()

if __name__ == '__main__':
    #get_data()
    telegram_bot(token)