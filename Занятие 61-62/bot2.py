import telebot
import random


bot = telebot.TeleBot(token)

todo = []
user_state = ''


@bot.message_handler(commands=['weather'])
def weather(message):
    print(message)
    bot.reply_to(message, 'погода не очень! 😂')


@bot.message_handler(commands=['course'])
def course(message):
    print(message)
    bot.reply_to(message, 'не очень! 😂')


@bot.message_handler(commands=['hello'])
def hello(message):
    print(message)
    bot.reply_to(message, 'Привет! 😍')


@bot.message_handler(commands=['coin'])
def coin(message):
    res = random.choice(['Орел', 'Решка'])
    bot.reply_to(message, res)


@bot.message_handler(regexp='привет')
def hello_message(message):
    bot.reply_to(message, 'привет 👀')


@bot.message_handler(commands=['add'])
def add(message):
    global user_state
    user_state = 'add'
    bot.reply_to(message, 'Введи текст задачи: ')


@bot.message_handler(commands=['tasks'])
def get_task_list(message):
    bot.reply_to(message, ', '.join(todo))


@bot.message_handler(func=lambda message: True)
def get_task(message):
    global user_state
    if user_state == 'add':
        todo.append(message.text)
        user_state = ''
        bot.reply_to(message, "Добавил в базу")


bot.infinity_polling()



# pythontelebot shift+enter => перенос строки, W+Ю => смайлик
