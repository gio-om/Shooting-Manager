from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()
manager_id = os.getenv('MANAGER_ID')

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
