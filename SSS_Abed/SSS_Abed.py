from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('5484337646:AAHuupgWpbqT6_5CrOH27Vi9KSWMxkFyH6I')



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message,
                      """\
Botimizda xodimlar bugungi nonushta, 
tushlik va kechgi ovqatni yeyish yoki yemasliklarini tanlashlari kerak bo'ladi. 
Ovqat tayyor bo'lganda esa botimiz kerak hodimlarni ovqatga chaqiradi.\
""")



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
    


import asyncio
asyncio.run(bot.polling())