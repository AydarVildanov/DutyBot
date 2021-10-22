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


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        await State_for_classes.class_.set()

        await message.reply("Приветствую вас, пожалуйста, выберите свой класс", reply_markup=classes_markup)

    except Exception as error:
        print("Ошибка в send_welcome")


@dp.message_handler(state=State_for_classes.class_)
async def send_who_is_duty(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['class_'] = message.text

        await State_for_classes.next()

        date = DateTime()
        counter = date.function_for_correct_date()

        if data['class_'] == '5а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.fiveA[counter % len(database_of_students.fiveA)][0]} "
                f"{database_of_students.fiveA[counter % len(database_of_students.fiveA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '5б':
            await message.reply(
                f"Сегодня дежурит {database_of_students.fiveB[counter % len(database_of_students.fiveB)][0]} "
                f"{database_of_students.fiveB[counter % len(database_of_students.fiveB)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '6а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.sixA[counter % len(database_of_students.sixA)][0]} "
                f"{database_of_students.sixA[counter % len(database_of_students.sixA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '7а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.sevenA[counter % len(database_of_students.sevenA)][0]} "
                f"{database_of_students.sevenA[counter % len(database_of_students.sevenA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '8а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.eightA[counter % len(database_of_students.eightA)][0]} "
                f"{database_of_students.eightA[counter % len(database_of_students.eightA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '8б':
            await message.reply(
                f"Сегодня дежурит {database_of_students.eightB[counter % len(database_of_students.eightB)][0]} "
                f"{database_of_students.eightB[counter % len(database_of_students.eightB)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '9а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.nineA[counter % len(database_of_students.nineA)][0]} "
                f"{database_of_students.nineA[counter % len(database_of_students.nineA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '9б':
            await message.reply(
                f"Сегодня дежурит {database_of_students.nineB[counter % len(database_of_students.nineB)][0]} "
                f"{database_of_students.nineB[counter % len(database_of_students.nineB)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '10а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.tenA[counter % len(database_of_students.tenA)][0]} "
                f"{database_of_students.tenA[counter % len(database_of_students.tenA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '11а':
            await message.reply(
                f"Сегодня дежурит {database_of_students.elevenA[counter % len(database_of_students.elevenA)][0]} "
                f"{database_of_students.elevenA[counter % len(database_of_students.elevenA)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        elif data['class_'] == '11б':
            await message.reply(
                f"Сегодня дежурит {database_of_students.elevenB[counter % len(database_of_students.elevenB)][0]} "
                f"{database_of_students.elevenB[counter % len(database_of_students.elevenB)][1]}",
                reply_markup=types.ReplyKeyboardRemove())

        else:
            await message.reply(f"Такого класса не существует, пожалуйста, выберите нужный класс")


    except Exception as error:
        print("Ошибка в send_who_is_duty")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
