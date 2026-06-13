import requests

url = "https://listado.mercadolibre.com.mx/rtx-5070"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print(r.text[:3000])