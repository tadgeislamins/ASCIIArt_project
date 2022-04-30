import telebot
from telebot import types

cmd_create_shade = 'Создать тональный ASCII-арт'
cmd_create_line = 'Создать контурный ASCII-арт'
cmd_premade = 'Выбрать ASCII-арт из коллекции'
cmd_goose = 'Запустить гуся'

msg_init = 'Что вы хотите сделать?'
msg_guide_start = 'Чтобы начать работу, напишите /start'
msg_guide_sendimg = 'Пожалуйста, отправьте картинку. Можете указать желаемую ширину арта (по умолчанию {}).'
msg_sizeset = 'Принято! Теперь ширина таких артов будет {}.'
msg_wip = 'Coming soon...'
msg_nan = 'Это не число. Размер арта — по умолчанию.'
msg_notype = 'Сначала выберите тип арта.'

bot = telebot.TeleBot(open('token.txt').read()[:-1])
# токен бота; в телеге t.me/ASCIIArt_project_bot

size = {'shade': 50, 'line': 50}
art_type = ''
chat = ''


# старт и кнопочки
@bot.message_handler(commands=['start'])
def start(message):
    global art_type
    art_type = 0

    global chat
    chat = message.from_user.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cmd in [cmd_create_shade, cmd_create_line, cmd_premade, cmd_goose]:
        markup.add(types.KeyboardButton(cmd))
    bot.send_message(chat, msg_init, reply_markup=markup)


# ладно, мне не нравится
# позволяет изменить размер арта на этапе выбора картинки
# @bot.message_handler(func=lambda x: bool(art_type), content_types=['text'])
# def resize(message):
#     if message.text.isdigit():
#         global size
#         size[art_type] = int(message.text)
#         bot.send_message(chat, msg_sizeset.format(message.text))
#         bot.send_message(chat, msg_guide_sendimg.format(size[art_type]))
#     else:
#         bot.send_message(chat, msg_nan)


@bot.message_handler(content_types=['text'])
def functions(message):
    global art_type

    if message.text == cmd_create_shade:
        art_type = 'shade'
        bot.send_message(chat, msg_guide_sendimg.format(size[art_type]))

    if message.text == cmd_create_line:
        art_type = 'line'
        bot.send_message(chat, msg_guide_sendimg.format(size[art_type]))

    elif message.text == cmd_premade:
        bot.send_message(chat, msg_wip)

    elif message.text == cmd_goose:
        with open('goose.txt', encoding='utf8') as goose:
            goose = goose.read()
        bot.send_message(chat, goose)


# тут он отправляет txt файл в ответ на картинку
@bot.message_handler(content_types=['photo'])
def send_art(message):
    sz = size[art_type]
    if message.caption:
        if message.caption.isdigit():
            sz = int(message.caption)
        else:
            bot.send_message(chat, msg_nan)

    with open('reply.txt', 'w', encoding='utf-8') as reply:
        reply.write('Image with size {}'.format(sz))

    with open('reply.txt', encoding='utf-8') as reply:
        if art_type == 'shade':
            bot.send_document(chat, reply)
        elif art_type == 'line':
            bot.send_document(chat, reply)
        else:
            bot.send_message(chat, msg_notype)


bot.polling(none_stop=True, interval=0)
