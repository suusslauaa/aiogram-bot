from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Калькулятор📝'), KeyboardButton(text='Контакт')]
], input_field_placeholder='Сервис таңдаңыз.', resize_keyboard=True)

main_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Калькулятор📝'), KeyboardButton(text='Контакт')]
], input_field_placeholder='Выберите сервис.', resize_keyboard=True)

calculator_kz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📏 Орташа баға'), KeyboardButton(text='📌 Рейтинг')],
    [KeyboardButton(text='📎 Емтихан'), KeyboardButton(text='❓ Көмек ❓')],
    [KeyboardButton(text='🇰🇿 Тіл 🇷🇺'), KeyboardButton(text='◀️ Меню ◀️')]
], input_field_placeholder='Сервис таңдаңыз.', resize_keyboard=True)

avg_kz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Лек/Прак/CРО 📝'), KeyboardButton(text='Лек/Прак/CРО/Лаб 📝'), KeyboardButton(text='Прак/CРО 📝')],
    [KeyboardButton(text='◀️ Артқа ◀️')]
], input_field_placeholder='Сервис таңдаңыз.', resize_keyboard=True)

back_kz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='◀️ Артқа ◀️')]
], resize_keyboard=True)

language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='KZ'), KeyboardButton(text='RU')]
], input_field_placeholder='Тіл таңдаңыз / Выберите язык', resize_keyboard=True)

help_kz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Орташа бағаны анықтау'), KeyboardButton(text='Рейтинг бағаны анықтау'), KeyboardButton(text='Емтихан бағаны анықтау')],
    [KeyboardButton(text='◀️ Артқа ◀️')]
], input_field_placeholder='Көмек қажет категорияны таңдаңыз.', resize_keyboard=True)

get_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер', request_contact=True)],
    [KeyboardButton(text='◀️ Назад ◀️')]
], input_field_placeholder='Выберите пункт меню.', resize_keyboard=True)
