from xml.dom import minidom
from openpyxl import load_workbook
from company_data import *
from define_sku import *

enterprise, date, nfe, state = company_data()

sheet = load_workbook('model.xlsx')
sheet['main']['A2'] = enterprise
sheet['main']['A3'] = date
sheet['main']['A4'] = nfe
sheet['main']['A5'] = state
sheet.save('model.xlsx')


nfe = minidom.parse(open('nfe.xml'))

qty_itens = nfe.getElementsByTagName('det')
for itens in qty_itens:
    qty_itens = int(itens.attributes['nItem'].value)
    

for i in range(qty_itens):
    row = i + 2
    cod_str = nfe.getElementsByTagName('cProd')[i].firstChild.data
    cod = int(cod_str)
    qty = nfe.getElementsByTagName('qCom')[i].firstChild.data
    price = nfe.getElementsByTagName('vUnCom')[i].firstChild.data
    ipi = float(nfe.getElementsByTagName('pIPI')[i].firstChild.data)   
    
    sheet['main'][f'B{row}'] = cod
    sheet['main'][f'C{row}'] = define_sku(cod)
    sheet['main'][f'D{row}'] = int(qty)    
    sheet['main'][f'G{row}'] = ipi

    if state == 'SC':
        sheet['main'][f'E{row}'] = f'={price}*{1 + (ipi/100)}'
    else:
        sheet['main'][f'E{row}'] = f'={price}*1.08*{1 + (ipi/100)}'

sheet.save('model.xlsx')

   
