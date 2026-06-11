from telegram import Bot
import asyncio

TOKEN = "8791643909:AAGS-jPrDPRDLwhaC4FEFYxReHcBZPaQ-AA"
CHAT_ID = "8575814755"

bot = Bot(token=TOKEN)

async def main():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🔥 ¡Tu bot funciona correctamente!"
    )

asyncio.run(main())