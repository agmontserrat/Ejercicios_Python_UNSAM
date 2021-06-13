# 5.09) Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas.

# 5.10) Implementá la función album_incompleto(A) que recibe un vector y devuelve True si el álbum A no está completo y False si está completo.

# 5.11) Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) 
#       y devuelva un número entero aleatorio que representa la figurita que nos tocó.

# 5.12) Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), genere un álbum nuevo, 
#       simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.

# 5.13) Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 
#       y guardá en una lista los resultados obtenidos en cada repetición. 
#       Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, 
#       para completar el álbum de seis figuritas.

# 5.14) Calculá n_repeticiones=100 veces la función cuantas_figus(figus_total=670) y guardá los resultados obtenidos en cada repetición en una lista. 
#       Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum (de 670 figuritas).

import random
import numpy as np


def crear_album(figus_total):
    '''Recibe un numero de figuritas, y crea un vector.
    Cada posición representa el estado de una figurita del album con dos valores: 
        0 --- para indicar que aún no la conseguimos 
        1 (o más)--- para indicar que sí'''
    album = np.zeros(figus_total)
    return album

def album_incompleto(A):
    '''Devuelve True si el album esta incompleto, o False si no lo está'''
    return (0 in A)

def comprar_figu(figus_total):
    '''Nos devuelve un entero entre 1 y la cantidad total de figuritas del album.
    Simula la compra de una figurita.'''
    return random.randint(1, figus_total)

def cuantas_figus(figus_total): 
    '''Dado el tamaño del álbum, genera un álbum nuevo, 
    simula su llenado y devuelve la cantidad de figuritas que se debieron comprar para completarlo.'''
    cant_figus = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figu = comprar_figu(figus_total) #Compro una figurita
        cant_figus += 1                  #Incremento contador de figuritas a comprar
        album[figu-1] += 1               #Coloco la figurita en su posición
    return cant_figus

#Ejercicio 5.13 ------------
#n_repeticiones = 1000 
#figus_total = 6
#resultados = [cuantas_figus(figus_total) for x in range(n_repeticiones)]
#print(f"En promedio hay que comprar {np.mean(resultados):.1f} figuritas para completar un album de {figus_total} figuritas en total")
#---------------------------


#Ejercicio 5.14 ------------
n_repeticiones=100
figus_total=670
resultados =  [cuantas_figus(figus_total) for x in range(n_repeticiones)]
print(f"En promedio hay que comprar {np.mean(resultados):.1f} figuritas para completar un album de {figus_total} figuritas en total")