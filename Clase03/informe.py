# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas
# mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
# En lugar de tener hardcodeado un formato fijo, la nueva versión de la función costo_camion() puede sacar la
# información de interés de cualquier archivo CSV. En la medida en que el archivo tenga las columnas requeridas, el código va a funcionar.

# Modificá el programa informe.py que escribiste antes (ver Ejercicio clase 2, 18) para que use esta técnica para elegir
# las columnas a partir de sus encabezados.


import csv


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas) #Saco encabezados
        try:
            for fila in filas:
                record = dict(zip(encabezados, fila))
                camion.append(record)
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            pass
    return camion


def leer_precios(nombre_archivo):
    precios = dict()
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1]) #La clave es la fruta, el valor es el precio
            except IndexError: # Atrapa la ultima linea vacía
                pass
    return precios


def calcular_gastos(camion):
    suma = 0.0
    for each in camion:
        try:
            suma += (int(each['cajones']) * float(each['precio'])) #Cantidad de cajones por el precio de cada uno
        except ValueError: #Atrapa los valores que no están en missing.csv
            pass
    return suma


#Funciona con camion.csv, fecha_camion.csv y missing.csv
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
costo_camion = calcular_gastos(camion)
total_vendido = 0.0


for each in camion:
    try:
        total_vendido += ( int(each['cajones']) *float(precios[each['nombre']]) )
    except ValueError:
        pass

print(f'Costo camión: {costo_camion}')
print(f'Total recaudado: {total_vendido}')

if costo_camion > total_vendido:
    print('Hubo perdida de plata.')
else:
    print('Tenemos ganancia! :)')
