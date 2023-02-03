from loader import dp
from aiogram import types
from loader import *
from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, callback_query, ReplyKeyboardRemove
from keyboards import kb, ikb, bot_game_kb
import random

HELP_COMMANDS = """
<b>/start</b> - <i>начать работу с ботом</i>
<b>/candies</b> - <i>чтобы поиграть в конфеты</i>
<b>/help</b> - <i>для просмотра команд, которые я могу выполнить</i>
<b>/vote</b> - <i>чтобы оценить моего чат бота</i>
<b>/cat</b> - <i>чтобы насладиться котиком</i>
"""
global player_switch

arr_bot = ["https://media.lpgenerator.ru/uploads/2021/07/26/1.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzZ22qi5l5zs4kRZmkcm8bMrdOtbPbA4oU1Q&usqp=CAU", "https://umi.ru/images/blog/bot/bot1.jpg"]
dic_bot = dict(zip(arr_bot, ["Зацени бота! Хорош?", "Как Бот? Норм?", "Я бот-красавчик, правда?"]))
random_bot_pic = random.choice(list(dic_bot.keys()))


@dp.message_handler(commands = ["cat"])
async def cat_command(message:types.Message):
    await message.answer("Смотри, какой смешной котик!")
    await bot.send_sticker(message.from_user.id, sticker = "CAACAgIAAxkBAAEHirtj2mM9w8LkKVEpWv-q7snar9q_dgACaAIAAsoDBgsoCgAB2Y6GhyIuBA")    
    await message.delete()


@dp.message_handler(commands= ['vote'])
async def vote(message:types.Message):
    global random_bot_pic
    await bot.send_message(chat_id=message.from_user.id, text = "Смотри!", reply_markup= ReplyKeyboardRemove())
    random_bot_pic = random.choice(list(filter(lambda x: x!= random_bot_pic, list(dic_bot.keys()))))
    await bot.send_photo(chat_id=message.from_user.id, photo= random_bot_pic, caption= dic_bot[random_bot_pic], reply_markup=ikb)
    await message.delete()

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'yes':
        await callback.answer("Ура! Ура! Ура!")
        await bot.send_message(chat_id= callback.from_user.id, text ="Спасибо 💕")
        await bot.send_message(chat_id = 1503472091, text=f" Поставил лайк {callback.from_user.full_name}")
    elif callback.data == 'no':
        await callback.answer("Как ты мог?! Пойду плакать. Я в депрессии.")
        await bot.send_message(chat_id= callback.from_user.id, text ="О нет! 😭")
    elif callback.data == 'bot':
        await bot.send_message(chat_id= callback.from_user.id, text ="Жми ", reply_markup= bot_game_kb)
        await callback.answer()
    # elif callback.data == 'user':
    #     user_user_candy_game()
    elif callback.data == 'rules':
        await bot.send_message(chat_id= callback.from_user.id, text ="На столе лежит рандомное число конфет.\n Победил тот, кто взял последнюю конфетку.\n Можно взять от одной до 28 конфет.")
        await callback.answer()
    else:
        await bot.send_message(chat_id= callback.from_user.id, text ="Пожалуйста!", reply_markup = kb )
        await callback.answer()
