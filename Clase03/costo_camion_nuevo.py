# Suponé que querés hacer que el programa costo_camion.py trabaje con diferentes archivos de entrada,
# pero que no le importe la posición exacta de la columna que tiene la cantidad de cajones o el precio.
# Es decir, que entienda que la columna tiene el precio por su encabezado y no por su posición dentro del archivo.

# En lugar de tener hardcodeado un formato fijo, la nueva versión de la función costo_camion()
# puede sacar la información de interés de cualquier archivo CSV.
# En la medida en que el archivo tenga las columnas requeridas, el código va a funcionar.


import csv


def costo_camion(nombre_archivo):
    f = open(nombre_archivo)

    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total = 0.0
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return costo_total



costo = costo_camion('../Data/camion.csv')
print(costo)