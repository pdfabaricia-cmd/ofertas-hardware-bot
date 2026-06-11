import os
import json
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

with open("productos.json", "r", encoding="utf-8") as f:
    PRODUCTOS = json.load(f)

async def main():
    mensaje = "📊 REPORTE DE HARDWARE\n\n"

    for producto in PRODUCTOS:
        mensaje += f"🔍 {producto}\n"
        mensaje += "Estado: Monitoreando\n\n"

    mensaje += "✅ Bot funcionando correctamente"

    await bot.send_message(
        chat_id=CHAT_ID,
        text=mensaje
    )

asyncio.run(main())
