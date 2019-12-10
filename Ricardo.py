import datetime
import telebot

bot = telebot.TeleBot('931907478:AAE5az3JY8pvjstdqhUDOKlLeMzTWXBjqwc')
now = datetime.datetime.now()
@bot.message_handler(commands=['ДЗ'])
def homework(message):
    bot.reply_to(message, 'ДЗ на среду:\nГеометрия - 12(8;10;12;14;16).\nУкр мова - не задано.\nФизика - презентации на темы в тетраде.\nИстория - Урок отменен.\nЗаруб. Лит. - стих Пушкина \"Я помню чудное мгновенье\"')

@bot.message_handler(commands=['events'])
def start_message(message):
    bot.reply_to(message, 'Новости отсутствуют.')

@bot.message_handler(commands=['copy'])
def copy(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['delete'])
def handler_clear(message):
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['date'])
def handler_clear(message):
    bot.reply_to(message, "Дата: " + str(now.strftime("%d-%m-%Y %H:%M")))

@bot.message_handler(commands=['spam'])
def handler_clear(message):
    spam_count = 0
    bot.delete_message(message.chat.id, message.message_id)
    while spam_count<5:
        spam_count+=1
        bot.send_message(message.chat.id, "SPAM FUNCTION")

@bot.message_handler(content_types=['text'])
def send_text(message):
    for i in range(len(message.text)):
        if message.text[i] == "Д" and message.text[i+1] == "З":
            homework(message)

bot.polling()