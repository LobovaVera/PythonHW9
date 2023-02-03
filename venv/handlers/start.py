from loader import dp
from aiogram import types
from keyboards import kb, ikb, spm_kb, bot_game_kb

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer(text = f'Приветствую, {message.from_user.first_name}!', reply_markup = kb )
    await message.delete()