import requests

url = "https://www.cyberpuerta.mx/index.php?cl=search&searchparam=RTX+5070"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

with open("pagina.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Guardado")