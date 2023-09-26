from bs4 import BeautifulSoup
import bs4
import requests
import re

URL_BASE = "https://scrapepark.org/spanish/"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

# 2. "Parsear" ese HTML
soup = BeautifulSoup(html_obtenido, "html.parser")
