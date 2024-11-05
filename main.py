# @TG01wetherbot or tg01bot

#import os
import asyncio
#import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message
#from aiogram.utils import start_polling

from config import TOKEN
import random

# Инициализация бота и маршрутизатора
bot = Bot(token=TOKEN)
dp = Dispatcher()
# TELEGRAM_TOKEN = '7904269589:AAF_Cbn-HswNllR6O8J7obwgbWh59KxR5cI'  # Замените на ваш токен
# WEATHER_API_KEY = '18296f86db52c8ed138347556f734ec2'  # Замените на ваш ключ API для погоды
# CITY = 'Moscow'  # Замените на нужный город




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


# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer('Привет! Я маленький бот.')

# def get_weather(city: str) -> str:
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     data = response.json()
#
#     if response.status_code == 200:
#         temperature = data['main']['temp']
#         description = data['weather'][0]['description']
#         return f"Температура в {city}: {temperature}°C, {description}."
#     else:
#         return "Город не найден."
#
#
# @router.message(Command("weather"))
# async def weather_command(message: types.Message):
#     weather_info = get_weather(CITY)
#     await message.answer(weather_info)

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




