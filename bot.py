import os
from telegram import Bot
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def main():
    mensaje = """
🚨 PRUEBA NUEVA 🚨

Si recibes este mensaje,
GitHub está ejecutando el código correcto.

RTX 5060
RTX 5070

Hora de prueba
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=mensaje
    )

asyncio.run(main())
