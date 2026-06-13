import os
import re
import json
import asyncio
from playwright.async_api import async_playwright
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

PRODUCTOS = [
"RTX 5060",
"RTX 5070",
"Ryzen 7 9700X",
"990 Pro"
]

async def obtener_total(producto):

```
url = "https://www.cyberpuerta.mx/index.php?cl=search&searchparam=" + producto.replace(" ", "+")

async with async_playwright() as p:

    navegador = await p.chromium.launch(headless=True)

    pagina = await navegador.new_page()

    await pagina.goto(
        url,
        wait_until="domcontentloaded",
        timeout=120000
    )

    await pagina.wait_for_timeout(10000)

    texto = await pagina.locator("body").inner_text()

    await navegador.close()

    precios = re.findall(r"\$([\d,]+\.\d{2})", texto)

    if len(precios) >= 2:

        producto_precio = float(precios[0].replace(",", ""))
        envio = float(precios[1].replace(",", ""))

        return round(producto_precio + envio, 2)

    return None
```

async def main():

```
try:
    with open("precios.json", "r", encoding="utf-8") as f:
        anteriores = json.load(f)
except:
    anteriores = {}

nuevos = {}

mensaje = "🔥 BAJADA DE PRECIOS DETECTADA 🔥\n\n"
hay_oferta = False

for producto in PRODUCTOS:

    try:

        total_actual = await obtener_total(producto)

        if total_actual is None:
            continue

        nuevos[producto] = total_actual

        if producto in anteriores:

            precio_anterior = anteriores[producto]

            if total_actual < precio_anterior:

                ahorro = round(precio_anterior - total_actual, 2)

                mensaje += (
                    f"🖥 {producto}\n"
                    f"Antes: ${precio_anterior}\n"
                    f"Ahora: ${total_actual}\n"
                    f"Ahorro: ${ahorro}\n\n"
                )

                hay_oferta = True

    except Exception as e:
        print(producto, e)

with open("precios.json", "w", encoding="utf-8") as f:
    json.dump(nuevos, f, indent=4)

if hay_oferta:

    await bot.send_message(
        chat_id=CHAT_ID,
        text=mensaje
    )
```

asyncio.run(main())
