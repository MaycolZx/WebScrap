# WebScraping
🇪🇸 [Spanish](./README.md) 
🇬🇧 [English](../README.md)

## Introduccion:
Vamos a scrapear las siguientes paginas de dos formas distintas empleadno tanto `nodejs` y `python`:
- [G-SYNC GAMING MONITORS](https://www.nvidia.com/en-us/geforce/products/g-sync-monitors/specs/ "G-SYNC GAMING MONITORS")  
- [Una Luka](https://unaluka.com "UnaLuka")

Primero inicializamos el proyecto clonando el repositorio con el siguiente comando:
```bash
git clone https://github.com/MaycolZx/WebScrap.git
```

Ahora verificamos si tenemos las dependencias necesarias de la siguiente manera atraves de la terminal:
```bash
node --version && python3 --version
```
Si no tenemos ningun mensaje de error entonces podemos seguir de lo contrario recomiendo instalar estas dependecias atraves de las paginas oficiales:

- https://www.python.org/downloads/
- https://nodejs.org/es

Emplearemos dos opciones, ambas sujetas casos totalmente distintos :
## 1. Nodejs(Javascript) - Puppeteer & exceljs
Para este caso vamos a extraer los datos de la pagina [G-SYNC GAMING MONITORS](https://www.nvidia.com/en-us/geforce/products/g-sync-monitors/specs/ "G-SYNC GAMING MONITORS") nos dirigimos al directorio de `nodejs` con un ChangeDirectory

```bash
cd versionNodejs
```
Seguido de los comandos para inicializar el proyecto nodejs

```bash
node install
```
Ahora ejecutamos el archivo con extension **js**(`javascript`) con el comando:

```bash
node server.js
```
Podemos observar que se genera un archivo `csv` (**tabla.csv**) con los datos contenidos en la tabla generada con `javascript` a traves de una funcion `async` para consultar los datos
## 2. Python - Selenium & BeatifulSoup4
Para este caso vamos a extraer los datos de los productos de la pagina [Una Luka](https://unaluka.com "UnaLuka") primero inicializar el entorno virtual de python usaremos el siguiente comando:

```bash
cd versionPython
```
Seguido vamos a crear e iniciar el entorno virtual de python de forma nativa con el siguiente comando:
```bash
python -m venv scrapenv
source scrapenv/bin/activate
```
Luego para instalar las dependencias del entorno virtual. 
```bash
pip install -r requirements
```
Ahora ejecutamos el archivo con extension **py**(`python`) con el comando:

```bash
python main.py
```
Podemos observar que se genera un archivo `csv` (**datos.csv**) con los datos contenidos por la busqueda de cada producto .

**Nota** : Para salir del entorno virtual de `python venv` usar el comando `deactivate` en la terminal donde se haya inicializado el entorno.