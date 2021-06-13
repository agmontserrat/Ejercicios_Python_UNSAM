# 5.24) Usando tu trabajo en el Ejercicio 4.16 (funcion def lista_de_alturas(arboleda, tipo_arbol) en archivo arboles.py),
#       generá un histograma con las alturas de los Jacarandás en el dataset.

# 5.25) En este ejercicio introducimos un nuevo tipo de gráfico: el gráfico de dispersión o scatterplot. 
#       El mismo usa coordenadas cartesianas para mostrar los valores de dos variables para un conjunto de datos.
#       vamos a graficar un punto en el plano (x,y) por cada árbol en el dataset (o para cada arbol de cierta 
#       especie). 
#       El punto correspondiente a un árbol con diámetro d y altura h será ubicado en la posición x=d y y=h. 
#       Este tipo de gráfico permite visualizar relaciones o tendencias entre las variables y es muy útil en el 
#       análisis exploratorio de datos.
import os
import csv
import matplotlib.pyplot as plt


def leer_arboles(nombre_archivo):
    '''Lee el archivo arbolado-en-espacios-verdes.csv y devuelve una lista diccionarios que representan cada arbol. '''
    arboleda = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila))
            arboleda.append(arbol)
    return arboleda


def lista_de_alturas(arboleda, tipo_arbol=None):
    """Usando comprensión de listas y la variable arboleda, armar la lista de alturas de los Jacarandás solamente.
    Yo le agregué la variable para que podamos agarrar cualquier tipo de arbol
    """
    if tipo_arbol is None:
        return [float(arbol['altura_tot']) for arbol in arboleda]
    return[float(arbol['altura_tot']) for arbol in arboleda if (arbol['nombre_com'] == tipo_arbol)]


def lista_de_diametros(arboleda, tipo_arbol=None):
    """Usando comprensión de listas y la variable arboleda, armar la lista de diametros."""
    if tipo_arbol is None:
        return [float(arbol['diametro']) for arbol in arboleda]
    return[float(arbol['diametro']) for arbol in arboleda if (arbol['nombre_com'] == tipo_arbol)]


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
h = lista_de_alturas(arboleda, 'Jacarandá')
d = lista_de_diametros(arboleda, 'Jacarandá')
plt.scatter(d,h, alpha=0.5)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
plt.show() 