import requests
import re

url = "https://www.cyberpuerta.mx/index.php?cl=search&searchparam=RTX+5070"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("Coincidencias:")
print(re.findall(r'"price":"(\d+)"', r.text)[:10])