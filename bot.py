import telebot
from telebot import types
from io import BytesIO, StringIO
from gen_shading import gen_shading
from PIL import Image
import pandas as pd

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

token = open('token.txt').read()[:-1]
bot = telebot.TeleBot(token)
# токен бота; в телеге t.me/ASCIIArt_project_bot


df = pd.DataFrame()


# старт и кнопочки
@bot.message_handler(commands=['start'])
def start(message):
    global df
    if message.from_user.id not in df.index:
        row = pd.DataFrame({'type': '', 'shade_size': 50, 'line_size': 50}, index=[message.from_user.id])
        df = pd.concat([df, row])
        
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cmd in [cmd_create_shade, cmd_create_line, cmd_premade, cmd_goose]:
        markup.add(types.KeyboardButton(cmd))
    bot.send_message(message.from_user.id, msg_init, reply_markup=markup)


@bot.message_handler(content_types=['text'], func=lambda message: message.from_user.id in df.index)
def functions(message):

    if message.text == cmd_create_shade:
        df.at[message.from_user.id, 'type'] = 'shade'
        bot.send_message(message.from_user.id, msg_guide_sendimg.format(str(df.at[message.from_user.id, 'shade_size'])))

    if message.text == cmd_create_line:
        df.at[message.from_user.id, 'type'] = 'line'
        bot.send_message(message.from_user.id, msg_guide_sendimg.format(str(df.at[message.from_user.id, 'line_size'])))

    elif message.text == cmd_premade:
        bot.send_message(message.from_user.id, msg_wip)

    elif message.text == cmd_goose:
        with open('files/goose.txt', encoding='utf8') as goose:
            goose = goose.read()
        bot.send_message(message.from_user.id, goose)


# тут он отправляет txt файл в ответ на картинку
@bot.message_handler(content_types=['photo'], func=lambda message: message.from_user.id in df.index)
def send_art(message):
    if df.at[message.from_user.id, 'type'] == '':
        bot.send_message(message.from_user.id, msg_notype)
    else:
        if message.caption:
            if message.caption.isdigit():
                df.at[message.from_user.id, str(df.at[message.from_user.id, 'type']) + '_size'] = int(message.caption)
            else:
                bot.send_message(message.from_user.id, msg_nan)

    file = bot.download_file(bot.get_file(message.photo[-1].file_id).file_path)
    img = BytesIO(file)

    if df.at[message.from_user.id, 'type'] == 'shade':
        bot.send_document(message.from_user.id, StringIO(gen_shading(img, width=df.at[message.from_user.id, 'shade_size'])), visible_file_name='art.txt')
    elif df.at[message.from_user.id, 'type'] == 'line':
        bot.send_message(message.from_user.id, msg_wip)
    else:
        bot.send_message(message.from_user.id, msg_notype)


bot.polling(none_stop=True, interval=0)


if df.shape[0] >= 50:
    df = df.drop(df.index[0])
