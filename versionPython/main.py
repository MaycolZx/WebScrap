from bs4 import BeautifulSoup
import bs4
import requests
import re
import csv

URL_BASE = "https://unaluka.com/collections/ofertas?page="
nextSignal = True
numerPage = 1
# Lista de valores
values = [
    ["Product-Vendor"],
    ["Product-Name"],
    ["Price-Deposit"],
    ["Sale"],
    ["Price-Credit-Card"],
    ["Price-Compare"],
]
while nextSignal:
    URL_FINAL = f"{URL_BASE}{numerPage}"
    r = requests.get(URL_FINAL)
    soup = BeautifulSoup(r.text, "html.parser")
    nextPage = soup.find("a", class_="next")
    if nextPage and "disabled" in nextPage["class"]:
        nextSignal = False
    else:
        numerPage += 1
    # print(f"Entrando a la pagina:{URL_FINAL}")
    elementos = soup.find_all("div", class_="product-wrapper effect-overlay")
    for i in elementos:
        productVendor = i.find("div", class_="product-vendor").get_text(strip=True)
        nameProduct = i.find("h5", class_="product-name balance-row-3").get_text(
            strip=True
        )
        precio = i.find("div", class_="price-deposit-inner")
        if not precio:
            continue
        precio = precio.get_text(strip=True)
        descuento = i.find("span", class_="sale-text").get_text(strip=True)
        priceCard = i.find(
            "div", class_="price-no-discount price-credit-card"
        ).get_text(strip=True)
        priceCompare = i.find("div", class_="price-compare")
        if not priceCompare:
            priceCompare = "none"
        else:
            priceCompare = priceCompare.get_text(strip=True)
        index = [productVendor, nameProduct, precio, descuento, priceCard, priceCompare]
        for i in range(6):
            values[i].append(index[i])
        # print(f"{productVendor.get_text(strip=True)}   {nameProduct.get_text(strip=True)}   {precio.get_text(strip=True)}   {descuento.get_text(strip=True)}   {priceCard.get_text(strip=True)}   {priceCompare}")

with open("datos.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in values:
        escritor_csv.writerow(fila)
