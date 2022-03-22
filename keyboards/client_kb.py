from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

""" Start keyboard """
info_button = InlineKeyboardButton(text='Информация о тарифах', callback_data='info')
test_button = InlineKeyboardButton(text='Пройти тест для определения тарифа', callback_data='test')
contact_button = InlineKeyboardButton(text='Контакты', callback_data='contact')

inline_client_kb = InlineKeyboardMarkup(row_width=1).add(info_button).add(test_button).add(contact_button)

""" Information keyboard """
simple_shooting_button = InlineKeyboardButton(text='Съемка', callback_data='simple_shooting')
advanced_shooting_button = InlineKeyboardButton(text='Продвинутая съемка', callback_data='advanced_shooting')
video_shooting_button = InlineKeyboardButton(text='Фото+Видео', callback_data='video_shooting')
individual_shooting_button = InlineKeyboardButton(text='Индивидуальный тариф', callback_data='individual_shooting')

tariff_kb = InlineKeyboardMarkup(row_width=1).add(simple_shooting_button).\
    add(advanced_shooting_button).add(video_shooting_button).add(individual_shooting_button)

""" Keyboard for choosing time """
button_30min = KeyboardButton('/30_минут')
button_1hour = KeyboardButton('/1_час')
button_2hour = KeyboardButton('/больше')

time_client_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(button_30min, button_1hour, button_2hour)

""" Keyboard for choosing product(format) """
button_common_photos = KeyboardButton('/Фото')
button_advanced_photos = KeyboardButton('/Фото+обработка')
button_photo_video = KeyboardButton('/Фото+видео')

product_client_kb = ReplyKeyboardMarkup(resize_keyboard=True).\
    row(button_common_photos, button_advanced_photos, button_photo_video)

""" Keyboard for choosing makeup type """
button_no_makeup = KeyboardButton('/Нет')
button_simple_makeup = KeyboardButton('/С_одним_акцентом')
button_advanced_makeup = KeyboardButton('/С_несколькими_акцентами')

makeup_client_kb = ReplyKeyboardMarkup(resize_keyboard=True).\
    row(button_no_makeup, button_simple_makeup, button_advanced_makeup)

""" Keyboard for conformation test results"""
button_confirm = KeyboardButton('/Да')
button_cancel = KeyboardButton('/Нет')

test_conformation_client_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_confirm).\
    add(button_cancel)

""" Keyboard for miss """
button_home = KeyboardButton('/На_главную')
button_repeat_test = KeyboardButton('/Повторить_тест')

miss_in_test_client_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_home).\
    add(button_repeat_test)
