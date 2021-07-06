import logging

from aiogram import Bot, Dispatcher, executor, types

#уровень логов

logging.basicConfig(level=logging.INFO)

bot = Bot(token="1894033467:AAH_CGins3O2ajccm5bl87qsb9fGRinWFqs")
dp = Dispatcher(bot)

#Echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Amantay")

#Запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
