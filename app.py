from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import database_of_students
from config import BOT_TOKEN
from database import DateTime
from keyboards.choosing_classes import classes_markup
from states.state_1 import State_for_classes

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await State_for_classes.class_.set()

    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=classes_markup)


@dp.message_handler(state=State_for_classes.class_)
async def send_who_is_duty(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['class_'] = message.text

    await State_for_classes.next()

    date = DateTime()
    counter = date.function_for_correct_date()

    if data['class_'] == '11а':
        await message.reply(
            f"Сегодня дежурит {database_of_students.elevenA[counter][0]} {database_of_students.elevenA[counter][1]}",
            reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
