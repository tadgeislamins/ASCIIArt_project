import telebot
from telebot import types

cmd_create = "Создать свой ASCII-арт"
cmd_premade = "Выбрать ASCII-арт из коллекции"
cmd_goose = "Запустить гуся"
msg_init = "Что вы хотите сделать?"
msg_guide_start = "Чтобы начать работу, напишите /start"
msg_guide_sendimg = "Пожалуйста, отправьте картинку"
msg_wip = "Coming soon..."

bot = telebot.TeleBot(open('token.txt').read()[:-1])  # токен бота; в телеге t.me/ASCIIArt_project_bot

# старт и кнопочки
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        create_art = types.KeyboardButton(cmd_create)
        choose_art = types.KeyboardButton(cmd_premade)
        goose = types.KeyboardButton(cmd_goose)
        markup.add(create_art, choose_art, goose)
        bot.send_message(message.from_user.id, msg_init, reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, msg_guide_start)

@bot.message_handler(content_types=['text'])
def functions(message):
    if message.text == cmd_create:
        bot.send_message(message.from_user.id, msg_guide_sendimg)
    elif message.text == cmd_premade:
        bot.send_message(message.from_user.id, msg_wip)
    elif message.text == cmd_goose:
        with open("goose.txt", encoding="utf8") as goose:
            goose = goose.read()
        bot.send_message(message.from_user.id, goose)

# тут он отправляет txt файл в ответ на картинку
@bot.message_handler(content_types=['photo'])
def send_art(message):
    reply = open("reply.txt", encoding="utf8")
    bot.send_document(message.from_user.id, reply)


bot.polling(none_stop=True, interval=0)
