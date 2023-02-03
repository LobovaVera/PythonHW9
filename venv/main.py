from handlers import dp
from aiogram import Bot, Dispatcher, executor, types


async def on_start(_):
    print("Started")
  

if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = on_start)    


