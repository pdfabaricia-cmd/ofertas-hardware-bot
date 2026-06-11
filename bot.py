import os
from telegram import Bot
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🔥 ¡Tu bot funciona correctamente!"
    )

asyncio.run(main())