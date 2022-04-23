from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

import os

from translate import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот в сети')

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message, users=None):
    try:
    await bot.send_message(
        if message.chat.id in users:
            users.remove(message.chat.id);
    translator = Translator(to_lang="Russian");
    translation = translator.translate(message.text);
    await bot.send_message(message.chat.id, translation);

        elif message.text == '🇬🇧Перевод🇷🇺';
    users.append(message.chat.id);
    bot.send_message(message.chat.id, 'Введи мне текст на Английском языке'), 'Напишите слово или предложение и я вам его переведу!')
        await message.delete()
    except:

        await message.reply('Для подключения бота, напишите ему: \nhttps://t.me/tul_trans_bot')

@dp.message_handler(commands=['How_it_works'])
async def command_start(message : types.Message):
        await bot.send_message(message.from_user.id, 'You can enter you a word or sentence and bot translate it')
        await message.delete()

@dp.message_handler(commands=['Developers'])
async def command_start(message : types.Message):
        await bot.send_message(message.from_user.id, 'Бот был разработан молодыми разработчиками из Тулы. Тимур, Лера, Даня, Вова. TulaHack2022 ')
        await message.delete()

@dp.message_handler()
async def echo_send(message : types.Message):
    #await message.answer(message.text)
    await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)