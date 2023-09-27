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
We can see that a `csv` file(**tabla.csv**) is generated with the data contained in the table generated with `javascript` through an `async` function to consult the data.
## 2. Python - Selenium & BeatifulSoup4
For this case we are going to extract the product data from the page [Una Luka](https://unaluka.com "UnaLuka"), first initialize the python virtual environment and use the following command:

```bash
cd versionPython
```
Next we are going to create and start the python virtual environment natively with the following command:
```bash
python -m venv scrapenv
source scrapenv/bin/activate
```
Then to install the virtual environment dependencies.
```bash
pip install -r requirements
```
Now we execute the file with extension **py**(`python`) with the command:

```bash
python main.py
```
We can see that a `csv` file(**datos.csv**) is generated with the data contained by the search for each product.

**Note**: To exit the `python venv` virtual environment use the `deactivate` command in the terminal where the environment has been initialized.