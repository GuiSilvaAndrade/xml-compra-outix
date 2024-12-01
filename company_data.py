from xml.dom import minidom

def company_data():
    xml = open('nfe.xml')
    nfe = minidom.parse(xml)

    # ENTERPRISE
    fantasy_name = nfe.getElementsByTagName('xFant')[0].firstChild.data

    if fantasy_name[0:5] == 'BRAFT':
        enterprise = 'Brasfort'
    else:
        enterprise = 'Lotus'

    # DATE
    unformatted_date = nfe.getElementsByTagName('dhEmi')[0].firstChild.data
    year = unformatted_date[0:4]
    day = unformatted_date[8:10]
    month = unformatted_date[5:7]
    date = (f'{day}/{month}/{year}')

    # STATE
    state = nfe.getElementsByTagName('UF')[0].firstChild.data

    # INVOICE NUMBER
    num_nfe = nfe.getElementsByTagName('nNF')[0].firstChild.data

    if len(num_nfe) == 6:
        nfe_formatted = f'{num_nfe[0:3]}.{num_nfe[3:6]}'
    else:
        nfe_formatted = f'{num_nfe[0:2]}.{num_nfe[2:6]}'

    nfe = f'NF {nfe_formatted}'    

    return enterprise, date, nfe, state


