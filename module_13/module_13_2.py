from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import  asyncio


api ='7820157324:AAHk001jw7DJpUX0Tp2sVPx63VxBRioAa-s'
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massage(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
