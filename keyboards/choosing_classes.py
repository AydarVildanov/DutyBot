from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

classes_markup = ReplyKeyboardMarkup(resize_keyboard=True)

classes_markup.add(
    KeyboardButton("5а"), KeyboardButton("5б"), KeyboardButton("6а"), KeyboardButton("7а"), KeyboardButton("8а"),
    KeyboardButton("8б"), KeyboardButton("9а"), KeyboardButton("9б"), KeyboardButton("10а"), KeyboardButton("11а"),
    KeyboardButton("11б")
)


