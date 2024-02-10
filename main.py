import asyncio
import logging
import os
import sys

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
# -------
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, StateFilter, state, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
# -------
from registration import *
from task import *

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = os.environ.get("TOKEN")
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


class BotStates(StatesGroup):
    """
    Состояния телеграм бота
    """
    get_surname = State()
    get_name = State()
    # ----
    get_service_name = State()
    get_description = State()


def create_keyboard(buttons: list):
    """
    -> Создание клавиатуры
    :param buttons: Список с названиями кнопок
    :return: keyboard - экземпляр клавы
    """
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text=button)] for button in buttons])
    return keyboard


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    -> Хендлер для регистрации пользователей
    """
    if check_user_db(message.from_user.id):
        await message.answer('Вы уже зарегистрированы!\n/menu - для выбора сервиса')
    else:
        await message.answer('Здравствуйте! Вам необходимо пройти регистрацию.\nВведите Вашу фамилию:')
        await state.set_state(BotStates.get_surname)


@dp.message(Command(commands=["menu"]))
async def menu_handler(message: Message, state: FSMContext):
    """
    -> Хендлер для создания заявок
    -> Запрашиваем у пользователя сервис
    """
    if check_user_db(message.from_user.id):
        services_list = get_services_db()
        await message.answer('Выберете сервис:', reply_markup=create_keyboard(services_list))
        await state.set_state(BotStates.get_service_name)
    else:
        await message.answer('Здравствуйте! Вам необходимо пройти регистрацию.\nВведите Вашу фамилию:')
        await state.set_state(BotStates.get_surname)


@dp.message(Command(commands=["tasklist"]))
async def tasklist_handler(message: Message, state: FSMContext):
    """
    -> Хендлер для получения списка заявок
    """
    if check_user_db(message.from_user.id):
        tasklist = get_tasklist_db(message.from_user.id)
        if tasklist:
            for task in tasklist:
                task_number = task[0]
                service_name = task[1]
                task_date = task[2]
                creator_name = task[3]
                task_description = task[4]
                await message.answer(f'<b>Заявка</b> {task_number}\n'
                                     f'<b>Создана</b>: {creator_name}\n'
                                     f'<b>Сервис</b>: {service_name}\n'
                                     f'<b>Описание</b>: {task_description}')
        else:
            await message.answer('У Вас еще нет созданных заявок', parse_mode=ParseMode.HTML)
    else:
        await message.answer('Здравствуйте! Вам необходимо пройти регистрацию.\nВведите Вашу фамилию:')
        await state.set_state(BotStates.get_surname)


@dp.message(BotStates.get_surname)
async def user_surname_handler(message: Message, state: FSMContext):
    """
    -> Хендлер для регистрации пользователей
    -> Получаем фамилию
    """
    await state.update_data(usersurname=message.text)
    await message.answer('Введите Ваше имя:')
    await state.set_state(BotStates.get_name)


@dp.message(BotStates.get_name)
async def user_name_handler(message: Message, state: FSMContext):
    """
    -> Хендлер для регистрации пользователей
    -> Получаем имя
    """
    await state.update_data(username=message.text)
    await state.update_data(tgid=message.from_user.id)
    state_data = await state.get_data()
    print(f'{state_data=}')
    registrate_user(state_data)
    await message.answer('Регистрация прошла успешно!\n/menu - для выбора сервиса')
    await state.clear()


@dp.message(BotStates.get_service_name)
async def service_name_handler(message: Message, state: FSMContext):
    """
    -> Хендлер для создания заявок
    -> Получаем имя сервиса
    """
    await state.update_data(servicename=message.text)
    await message.answer('Введите описание заявки:')
    await state.set_state(BotStates.get_description)


@dp.message(BotStates.get_description)
async def task_description_handler(message: Message, state: FSMContext):
    """
    -> Хендлер для создания заявок
    -> Получаем описание заявки
    """
    await state.update_data(taskdescription=message.text)
    await state.update_data(tgid=message.from_user.id)
    create_task(await state.get_data())
    await message.answer('Заявка успешно создана!')
    await state.clear()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
