from loader import dp
from aiogram import types



HELP_COMMANDS = """
<b>/start</b> - <i>начать работу с ботом</i>
<b>/candies</b> - <i>чтобы поиграть в конфеты</i>
<b>/help</b> - <i>для просмотра команд, которые я могу выполнить</i>
<b>/vote</b> - <i>чтобы оценить моего чат бота</i>
<b>/cat</b> - <i>чтобы насладиться котиком</i>
"""

    

@dp.message_handler(commands=['help'])
async def help_command(message:types.Message):
    await message.reply(text = HELP_COMMANDS, parse_mode= 'HTML') 
    await message.delete()