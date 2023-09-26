# WebScraping
🇪🇸 [Spanish](./Spanish/README.md) 
🇬🇧 [English](./README.md)

## Introduccion:
We are going to scrape the following pages in two different ways using both `nodejs` and `python`:
- [G-SYNC GAMING MONITORS](https://www.nvidia.com/en-us/geforce/products/g-sync-monitors/specs/ "G-SYNC GAMING MONITORS")  
- [Una Luka](https://unaluka.com "UnaLuka")

First we initialize the project by cloning the repository with the following command:
```bash
git clone https://github.com/MaycolZx/WebScrap.git
```

Now we check if we have the necessary dependencies as follows through the terminal:
```bash
node --version && python3 --version
```
If we don't have any error messages then we can continue, otherwise I recommend installing these dependencies through the official pages:

- https://www.python.org/downloads/
- https://nodejs.org/es

We will use two options, both subject to totally different cases:
## 1. Nodejs(Javascript) - Puppeteer & exceljs
For this case we are going to extract the data from the [G-SYNC GAMING MONITORS](https://www.nvidia.com/en-us/geforce/products/g-sync-monitors/specs/ "G-SYNC GAMING MONITORS") page and go to the `nodejs` directory with a ChangeDirectory.

```bash
cd versionNodejs
```
Followed by the commands to initialize the nodejs project.

```bash
node install
```
Now we execute the file with extension **js**(`javascript`) with the command:

```bash
node server.js
```
We can see that a `csv` file is generated with the data contained in the table generated with `javascript` through an `async` function to consult the data.
## 2. Python - Selenium & BeatifulSoup4
Para este caso vamos a extraer los datos de los productos de la pagina [Una Luka](https://unaluka.com "UnaLuka") primero inicializar el entorno virtual de python usaremos el siguiente comando:

```bash
cd versionPython
```
Seguido inicializamos el proyecto con los siguientes comandos:
```bash
pipenv shell
#Luego para instalar las dependencias del entorno virtual 
pipenv install --dev
```
Ahora ejecutamos el archivo con extension **py**(`python`) con el comando:

```bash
python main.py
```

Podemos observar que se genera un archivo `csv` con los datos contenidos por la busqueda de cada producto .

