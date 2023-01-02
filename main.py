import os
import telebot
import multiprocessing

BOT_TOKEN = "5813888040:AAE309_V6KI3hjE4QpoBuPitF85bSmWgJ-o"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome_msg(message):
    msg = """سلام 😍

    این ربات کارش فرستادن پیام خودتونه برای اینکه به هر دلیلی کسی متوجه نشه اصل پیام برای کی بوده. 
    اینم بگم که در آینده قابلیت های بیشتری اضافه خواهد شد به این بات😁

    برای اینکه بدونی چه کارهایی هم میشه با این بات انجام داد /help رو بزن.

    امیدوارم مناسب کاری که میخوای بکنی باشه🤝
    """
    bot.reply_to(message, msg)


@bot.message_handler(commands=['help'])
def send_help_msg(message):
    msg = """خوش اومدی :)

    فعلا تنها قابلیت بات همینه که پیامی که میفرستی یا فوروارد میکنی رو برات میفرستیم تا راحت بدون اینکه اسم فرد اصلی بالای پیایم بخوره فورواردش کنی..

    برای اینکار اون پیام رو فوروارد کن یا مستقیم تایپش کن
    """

    bot.reply_to(message, msg)


@bot.message_handler(func=lambda msg: True)
def send_forw_msg(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, 'به امید دیدار 😁')
    bot.send_sticker(message.chat.id,)


bot.infinity_polling()
# print('bot is running...')
