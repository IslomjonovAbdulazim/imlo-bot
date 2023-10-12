import logging
from aiogram import Bot, Dispatcher, executor, types
from check_word import check_word

API_TOKEN = "6553659526:AAENRZ02Y2T96q3ErAC4SYdfK-HmoXH0B3c"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("uz-imlo botga xush kelibsiz!")


@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z yuboring")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word_list = message.text.split()
    for word in word_list:
        result = check_word(word)
        if result['available']:
            response = f"correct: {word.capitalize()}"
        else:
            response = f"incorrect: {word.capitalize()}\n"
            for text in result['matches']:
                response += f"{text.capitalize()}\n"
        await message.answer(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)