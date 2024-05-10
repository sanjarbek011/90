import os
import sqlite3

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
load_dotenv()
from database import registruser

bot = Bot(os.getenv('apitoken'))
dp = Dispatcher(bot)

knopka = ReplyKeyboardMarkup(resize_keyboard=True)
knopka.add(
    KeyboardButton(text='Asosiy menu')
)

kanalbutton = InlineKeyboardMarkup()
kanalbutton.add(
    InlineKeyboardButton(text='Bagdad IT Academy', url='https://t.me/bagdaditacademy')
)







CHANNEL = '@bagdaditacademy'

@dp.message_handler(commands='start')
async def start(message: Message):

    fullname = message.from_user.full_name
    username = message.from_user.username
    chatid = message.chat.id

    check = await bot.get_chat_member(CHANNEL, chatid)
    if check.status == 'left':
        await bot.send_message(chat_id=chatid, text='Siz kanalga azo bolmagansiz', reply_markup=kanalbutton)
    else:

        database = sqlite3.connect('baza.sqlite')
        cursor = database.cursor()
        cursor.execute('''SELECT chatid FROM users WHERE chatid = ?''', (chatid, ))
        user = cursor.fetchone()
        if not user:
            registeruser(full_name=fullname, user_name=username, chat_id=chatid)
        await bot.send_message(chat_id=chatid, text='Xush kelibsiz', reply_markup=knopka)




executor.start_polling(dp, skip_updates=True)





