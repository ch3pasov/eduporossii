import telebot
from secret import token0, token1, token2
from time import sleep

bot0 = telebot.TeleBot(token0)
bot1 = telebot.TeleBot(token1)
bot2 = telebot.TeleBot(token2)

j=0
def cleaner(i):
    global j
    if j==0:
        try:
            bot0.delete_message('@eduporossii', i)
        except:
            pass
    elif j==1:
        try:
            bot1.delete_message('@eduporossii', i)
        except:
            pass
    else:
        try:
            bot2.delete_message('@eduporossii', i)
        except:
            pass
    j=(j+1)%3


id_start=900
id_end=73106

for i in range(id_start, id_end):
    cleaner(i)
