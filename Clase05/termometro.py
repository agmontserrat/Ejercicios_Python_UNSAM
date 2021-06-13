#Hagamos algún ejercicio sencillo antes de terminar. Supongamos que una persona se compra un termómetro 
# que mide la temperatura con un error aleatorio normal con media 0 y desvío estándar de 0.2 grados (error gaussiano).
# Si la temperatura real de la persona es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) 
# n = 99 valores medidos por el termómetro.
# Ampliá el código de termometro.py que escribiste en el Ejercicio 5.5 para que guarde el vector con las temperaturas 
# simuladas en el directorio Data de tu carpeta de ejercicios, en un archivo llamado temperaturas.npy. Hacé que corra 999 veces en lugar de solo 99.

import random
import numpy as np


def calcular_posibles_numeros():
    lista = []
    for i in range(999):
        #print(f'{random.normalvariate(0,0.2):.2f}', end=', ')
        lista.append(37.5 + random.normalvariate(0,0.2)) # distribución normal
    return lista

def termometro():
    valores = np.array(calcular_posibles_numeros()) #Transformo la lista en arreglo

    print('Valores de termometro ')
    for each in valores:
        print(f'{(each):.2f}') #Imprimo los valores
    
    print(f'Valor máximo: {max(valores):.2f}')
    print(f'Valor minimo: {min(valores):.2f}')
    suma = sum(valores)
    print(f'Promedio: {(suma/len(valores)):.2f}') #Saco el promedio: la suma de todos los valores / cantidad de valores
    temperaturas_ordenada = np.sort(valores)
    mediana = temperaturas_ordenada[int(len(valores)/2)] #Elijo el valor de la mitad del arreglo ordenado
    print(f'Mediana: {mediana:.2f}')

    np.save('../Data/temperaturas.npy', valores)
termometro()