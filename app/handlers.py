import app.keyboards as kb
import app.database.requests as rq

from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply('Сервис таңдаңыз', reply_markup=kb.main_kz)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Список команд:\n/get_photo\n/get_user_id')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMHZm69hGz90LsvZ2piSUDJJtwztC0AAobdMRvKrXhLmdrEZfhwy_UBAAMCAAN4AAM1BA', caption='Это аватарка Акжола')


@router.message(Command('get_user_id'))
async def get_user_id(message: Message):
    await message.answer(f'Ваше ID: {message.from_user.id}')
    
    
@router.message(F.text == 'Калькулятор📝')
async def calculator_kz(message: Message):
    await message.answer('Сіз нені есептегіңіз келеді?', reply_markup=kb.calculator_kz)
    
    
@router.message(F.text == '📏 Орташа баға')
async def avg_kz(message: Message):
    await message.answer('Сіз нені есептегіңіз келеді?', reply_markup=kb.avg_kz)
    
    
@router.message(F.text == '📌 Рейтинг')
async def rating_kz(message: Message):
    await message.answer('Сіздің апталық бағаңыздың орташа баллын енгізіңіз (Егер бағаңыз толық болмаса, нүкте қою арқылы жазыңыз. Мысалы: 85.33)', reply_markup=kb.back_kz)
    
    
@router.message(F.text == '🇰🇿 Тіл 🇷🇺')
async def choose_language(message: Message):
    await message.answer('Тіл таңдаңыз / Выберите язык', reply_markup=kb.language)
    

@router.message(F.text == 'KZ')
async def kazakh(message: Message):
    await message.answer('Сіз қазақ тілін таңдадыңыз', reply_markup=kb.main_kz)
    
    
@router.message(F.text == 'RU')
async def russian(message: Message):
    await message.answer('Вы выбрали русский язык', reply_markup=kb.main_ru)
    
    
@router.message(F.text == 'Прак/CРО 📝')
async def prac_sro_kz(message: Message):
    await message.answer('Барлық ПРАКТИКА бағаларын бос орын арқылы немесе үтір арқылы енгізіңіз (н.п. енгізбеңіз!, н.я.= 0 ретінде саналады)', reply_markup=kb.back_kz)
    
    
@router.message(F.text == '◀️ Артқа ◀️')
async def back_kz(message: Message):
    await message.answer('Сервис таңдаңыз', reply_markup=kb.main_kz)   


@router.message(F.text == '◀️ Меню ◀️')
async def menu_kz(message: Message):
    await message.answer('Сервис таңдаңыз', reply_markup=kb.main_kz)       
    
    
@router.message(F.text == '❓ Көмек ❓')
async def help_kz(message: Message):
    await message.answer('Көмек қажет категорияны таңдаңыз', reply_markup=kb.help_kz)
    
    
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.number)
    await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)
    

@router.message(Reg.number, F.contact)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.contact.first_name)
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена.\nИмя: {data['name']}\nНомер: {data['number']}')
    await state.clear()
       
    