import asyncio
from playwright.async_api import async_playwright

async def main():

    async with async_playwright() as p:

        navegador = await p.chromium.launch(headless=False)

        pagina = await navegador.new_page()

        await pagina.goto(
            "https://www.cyberpuerta.mx/index.php?cl=search&searchparam=RTX+5070",
            wait_until="domcontentloaded",
            timeout=120000
        )

        await pagina.wait_for_timeout(15000)

        texto = await pagina.locator("body").inner_text()

        with open("cyber.txt", "w", encoding="utf-8") as f:
            f.write(texto)

        print("Guardado")

        await navegador.close()

asyncio.run(main())