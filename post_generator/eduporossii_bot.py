import telebot
#но вы ключей не увидите
from secret import token0, token1, token2
from time import sleep

bot0 = telebot.TeleBot(token0)
bot1 = telebot.TeleBot(token1)
bot2 = telebot.TeleBot(token2)

while True:
    sleep(1.467)
    bot0.send_message('@eduporossii', 'еду по России,', disable_notification=True)
    sleep(1)
    bot0.send_message('@eduporossii', 'не доеду до конца', disable_notification=True)
    sleep(1.467)
    bot1.send_message('@eduporossii', 'еду по России,', disable_notification=True)
    sleep(1)
    bot1.send_message('@eduporossii', 'не доеду до конца', disable_notification=True)
    sleep(1.467)
    bot2.send_message('@eduporossii', 'еду по России,', disable_notification=True)
    sleep(1)
    bot2.send_message('@eduporossii', 'не доеду до конца', disable_notification=True)
