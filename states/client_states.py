from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    time = State()
    product = State()
    makeup = State()
    conformation = State()
