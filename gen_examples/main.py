from aiogram.fsm.state import StatesGroup, State
from aiogram import F, Router, Bot, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import get_tg_api_token

#импорт модулей проекта
from database.main import Database
from gen_examples.examples import Examples


#импорт клавиатуры
from gen_examples.keyboard import ExampleKeyboard


router = Router()

bot = Bot(token=get_tg_api_token())

db = Database('gen example')
training_db = {}


class UsersState(StatesGroup):
    training_plus = State()
    training_minus = State()
    training_multi = State()
    training_division = State()




@router.message(F.text == 'Мой уровень')
async def get_level(message: types.Message, state:FSMContext):


    levels = db.select_levels(chat_id=message.chat.id)

    mes = f"""Ваши уровни:\n
Сложение: {levels[0]}
Вычитание: {levels[1]}
Умножение: {levels[2]}
Деление: {levels[3]}"""

    await message.answer(mes)







@router.message(F.text == '/start')
async def start(message: types.Message, state:FSMContext):

    """первое знакомство с пользователем"""

    db.insert_user(message.chat.id)

    await message.answer('Здравствуй дорогой друг, этот бот создан чтобы помочь тебе отточить твои навыки в математике.', reply_markup=ExampleKeyboard.start_keyboard())








@router.message(F.text == 'Тренировка')
async def training(message: types.Message, state:FSMContext):

    """Включает режим тренировка"""
    await message.answer("Тренировка", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите что вы хотели бы потренировать", reply_markup=ExampleKeyboard.training())




#============================== plus ===========================================

@router.callback_query(F.data == 'tr_plus')
async def plus(call: types.CallbackQuery, state:FSMContext):

    if not call.message.chat.id in training_db.keys():
        await bot.send_message(call.message.chat.id, "Вы в тренировке сложения")
        training_db[call.message.chat.id] = {'level':1, 'answer':''}

    example, answer = Examples.plus(training_db[call.message.chat.id]['level'])

    training_db[call.message.chat.id]['answer'] = answer

    await bot.send_message(call.message.chat.id, example, reply_markup=ExampleKeyboard.stop())
    await call.message.edit_reply_markup()
    await state.set_state(UsersState.training_plus)






@router.message(UsersState.training_plus)
async def plus_answer(message: types.Message, state:FSMContext):

    if message.text == 'Закончить':
        result = training_db[message.chat.id]['level']
        if int(db.select_levels(message.chat.id)[0]) < int(result): db.update_user(message.chat.id, level_plus=int(result))
        await state.clear()
        training_db[message.chat.id] = {'level':1, 'answer':''}
        return message.answer("Вы вышли в основное меню", reply_markup=ExampleKeyboard.start_keyboard())

    if message.text == training_db[message.chat.id]['answer']:
        await message.answer("Правильно!!!")
        training_db[message.chat.id]['level'] += 1

    else:
        await message.answer("Неправильно(((")

    example, answer = Examples.plus(training_db[message.chat.id]['level'])
    example = f"Уровень {training_db[message.chat.id]['level']}\n"+example
    training_db[message.chat.id]['answer'] = answer

    await message.answer(example)








#================================================== minus ========================================================
@router.callback_query(F.data == 'tr_minus')
async def minus(call: types.CallbackQuery, state:FSMContext):

    if not call.message.chat.id in training_db.keys():
        await bot.send_message(call.message.chat.id, "Вы в тренировке вычитания")
        training_db[call.message.chat.id] = {'level':1, 'answer':''}

    example, answer = Examples.minus(training_db[call.message.chat.id]['level'])

    training_db[call.message.chat.id]['answer'] = answer

    await bot.send_message(call.message.chat.id, example, reply_markup=ExampleKeyboard.stop())
    await call.message.edit_reply_markup()
    await state.set_state(UsersState.training_minus)






@router.message(UsersState.training_minus)
async def plus_answer(message: types.Message, state:FSMContext):

    if message.text == 'Закончить':
        result = training_db[message.chat.id]['level']
        if int(db.select_levels(message.chat.id)[1]) < int(result): db.update_user(message.chat.id, level_minus=int(result))
        await state.clear()
        training_db[message.chat.id] = {'level':1, 'answer':''}
        return message.answer("Вы вышли в основное меню", reply_markup=ExampleKeyboard.start_keyboard())

    if message.text == training_db[message.chat.id]['answer']:
        await message.answer("Правильно!!!")
        training_db[message.chat.id]['level'] += 1

    else:
        await message.answer("Неправильно(((")

    example, answer = Examples.minus(training_db[message.chat.id]['level'])
    example = f"Уровень {training_db[message.chat.id]['level']}\n"+example
    training_db[message.chat.id]['answer'] = answer

    await message.answer(example)








#===================================== multi ============================================

@router.callback_query(F.data == 'tr_multi')
async def minus(call: types.CallbackQuery, state:FSMContext):

    if not call.message.chat.id in training_db.keys():
        await bot.send_message(call.message.chat.id, "Вы в тренировке умножения")
        training_db[call.message.chat.id] = {'level':1, 'answer':''}

    example, answer = Examples.multi(training_db[call.message.chat.id]['level'])

    training_db[call.message.chat.id]['answer'] = answer

    await bot.send_message(call.message.chat.id, example, reply_markup=ExampleKeyboard.stop())
    await call.message.edit_reply_markup()
    await state.set_state(UsersState.training_multi)






@router.message(UsersState.training_multi)
async def plus_answer(message: types.Message, state:FSMContext):

    if message.text == 'Закончить':
        result = training_db[message.chat.id]['level']
        if int(db.select_levels(message.chat.id)[2]) < int(result): db.update_user(message.chat.id, level_mult=int(result))
        await state.clear()
        training_db[message.chat.id] = {'level':1, 'answer':''}
        return message.answer("Вы вышли в основное меню", reply_markup=ExampleKeyboard.start_keyboard())


    if message.text == training_db[message.chat.id]['answer']:
        await message.answer("Правильно!!!")
        training_db[message.chat.id]['level'] += 1

    else:
        await message.answer("Неправильно(((")

    example, answer = Examples.multi(training_db[message.chat.id]['level'])
    example = f"Уровень {training_db[message.chat.id]['level']}\n"+example
    training_db[message.chat.id]['answer'] = answer

    await message.answer(example)







#========================================== division ===========================================

@router.callback_query(F.data == 'tr_division')
async def minus(call: types.CallbackQuery, state:FSMContext):

    if not call.message.chat.id in training_db.keys():
        await bot.send_message(call.message.chat.id, "Вы в тренировке деления")
        training_db[call.message.chat.id] = {'level':1, 'answer':''}

    example, answer = Examples.division(training_db[call.message.chat.id]['level'])

    training_db[call.message.chat.id]['answer'] = answer

    await bot.send_message(call.message.chat.id, example, reply_markup=ExampleKeyboard.stop())
    await call.message.edit_reply_markup()
    await state.set_state(UsersState.training_division)






@router.message(UsersState.training_division)
async def plus_answer(message: types.Message, state:FSMContext):

    if message.text == 'Закончить':
        result = training_db[message.chat.id]['level']
        if int(db.select_levels(message.chat.id)[3]) < int(result): db.update_user(message.chat.id, level_division=int(result))
        await state.clear()
        training_db[message.chat.id] = {'level':1, 'answer':''}
        return message.answer("Вы вышли в основное меню", reply_markup=ExampleKeyboard.start_keyboard())


    if message.text == training_db[message.chat.id]['answer']:
        await message.answer("Правильно!!!")
        training_db[message.chat.id]['level'] += 1

    else:
        await message.answer("Неправильно(((")

    example, answer = Examples.division(training_db[message.chat.id]['level'])
    example = f"Уровень {training_db[message.chat.id]['level']}\n"+example
    training_db[message.chat.id]['answer'] = answer

    await message.answer(example)

