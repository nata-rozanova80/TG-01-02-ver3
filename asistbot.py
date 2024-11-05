import os
import telebot
from googletrans import Translator

from config import TOKEN
bot = telebot.TeleBot(TOKEN)
translator = Translator()

if not os.path.exists('img'):
    os.makedirs('img')


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(f'img/{file_info.file_path.split("/")[-1]}', 'wb') as new_file:
        new_file.write(downloaded_file)


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    translated = translator.translate(message.text, dest='en')
    bot.send_message(message.chat.id, translated.text)


@bot.message_handler(commands=['voice'])
def send_voice(message):
    voice = open('path_to_your_voice_message.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)
    voice.close()


bot.polling()
