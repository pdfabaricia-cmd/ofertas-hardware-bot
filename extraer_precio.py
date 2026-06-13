import re

with open("cyber.txt", "r", encoding="utf-8") as f:
    texto = f.read()

precios = re.findall(r"\$([\d,]+\.\d{2})", texto)

print(precios[:10])