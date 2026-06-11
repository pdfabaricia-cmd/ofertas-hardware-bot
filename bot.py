import os
import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)


PRODUCTOS = [
    "rtx+5060",
    "rtx+5070",
    "ryzen+7+9700x",
    "samsung+990+pro+2tb",
    "ddr5+32gb"
]


def buscar_ddtech(producto):

    url = f"https://ddtech.mx/buscar/{producto}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=20)

    soup = BeautifulSoup(r.text, "lxml")

    texto = soup.get_text(" ", strip=True)

    return texto[:500]


async def main():

    mensaje = "🔎 BUSQUEDA DDTECH\n\n"

    for producto in PRODUCTOS:

        resultado = buscar_ddtech(producto)

        mensaje += f"🖥 {producto}\n"
        mensaje += resultado[:200]
        mensaje += "\n\n"


    await bot.send_message(
        chat_id=CHAT_ID,
        text=mensaje
    )


asyncio.run(main())