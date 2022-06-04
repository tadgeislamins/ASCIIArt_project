import telebot
from telebot import types
from io import BytesIO, StringIO
from gen_shading import gen_shading
import pandas as pd

cmd_create_shade = 'Создать тональный ASCII-арт'
cmd_create_line = 'Создать контурный ASCII-арт'
cmd_goose = 'Запустить гуся'
cmd_chars = 'Настроить список символов'

msg_init = 'Что вы хотите сделать?'
msg_guide_start = 'Чтобы начать работу, напишите /start.'
msg_guide_sendimg = 'Пожалуйста, отправьте картинку. Можете указать желаемую ширину арта (по умолчанию {}).'
msg_guide_chars = 'Введите в строку все символы, которые вы хотели бы использовать в тональных артах. Сейчас используются {}\n\nЧтобы восстановить значение по умолчанию, напишите /reset.'
msg_sizeset = 'Принято! Теперь ширина таких артов будет {}.'
msg_charset = 'Теперь тональные арты будут создаваться из символов {}.'
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
        row = pd.DataFrame({'type': '', 'shade_size': 50, 'line_size': 50, 'chars': ''.join([chr(i) for i in range(32, 127)])}, index=[message.from_user.id])
        df = pd.concat([df, row])
    else:
        df.at[message.from_user.id, 'type'] = ''

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for cmd in [cmd_create_shade, cmd_create_line, cmd_goose, cmd_chars]:
        markup.add(types.KeyboardButton(cmd))
    bot.send_message(message.from_user.id, msg_init, reply_markup=markup)


@bot.message_handler(content_types=['text'], func=lambda message: message.from_user.id in df.index)
def functions(message):
    if message.text == cmd_create_shade:
        df.at[message.from_user.id, 'type'] = 'shade'
        bot.send_message(message.from_user.id, msg_guide_sendimg.format(str(df.at[message.from_user.id, 'shade_size'])))

    elif message.text == cmd_create_line:
        df.at[message.from_user.id, 'type'] = ''
        bot.send_message(message.from_user.id, msg_wip)

    elif message.text == cmd_goose:
        with open('files/goose.txt', encoding='utf8') as goose:
            goose = goose.read()
        df.at[message.from_user.id, 'type'] = ''
        bot.send_message(message.from_user.id, goose)

    elif message.text == cmd_chars:
        df.at[message.from_user.id, 'type'] = 'charsetting'
        bot.send_message(message.from_user.id, msg_guide_chars.format(df.at[message.from_user.id, 'chars']))

    elif df.at[message.from_user.id, 'type'] == 'charsetting':
        if message.text == '/reset':
            df.at[message.from_user.id, 'chars'] = ''.join([chr(i) for i in range(33, 127)])
        else:
            df.at[message.from_user.id, 'chars'] = ''.join((set(message.text)))
        df.at[message.from_user.id, 'type'] = ''
        bot.send_message(message.from_user.id, msg_charset.format(df.at[message.from_user.id, 'chars']))


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
        bot.send_document(message.from_user.id, StringIO(gen_shading(img, chlist=df.at[message.from_user.id, 'chars'], width=df.at[message.from_user.id, 'shade_size'])), visible_file_name='art.txt')
    else:
        bot.send_message(message.from_user.id, msg_notype)


@bot.message_handler()
def not_started(message):
    bot.send_message(message.from_user.id, msg_guide_start)


bot.polling(none_stop=True, interval=0)


if df.shape[0] >= 50:
    df = df.drop(df.index[0])
