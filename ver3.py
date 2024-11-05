import os
from gtts import gTTS
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from googletrans import Translator
from aiogram.types import Message, FSInputFile
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

@dp.message(Command('translate'))
async def translate(message: Message, self=None):
    text_to_translate = message.text.removeprefix('/translate').strip()
    print(text_to_translate)
   

    if not text_to_translate:
        await message.reply("Пожалуйста, укажите текст для перевода после команды.")
        return

    translated = translator.translate(text_to_translate, dest='en')
    trans_text = translated.text

    await bot.send_chat_action(message.chat.id, 'upload_audio')

    tts = gTTS(text=trans_text, lang='en')
    tts.save("text_to_translate.mp3")

    audio = FSInputFile("text_to_translate.mp3")
    await bot.send_audio(message.chat.id, audio)

    os.remove("text_to_translate.mp3")

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("1.ogg")
    await message.answer_voice(voice)

@dp.message(Command('photo'))
async def photo(message: Message):
    list_photos = ['https://isrscience.ru/wp-content/uploads/2019/11/Very_tall_trees_02.jpg', 'https://notivory.com/upload/medialibrary/3ed/3edf3e212c5f4cf1662cbfc44cab2fea.jpg']
    rand_photo = random.choice(list_photos)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    responses = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(responses)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('ИИ, или искусственный интеллект, представляет собой область компьютерных наук, которая занимается созданием систем, способных выполнять задачи, требующие человеческого интеллекта.')

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
