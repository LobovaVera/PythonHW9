from loader import dp
from loader import *
from aiogram.types import Message
from random import randint
from aiogram.types import ReplyKeyboardRemove
from keyboards import spm_kb
from keyboards import bot_game_kb
from keyboards import kb
from config import players_dic, players_switch_dic



@dp.message_handler(commands = ['candies'])
async def start_candy_game(message:Message):
    await bot.send_message(chat_id=message.from_user.id, text = "Конфетки!", reply_markup= ReplyKeyboardRemove())
    await message.answer("Ура играем в конфетки!\n Для игры со мной нажмите кнопку 'Играем с ботом' \n  для игры с другом ждите обновления\n ", reply_markup = spm_kb)
    
 
@dp.message_handler(commands = ['bot_candy_game'])
async def bot_candy_game(message:Message):
    global set_number
    
   
    global players_dic
    players_dic[message.from_user.id] = set_number
    global players_switch_dic
    players_switch_dic[message.from_user.id] = randint(0,2)


    if players_switch_dic[message.from_user.id] :
        await message.answer(f'Кидаем жребий. Певым ходит {message.from_user.first_name}. На столе лежит {players_dic[message.from_user.id]} конфет, сколько берешь?')
    else:
        await message.answer(f'Кидаем жребий. Певым хожу я! Трепещи, кусок мяса!')
        candy_bot_num = players_dic[message.from_user.id]%29
        await message.answer(f"Мой ход! На столе {players_dic[message.from_user.id]} конфет! Я беру {candy_bot_num} конфет.")
        players_dic[message.from_user.id] -= candy_bot_num
        players_switch_dic[message.from_user.id]  = True
        if players_dic[message.from_user.id] <=0:
            await winner_time(message.from_user.id)
            return True
        else:
            await message.answer(f" На столе {players_dic[message.from_user.id]} конфет! Сколько возьмешь? ")
        



        
@dp.message_handler()
async def candy_game(message:Message):
    global players_dic
    global players_switch_dic
    
    count = int(message.text)
    name = message.from_user.first_name
    if message.text.isdigit() and 0 < count <29:
            players_dic[message.from_user.id] -= count 
            players_switch_dic[message.from_user.id] = False
            await message.answer(f" {name} взял {count} конфет и на столе осталось {players_dic[message.from_user.id]}")

            if players_dic[message.from_user.id] <= 0:
                await winner_time(message.from_user.id)
                return True
            
            else:   # ходит бот
                if players_dic[message.from_user.id] <= 28:
                    candy_bot_num = players_dic[message.from_user.id]
                elif players_dic[message.from_user.id]%29 == 0:
                    await message.answer("Я и не знал, что люди могут быть такие умные! Хотя, может это случайность...")
                    await bot.send_sticker(message.from_user.id, sticker ="CAACAgIAAxkBAAEHiqNj2l0YzrSBT5H9jaCsTMOSszikiwACGAADwDZPE9b6J7-cahj4LgQ")
                    candy_bot_num = randint(1, 28)
        
                else:
                    candy_bot_num = players_dic[message.from_user.id]%29
            
                await message.answer(f"Мой ход! На столе {players_dic[message.from_user.id]} конфет! Я беру {candy_bot_num} конфет.")
                players_dic[message.from_user.id] -= candy_bot_num
                players_switch_dic[message.from_user.id]  = True
            if players_dic[message.from_user.id] <=0:
                await winner_time(message.from_user.id)
                return True
            else:
                await message.answer(f" На столе {players_dic[message.from_user.id]} конфет! Сколько возьмешь? ")
    
    elif message.text.isdigit() and int(message.text)>28:
        await message.answer("Ой. Можно взять только от 1 до 28 конфет.")
    try:
        int(message.text.isdigit)
    except ValueError:
        await message.answer(f"Простите, я еще не знаю, что такое '{message.text}'. Я еще совсем маленький бот. ")





async def winner_time(userId):
    
    if players_switch_dic[userId]:
        await bot.send_message(chat_id=userId, text = "Я победил! Очевидно искуственный разум совершеннее человеческого!", reply_markup= kb)
        
    else:
        await bot.send_message(chat_id=userId, text ="Ты победил? 😭 Не может такого быть! Давай еще раз!\n ", reply_markup=bot_game_kb)



    