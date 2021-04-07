# En el Ejercicio 2.18, escribiste un programa llamado informe.py que calculaba las ganancias o
# pérdidas de un camión que compra a productores y vende en el mercado.
# Copiá su contenido en un archivo tabla_informe.py.
# En este ejercicio, vas a comenzar a modificarlo para producir una tabla como ésta:


import csv


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            linea = [fila[0], int(fila[1]), float(fila[2])]
            lote = dict(zip(encabezados, linea))
            camion.append(lote)
    return camion


def leer_precios(nombre_archivo):
    precios = dict()
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print('Linea vacía!')

    return precios

def hacer_informe(camion, precios):
    lista = []
    for each in camion:

        cambio = precios[each['nombre']] - each['precio']
        lista.append((each['nombre'], each['cajones'], each['precio'], cambio))
    return lista
def headers (tupla):
    for header in tupla:
        print(f'{header:>10s}', end='')
    print()
    for header in tupla:
        print(f'{"-"*10} ',end='')
    print()

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

informe = hacer_informe(camion, precios)
headers(('Nombre', 'Cajones', 'Precio', 'Cambio'))
#headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
#print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10.s} {headers[3]:>10.s}')
for nombre, cajones, precio, cambio in informe:
        print(f"{nombre:>10s} {cajones:>10d} {f'${precio:.2f}':>10}{cambio:>10.2f}")
