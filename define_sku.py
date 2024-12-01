from openpyxl import load_workbook

def define_sku(cod):
    sheet = load_workbook('model.xlsx')

    for i in range(0, 999):
        row = i + 2

        if cod == sheet['SKU'][f'B{row}'].value:
            return sheet['SKU'][f'A{row}'].value

    
    