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
