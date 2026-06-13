import requests

url = "https://www.cyberpuerta.mx"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print(r.text[:2000])