from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


TOKEN = '5141468385:AAEis82dot0kanavhNHz_7cJC7Lqf6EGr4U'
MANAGER_ID = '368234011'

storage = MemoryStorage()
manager_id = MANAGER_ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
