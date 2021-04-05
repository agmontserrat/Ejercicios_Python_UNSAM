# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas
# mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
import csv


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = dict()
            lote = {headers[0]: row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
            camion.append(lote)
    return camion


def leer_precios(nombre_archivo):
    precios = dict()
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print('Linea vacía!')

    return precios

def calcular_gastos(camion):
    suma = 0.0
    for each in camion:
        try:
            suma += (int(each['cajones']) * float(each['precio']))
        except KeyError:
            pass
    return suma

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
costo_camion = calcular_gastos(camion)
total_vendido = 0.0
for each in camion:
    try:
        total_vendido += ( each['cajones'] * precios[each['nombre']] )
    except:
        pass
print(f'Costo camión: {costo_camion}')
print(f'Total recaudado: {total_vendido}')

if costo_camion > total_vendido:
    print('Hubo perdida de plata.')
else:
    print('Tenemos ganancia! :)')
