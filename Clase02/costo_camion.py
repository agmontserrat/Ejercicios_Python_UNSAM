# Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los
# cajones cargados en el camión.

import csv


def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costo = 0.0
    for row in rows:
        try:
            costo += (float(row[2])*int(row[1]))
        except ValueError:
            print('Tenemos datos faltantes en el archivo proporcionado!')
    f.close()
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
