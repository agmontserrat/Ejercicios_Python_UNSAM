# ticker.py
import informe
from vigilante import vigilar
import csv
import formato_tabla

def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    return rows

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila


def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    for fila in filas:
        fila = [str(x) for x in fila.values()]
        formateador.fila(fila)


if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
