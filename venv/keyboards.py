from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, callback_query
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton(text = '/cat')
b2 = KeyboardButton(text = '/help')
b3 = KeyboardButton(text = '/candies')
b4 = KeyboardButton(text = '/vote')

kb.add(b1, b2).insert(b3).insert(b4)

#vote keyboard

ikb = InlineKeyboardMarkup(row_width = 2)

ib1 = InlineKeyboardButton(text='Да', callback_data='yes')
ib2 = InlineKeyboardButton(text= 'Нет', callback_data='no')
ib3 = InlineKeyboardButton(text="Главное меню", callback_data='main')

ikb.add(ib1, ib2, ib3)


#select playmode keyboard

spm_kb = InlineKeyboardMarkup(resize_keyboard=True)

spm_b1 = InlineKeyboardButton(text = "Играем с ботом", callback_data = 'bot')
# spm_b2 = InlineKeyboardButton(text = "Играем с другом", callback_data = 'user')
spm_b3 = InlineKeyboardButton(text = "Правила", callback_data = 'rules')

spm_kb.add(spm_b1, spm_b3)

bot_game_kb = ReplyKeyboardMarkup(resize_keyboard=True)

bg_b1 = KeyboardButton(text = '/bot_candy_game')

bot_game_kb.add(bg_b1)