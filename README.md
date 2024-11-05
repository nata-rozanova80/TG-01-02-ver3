# TG-01-02-ver3
Попытка 3 сделать заново, чтоб все устанавливалось


@dp.message(Command('photo'))
async def photo(message: Message):
		list = [ссылки URL на изображения через запятую]
		rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')