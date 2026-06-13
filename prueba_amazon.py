import requests

url = "https://www.amazon.com.mx/s?k=rtx+5070"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text[:500])