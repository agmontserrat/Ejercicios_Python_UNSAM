# fileparse.py del ejercicio 6.9
#Modificá la función parse_csv() de forma que (opcionalmente) pueda trabajar con este tipo de archivos, 
# creando tuplas en lugar de diccionarios cuando no haya encabezados. 
import csv



def parse_csv(nombre_archivo, select=None, types = None, has_headers=True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        if (not has_headers and select):
            raise RuntimeError("Para seleccionar, necesito encabezados.")

        # Lee los encabezados del archivo, si le pasamos has_headers=False no lo toma
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select and has_headers:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
            #Convierte los nombres de las columnas listadas en select a índices (posiciones) de columnas en el archivo.
        else:
            indices = []

        registros = []
        for num, fila in enumerate(filas, 1):
            if not fila: # Saltear filas vacías
                continue


            try: 
                if indices: # Filtrar la fila si se especificaron tipos
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar el diccionario
            except Exception as e:
                if not silence_errors:
                    print(f"Fila {num}: No pude convertir {fila}")
                    print(f"Fila {num}: Motivo: {e}")


            if has_headers:
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                registros.append(tuple(fila)) #Si no hay encabezados, convierto a tupla los valores.
    
    return registros



