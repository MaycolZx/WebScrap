from bs4 import BeautifulSoup
import bs4
import requests
import re
import csv

URL_BASE = "https://unaluka.com/collections/ofertas?page="
nextSignal = True
numerPage = 1

product_info = {
        "Product-Vendor": [],
        "Product-Name": [],
        "Price-Deposit": [],
        "Sale": [],
        "Price-Credit-Card": [],
        "Price-Compare": []
    }

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
        for k,v in zip(product_info.keys(),index):
            product_info[k].append(v)

# Nombre del archivo CSV de salida
csv_filename = "productos.csv"
# Abre el archivo CSV en modo de escritura
with open(csv_filename, mode='w', newline='') as csv_file:
    # Crea un escritor CSV
    csv_writer = csv.writer(csv_file)
    # Escribe el encabezado (las claves del diccionario) en el archivo CSV
    csv_writer.writerow(product_info.keys())
    # Combina los valores de las listas en una lista de tuplas
    data_rows = zip(*product_info.values())
    # Escribe los datos en el archivo CSV
    csv_writer.writerows(data_rows)

print(f"Los datos se han guardado en '{csv_filename}'.")