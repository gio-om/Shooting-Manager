from aiogram import types, Dispatcher
from keyboards import inline_client_kb, tariff_kb, time_client_kb, product_client_kb, makeup_client_kb, \
    test_conformation_client_kb, miss_in_test_client_kb
from aiogram.dispatcher.filters import Text
from states import Test
import data
from aiogram.dispatcher import FSMContext
from create_bot import bot, manager_id


""" Start keyboard """


async def command_start(message: types.Message):
    await message.answer('Это бот для записи на съемки', reply_markup=inline_client_kb)


""" Answers to information request"""


async def call_info(callback: types.CallbackQuery):
    await callback.message.answer('Выберите тариф для более подробной информации о нем', reply_markup=tariff_kb)
    await callback.answer()


async def call_description(callback: types.CallbackQuery):
    await callback.message.answer(data.descriptions[callback.data])
    await callback.answer()


""" Answers to test request """


async def call_test(callback: types.CallbackQuery):
    await callback.message.answer('Сколько времени вы готовы уделить на съемку?', reply_markup=time_client_kb)
    await Test.time.set()
    await callback.answer()


async def command_test_time(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as answers_counter:
        answers_counter['simple_shooting'] = 0
        answers_counter['advanced_shooting'] = 0
        answers_counter['video_shooting'] = 0
        if answer == '/30_минут':
            answers_counter['simple_shooting'] += 1
        elif answer == '/1_час':
            answers_counter['advanced_shooting'] += 1
        else:
            answers_counter['video_shooting'] += 1

        print(answers_counter['simple_shooting'], answers_counter['advanced_shooting'],
              answers_counter['video_shooting'])

    await message.answer('Что вы хотите получить от съемки?', reply_markup=product_client_kb)
    await Test.product.set()


async def command_test_product(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as answers_counter:
        if answer == '/Фото':
            answers_counter['simple_shooting'] += 1
        elif answer == '/Фото+обработка':
            answers_counter['advanced_shooting'] += 1
        else:
            answers_counter['video_shooting'] += 1

        print(answers_counter['simple_shooting'], answers_counter['advanced_shooting'],
              answers_counter['video_shooting'])

    await message.answer('Вам нужен макияж?', reply_markup=makeup_client_kb)
    await Test.makeup.set()


async def command_test_makeup(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as answers_counter:
        if answer == '/Нет':
            answers_counter['simple_shooting'] += 1
        elif answer == '/С_одним_акцентом':
            answers_counter['advanced_shooting'] += 1
        else:
            answers_counter['video_shooting'] += 1

        print(answers_counter['simple_shooting'], answers_counter['advanced_shooting'],
              answers_counter['video_shooting'])

    await message.answer('Все ли верно?', reply_markup=test_conformation_client_kb)
    await Test.conformation.set()


async def command_confirm_test_results(message: types.Message, state: FSMContext):
    answer = message.text
    client_username = message.from_user.username
    if answer == '/Да':
        async with state.proxy() as answers_counter:
            guessed_tariff = ''
            if answers_counter['simple_shooting'] >= 2:
                guessed_tariff += data.shooting_types_name['simple_shooting']
            elif answers_counter['advanced_shooting'] >= 2:
                guessed_tariff += data.shooting_types_name['advanced_shooting']
            elif answers_counter['video_shooting'] >= 2:
                guessed_tariff += data.shooting_types_name['video_shooting']
            else:
                guessed_tariff += data.shooting_types_name['individual_shooting']

            await message.answer('Тест пройден, вот рекомндованный тариф: ' + guessed_tariff + '.'
                                 + '\n\nМожете узнать больше о тарифах в разделе Информация',
                                 reply_markup=inline_client_kb)
            await bot.send_message(manager_id, 'Заказ на тариф: ' + guessed_tariff +
                                   ' от пользователя: ' + client_username)
        await state.reset_state()
    else:
        await message.answer('Вы можете пройти тест заново или вернуться в главное меню',
                             reply_markup=miss_in_test_client_kb)
        await state.reset_state()

""" Answers to contact request"""


async def call_contact(callback: types.CallbackQuery):
    await callback.message.answer(data.contacts)
    await callback.answer()


""" Answers to home button """


async def command_home(message: types.Message):
    await message.answer('Главная', reply_markup=inline_client_kb)


""" Answers to repeat test"""


async def command_repeat_test(message: types.Message):
    await message.answer('Сколько времени вы готовы уделить на съемку?', reply_markup=time_client_kb)
    await Test.time.set()


""" Register handlers"""


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_home, commands=['На_главную'])
    dp.register_message_handler(command_repeat_test, commands=['Повторить_тест'])

    dp.register_callback_query_handler(call_info, text='info')
    dp.register_callback_query_handler(call_description, Text(endswith='shooting'))

    dp.register_callback_query_handler(call_test, text='test')
    dp.register_message_handler(command_test_time, state=Test.time)
    dp.register_message_handler(command_test_product, state=Test.product)
    dp.register_message_handler(command_test_makeup, state=Test.makeup)
    dp.register_message_handler(command_confirm_test_results, state=Test.conformation)

    dp.register_callback_query_handler(call_contact, text='contact')
