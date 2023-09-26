import puppeteer from "puppeteer";
import ExcelJS from "exceljs"

async function tablaSDriveNvidia(){
    const browser = await puppeteer.launch({
        headless:'false',
        slowMo:400
    })
    const page = await browser.newPage()   
    await page.setDefaultNavigationTimeout(0)
    await page.goto('https://www.nvidia.com/en-us/geforce/products/g-sync-monitors/specs/')

    const tableData = await page.evaluate(() => { 
        const selecTable = document.querySelector('table')
        const rows = Array.from(selecTable.querySelectorAll('tr'));
        return rows.map(row => {
            const columns = Array.from(row.querySelectorAll('th,td'));
            return columns.map(column => column.innerText);
        });
    });
    console.log(tableData)

    await browser.close();

    //Almacenamos los datos en un csv
    const workbook = new ExcelJS.Workbook();
    const worksheet = workbook.addWorksheet('Tabla');
    tableData.forEach(row => worksheet.addRow(row));
    await workbook.csv.writeFile('tabla.csv');
    console.log('Datos guardados en tabla.csv');
}
tablaSDriveNvidia()
