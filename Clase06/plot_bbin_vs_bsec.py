import random
import matplotlib.pyplot as plt
import numpy as np


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado, lo devuelvo!
            return (pos,comps)
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               
            izq = medio + 1 # descarto mitad izquierda

    pos = medio #Si dimos vueltas y el elemento no se encontro, guardo la posicion mas cercana
    return pos, comps

def generar_lista(n, m):
    '''Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1'''
    l = random.sample(range(m), k = n)
    l.sort()
    return l


def generar_elemento(m):
    '''Devuelve un elemento aleatorio en el mismo rango de valores (0 y m-1).'''
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0 #Inicializo var en 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    comps_tot = 0 #Inicializo var en 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones en un algoritmo de b binaria sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_secuencial = np.zeros(256) # aca lo mismo pero en un algoritmo de busqueda secuencial.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k) # promedio de comparaciones binario
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista,m,k) #promedio de comparaciones secuencial

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio_binario,label = 'Búsqueda Binaria')
plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de las búsquedas")
plt.xlim(50)
plt.ylim(50)
plt.legend()
plt.show()
