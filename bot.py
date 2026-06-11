import os
from telegram import Bot
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    mensaje = """
📊 Hardware monitoreado

1. RTX 5060
2. RTX 5070
3. Ryzen 7 9700X
4. Samsung 990 Pro 2TB
5. DDR5 32GB

✅ Bot activo
"""
    
    await bot.send_message(
        chat_id=CHAT_ID,
        text=mensaje
    )

asyncio.run(main())
