# @TG01wetherbot or tg01bot

import os
from gtts import gTTS
import asyncio
#import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from googletrans import Translator
from aiogram.types import Message, FSInputFile
#from aiogram.utils import start_polling

from config import TOKEN
import random

# Инициализация бота и маршрутизатора
bot = Bot(token=TOKEN)
dp = Dispatcher()
# TELEGRAM_TOKEN = '7904269589:AAF_Cbn-HswNllR6O8J7obwgbWh59KxR5cI'  # Замените на ваш токен
# WEATHER_API_KEY = '18296f86db52c8ed138347556f734ec2'  # Замените на ваш ключ API для погоды
# CITY = 'Moscow'  # Замените на нужный город

@dp.message(Command('translate'))
async def translate(message: Message):
    trans_text = ['текст какой-то']
    # await message.answer(voice)
    tts = gTTS(text=trans_text, lang='en')
    tts.save("text_to_tras.mp3")
    audio = FSInputFile("text_to_tras.mp3")
    await bot.send_audio(message.chat.id, audio)
    os.remove("text_to_tras.mp3")


translator = Translator()


@dp.message(Command('translate'))
async def translate(message: Message):
    # Получаем текст сообщения от пользователя, убираем команду '/translate'
    text_to_translate = message.text.removeprefix('/translate').strip()

    if not text_to_translate:
        await message.reply("Пожалуйста, укажите текст для перевода после команды.")
        return

    # Переводим текст на английский
    translated = translator.translate(text_to_translate, dest='en')
    trans_text = translated.text
    await bot.send_chat_action(message.chat.id, 'upload_video')

    # Создаем аудиофайл из переведенного текста
    with open('output_file.mp3', 'wb') as f:
        tts = gTTS(text=trans_text, lang='en')
        tts.write_to_fp(f)
        #tts.save("text_to_translate.mp3")

    # Отправляем аудиофайл
    audio = FSInputFile("text_to_translate.mp3")
    await bot.send_audio(message.chat.id, audio)

    # Удаляем временный аудиофайл
    os.remove("text_to_translate.mp3")


@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("1.ogg")
    await message.answer_voice(voice)


@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://isrscience.ru/wp-content/uploads/2019/11/Very_tall_trees_02.jpg', 'https://notivory.com/upload/medialibrary/3ed/3edf3e212c5f4cf1662cbfc44cab2fea.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')


@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('ИИ, или искусственный интеллект, представляет собой область компьютерных наук, которая занимается созданием систем, способных выполнять задачи, требующие человеческого интеллекта. Эти задачи могут включать в себя понимание естественного языка, распознавание образов, принятие решений и обучение.')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')




@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Селеметсiз бе, {message.from_user.first_name}')

@dp.message()
async def startall(message: Message):
    await message.answer("Я тебе ответил")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())




