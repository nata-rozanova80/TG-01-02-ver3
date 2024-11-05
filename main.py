# @TG01wetherbot or tg01bot

#import os
import asyncio
#import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message
#from aiogram.utils import start_polling

from config import TOKEN

# Инициализация бота и маршрутизатора
bot = Bot(token=TOKEN)
dp = Dispatcher()
# TELEGRAM_TOKEN = '7904269589:AAF_Cbn-HswNllR6O8J7obwgbWh59KxR5cI'  # Замените на ваш токен
# WEATHER_API_KEY = '18296f86db52c8ed138347556f734ec2'  # Замените на ваш ключ API для погоды
# CITY = 'Moscow'  # Замените на нужный город






@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('ИИ, или искусственный интеллект, представляет собой область компьютерных наук, которая занимается созданием систем, способных выполнять задачи, требующие человеческого интеллекта. Эти задачи могут включать в себя понимание естественного языка, распознавание образов, принятие решений и обучение.')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Я маленький бот.')

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



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())




