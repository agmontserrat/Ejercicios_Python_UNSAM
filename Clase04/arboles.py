import csv
import pprint
# Ejercicio 4.18: Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, escribí otra leer_
# arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista de diccionarios con la información de todos
# los árboles en el archivo. La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los
#  datos.
def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt', encoding='utf-8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila))
            arboleda.append(arbol)
    return arboleda

def lista_de_alturas(arboleda, tipo_arbol):
    """Usando comprensión de listas y la variable arboleda, armar la lista de alturas de los Jacarandás solamente.
    Yo le agregué la variable para que podamos agarrar cualquier tipo de arbol
    """
    return[float(arbol['altura_tot']) for arbol in arboleda if (arbol['nombre_com'] == tipo_arbol)]


def lista_de_diametros(arboleda, tipo_arbol):
    """Usando comprensión de listas y la variable arboleda, armar la lista de diametros.
        """
    return[float(arbol['diametro']) for arbol in arboleda if (arbol['nombre_com'] == tipo_arbol)]

# Ejercicio 4.20: En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños.
# Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto
# sino también el diámetro de cada Jacarandá en la lista.

def lista_altos_y_diametros(nombre_archivo, tipo_arbol):
    """ Recibe el archivo " ../Data/arbolado-en-espacios-verdes" y el tipo de arbol "Jacarandá" (o el de preferencia)
    y devuelve una lista de tuplas (altura, diametro)
    """
    arboleda = leer_arboles(nombre_archivo)
    tuplas = []
    altos = lista_de_alturas(arboleda, tipo_arbol)
    diametros = lista_de_diametros(arboleda, tipo_arbol)
    for a, d in zip(altos, diametros):
        tuplas.append((a, d))
    return tuplas

# Ejercicio 4.21: vamos a considerar algunas especies de árboles. Por ejemplo:
#        especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
# Te pedimos que armes un diccionario en el que estas especies sean las claves y los valores asociados sean los datos
# que generaste en el ejercicio anterior. Más aún, organizá tu código dentro de una función medidas_de_
# especies(especies,arboleda) que recibe una lista de nombres de especies y una lista como la del
# Ejercicio 4.18 y devuelve un diccionario cuyas claves son estas especies y sus valores asociados sean las medidas
# generadas en el ejercicio anterior.
def medidas_de_especies(especies,arboleda):
    diccionario = {clave: lista_altos_y_diametros('../Data/arbolado-en-espacios-verdes.csv', clave) for clave in especies}
    pprint.pprint(diccionario)

#lista_altos_y_diametros('../Data/arbolado-en-espacios-verdes.csv', 'Jacarandá')

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas_de_especies(especies, arboleda)
