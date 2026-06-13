import requests

busquedas = [
    "990 Pro",
    "Samsung 990 Pro",
    "DDR5",
    "Kingston DDR5",
    "Corsair DDR5"
]

for b in busquedas:
    url = "https://www.cyberpuerta.mx/index.php?cl=search&searchparam=" + b.replace(" ", "+")
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    print(b, "->", '"price":"' in r.text)