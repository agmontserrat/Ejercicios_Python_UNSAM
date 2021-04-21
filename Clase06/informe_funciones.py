#Volvé a tu programa tabla_informe.py y modificalo de modo que todas las operaciones principales, 
# incluyendo cálculos e impresión, sean llevados a cabo por una colección de funciones. 
# Guarda la nueva versión en un archivo informe_funciones.py. Más específicamente:

#   Creá una función imprimir_informe(informe) que imprima el informe.
#   Cambiá la última parte del programa de modo que consista sólo en una serie de llamados a funciones, sin ningún cómputo.

import csv
from fileparse69 import parse_csv

def leer_camion(nombre_archivo):
    '''Recibe el nombre del archivo a abrir y devuelve la lista con los diccionarios'''
    return parse_csv(nombre_archivo, types=[str, int, float])


def leer_precios(nombre_archivo):
    '''Recibe el nombre del archivo a abrir y devuelve la lista con tuplas'''
    return parse_csv(nombre_archivo, types=[str, float], has_headers=False)


def convertir_diccionario(precios_tupla):
    ''' Recibe una lista de tuplas, y las convierte a diccionario.'''   
    precios = {}
    for row in precios_tupla:
        try:
            precios[row[0]] = float(row[1]) #Toma como clave la primera parte de la tupla (el nombre de la fruta) y como valor la segunda(su precio)
        except:
            continue
    return precios 


def hacer_informe(camion, precios):
    '''Genera una lista con tuplas de informacion del camion'''
    lista = []
    for each in camion:
        cambio = precios[each['nombre']] - each['precio'] #Calculo la ganancia
        lista.append((each['nombre'], each['cajones'], each['precio'], cambio))
    return lista


def headers (tupla):
    '''Imprime los encabezados del informe'''
    for header in tupla:
        print(f'{header:>10s}', end='')
    print()
    for header in tupla:
        print(f'{"-"*10} ',end='')
    print()


def imprimir_informe():
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    precios = convertir_diccionario(precios)
    informe = hacer_informe(camion, precios)
   

    headers(('Nombre', 'Cajones', 'Precio', 'Cambio'))
    for nombre, cajones, precio, cambio in informe:
            print(f"{nombre:>10s} {cajones:>10d} {f'${precio:.2f}':>10}{cambio:>10.2f}")

