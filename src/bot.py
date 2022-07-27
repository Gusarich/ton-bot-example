from aiogram import Bot, Dispatcher, types
import logging
import config


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(commands=['start', 'help'])
async def handle_welcome(message: types.Message):
    await message.reply('''Hi!
I'm example bot made for this article.
My goal is to show how simple it is to receive payments in TonCoin with Python.

Use keyboard to test my functionality.''')


@dp.message()
async def handle_balance(message: types.Message):
    await message.answer('Your balance: 0.00 TON')


if __name__ == '__main__':
    dp.run_polling(bot)
