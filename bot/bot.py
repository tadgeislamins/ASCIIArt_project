import telebot
from telebot import types

bot = telebot.TeleBot(
    "5385485353:AAH92twkm4czMP0uEy-ZYLqSlGSfCA179D0")  # токен бота; в телеге t.me/ASCIIArt_project_bot

# старт и кнопочки
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        create_art = types.KeyboardButton("Создать свой ASCII art")
        choose_art = types.KeyboardButton("Выбрать ASCII art из коллекции")
        goose = types.KeyboardButton("Запустить гуся")
        markup.add(create_art, choose_art, goose)
        bot.send_message(message.from_user.id, "Что вы хотите сделать?", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Чтобы начать работу, напишите /start")

@bot.message_handler(content_types=['text'])
def functions(message):
    if message.text == "Создать свой ASCII art":
        bot.send_message(message.from_user.id, "Пожалуйста, отправьте картинку")
    elif message.text == "Выбрать ASCII art из коллекции":
        bot.send_message(message.from_user.id, "Coming soon...")
    elif message.text == "Запустить гуся":
        with open("goose.txt", encoding="utf8") as goose:
            goose = goose.read()
        bot.send_message(message.from_user.id, goose)

# тут он отправляет txt файл в ответ на картинку
@bot.message_handler(content_types=['photo'])
def send_art(message):
    reply = open("reply.txt", encoding="utf8")
    bot.send_document(message.from_user.id, reply)


bot.polling(none_stop=True, interval=0)
