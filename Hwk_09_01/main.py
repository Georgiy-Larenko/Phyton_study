
from telebot import telebot, TeleBot, types
from telebot import types
import logger as lg
import emoji

TOKEN = ''

bot = telebot.TeleBot(TOKEN)


value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
             telebot.types.InlineKeyboardButton('C', callback_data = 'C'),
             telebot.types.InlineKeyboardButton('<=', callback_data = '<='),
             telebot.types.InlineKeyboardButton('/', callback_data = '/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data = '7'),
             telebot.types.InlineKeyboardButton('8', callback_data = '8'),
             telebot.types.InlineKeyboardButton('9', callback_data = '9'),
             telebot.types.InlineKeyboardButton('*', callback_data = '*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data = '4'),
             telebot.types.InlineKeyboardButton('5', callback_data = '5'),
             telebot.types.InlineKeyboardButton('6', callback_data = '6'),
             telebot.types.InlineKeyboardButton('-', callback_data = '-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data = '1'),
             telebot.types.InlineKeyboardButton('2', callback_data = '2'),
             telebot.types.InlineKeyboardButton('3', callback_data = '3'),
             telebot.types.InlineKeyboardButton('+', callback_data = '+'))

keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data = 'no'),
             telebot.types.InlineKeyboardButton('0', callback_data = '0'),
             telebot.types.InlineKeyboardButton(',', callback_data = '.'),
             telebot.types.InlineKeyboardButton('=', callback_data = '='))

@bot.message_handler(commands=['start'])
def getMessage(msg):
    bot.send_message(msg.chat.id, 'Привет, *' + msg.from_user.first_name +'* !\nЭто стандартный калькулятор.\nДумаю в объяснении не нуждается.' + '\U0001f609' + '\nПриятного пользования.' + '\U0001f64f'
    + '\nДля отправки лога введите /log.')
    lg.logging.info(f'User * {msg.from_user.first_name} ({msg.from_user.id}) * starting program')

    global value
    if value == '':
        bot.send_message(msg.from_user.id, '0', reply_markup = keyboard)
    else:
        bot.send_message(msg.from_user.id, value, reply_markup = keyboard)
    lg.logging.info(f'User * {msg.from_user.first_name} ({msg.from_user.id}) * send: {keyboard.row}')   


@bot.message_handler(commands=['start'])
def send_welcome(message):
    doc = open(r'Homework\Hwk_09_01\loglist.log', 'rb')
    bot.send_document(message.from_user.id, doc)
    doc.close()
    
    

@bot.callback_query_handler(func = lambda call: True)

def callback_func(query):

    global value, old_value
    data = query.data

    if data == 'no':
        pass

    elif data == 'C':
        value = ''

    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]

    elif data == '=':
        value = str(eval(value))

    else:
        value += data

    if value != old_value:

        if value == '':
            bot.edit_message_text(chat_id = query.message.chat.id, message_id = query.message.id, text = '0', reply_markup = keyboard)
            
        else:
            bot.edit_message_text(chat_id = query.message.chat.id, message_id = query.message.id, text = value, reply_markup = keyboard)
        old_value = value  


print('Calculator start')
bot.infinity_polling()