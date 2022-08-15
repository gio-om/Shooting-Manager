from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os


TOKEN = 'YOUR_TOKEN'
MANAGER_ID = 'YOUR_MANAGER_ID'

storage = MemoryStorage()
manager_id = MANAGER_ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
