from loader import dp
from loader import *
from aiogram.types import Message
from random import randint
from aiogram.types import ReplyKeyboardRemove
from keyboards import spm_kb
from keyboards import bot_game_kb
from keyboards import kb
from config import total, player_switch



@dp.message_handler(commands = ['candies'])
async def start_candy_game(message:Message):
    await bot.send_message(chat_id=message.from_user.id, text = "Конфетки!", reply_markup= ReplyKeyboardRemove())
    await message.answer("Ура играем в конфетки!\n Для игры со мной нажмите кнопку 'Играем с ботом' \n  для игры с другом ждите обновления\n ", reply_markup = spm_kb)
    
 
@dp.message_handler(commands = ['bot_candy_game'])
async def bot_candy_game(message:Message):
    global total
    global player_switch

    total = int(randint(30, 101))
    player_switch = randint(0,2)

    if player_switch:
        await message.answer(f'Кидаем жребий. Певым ходит {message.from_user.first_name}. На столе лежит {total} конфет, сколько берешь?')
    else:
        await message.answer(f'Кидаем жребий. Певым хожу я! Трепещи, кусок мяса!')
        candy_bot_num = total%29
        await message.answer(f"Мой ход! На столе {total} конфет! Я беру {candy_bot_num} конфет.")
        total -= candy_bot_num
        player_switch = True
        if total <=0:
            await winner_time()
            return True
        else:
            await message.answer(f" На столе {total} конфет! Сколько возьмешь? ")
        



        
@dp.message_handler()
async def candy_game(message:Message):
    global player_switch
    global total
    global userId
    userId = message.from_user.id
    count = int(message.text)
    name = message.from_user.first_name
    if message.text.isdigit() and 0 < count <29:
    
            total -= count
            player_switch = False
            await message.answer(f" {name} взял {count} конфет и на столе осталось {total}")

            if total <= 0:
                await winner_time()
                return True
            
            else:   # ходит бот
                if total <= 28:
                    candy_bot_num = total
                elif total%29 == 0:
                    await message.answer("Я и не знал, что люди могут быть такие умные! Хотя, может это случайность...")
                    await bot.send_sticker(message.from_user.id, sticker ="CAACAgIAAxkBAAEHiqNj2l0YzrSBT5H9jaCsTMOSszikiwACGAADwDZPE9b6J7-cahj4LgQ")
                    candy_bot_num = randint(1, 28)
        
                else:
                    candy_bot_num = total%29
            
                await message.answer(f"Мой ход! На столе {total} конфет! Я беру {candy_bot_num} конфет.")
                total -= candy_bot_num
                player_switch = True
            if total <=0:
                await winner_time()
                return True
            else:
                await message.answer(f" На столе {total} конфет! Сколько возьмешь? ")




async def winner_time():
    global userId
    if player_switch:
        await bot.send_message(chat_id=userId, text = "Я победил! Очевидно искуственный разум совершеннее человеческого!", reply_markup= kb)
        
    else:
        await bot.send_message(chat_id=userId, text ="Ты победил? 😭 Не может такого быть! Давай еще раз!\n ", reply_markup=bot_game_kb)
    
