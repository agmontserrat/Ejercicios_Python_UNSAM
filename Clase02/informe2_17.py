# si necesitás tener los precios de toda la mercadería, no resulta práctico abrir y cerrar el archivo para consultar cada precio.
# Por eso ahora te proponemos generar un diccionario que contenga todos los precios.
# En este diccionario, podés consultar luego los precios de cada producto.
import csv


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
