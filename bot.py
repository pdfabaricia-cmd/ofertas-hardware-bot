import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

PRODUCTOS = [
    "RTX 5060",
    "RTX 5070",
    "Ryzen 7 9700X",
    "Samsung 990 Pro 2TB",
    "DDR5 32GB"
]

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
