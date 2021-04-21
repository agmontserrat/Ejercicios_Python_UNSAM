# costo_camion
# En Ejercicio 2.6 escribiste el programa costo_camion.py que lee, 
# mediante una función llamada costo_camion() los datos de un camión y calcula su costo.
# Modificá el archivo costo_camion.py para que use la función informe_funciones.leer_camion() 
# del programa informe_funciones.py.

import os
import informe_funciones as informe



def costo_camion(nombre_archivo):
    suma = 0.0
    camion = informe.leer_camion(nombre_archivo) #Leo con el modulo leer_camion
    for row in camion:
        suma += row['cajones'] * row['precio'] #Saco el precio
    return(suma)


costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
