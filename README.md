# TG-01-02-ver3
(Учебный проект для Zerocoder. Уроки TG-01-02)
Попытка 3 сделать заново, чтоб все устанавливалось


@dp.message(Command('photo'))
async def photo(message: Message):
		list = [ссылки URL на изображения через запятую]
		rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

Для отправки тяжелых файлов, процесс может занять время. Чтобы пользователь видел, что бот не завис, можно прописать уведомление о загрузке. Для этого вернемся к фрагменту кода для отработки видео и после вызова асинхронной функции укажем:

await bot.send_chat_action(message.chat.id, 'upload_video')
Это уведомление покажет, что бот загружает видео. Когда загрузка завершится, уведомление исчезнет.



start - запуск бота
help - помощь в рвботе
photo - сохранение присланного фото
voice - прием звукового сообщения
translate - перевод сообщения пользователя
