import csv
from pprint import pprint

#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era que solo evaluaba el primer caracter, y si no cumplia con la condicion devolvia False y terminaba.
#    Lo corregí cambiando el incremento de i, para que se haga siempre y cuando aparezca una a.
#    Y tambien convirtiendo la expresion a minusculas para que abarque todas las "a" posibles.
#    A continuación va el código corregido


def tiene_a(expresion):
    expresion = expresion.lower()
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
    return False


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era que faltaban todos los ":", y que en el if comparaba con un solo "="
#    Al corregirlo tampoco andaba bien con todos los casos de prueba, asi que convertí "expresion" a minusculas para que cuente "UNSAM 2020"


# def tiene_a(expresion):
#     expresion = expresion.lower()
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         i += 1
#     return False


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era que estaba tratando a un int como un string, pidiendole su len() y comparandolo con un caracter
#

def tiene_uno(expresion):
    expresion= str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El metodo nunca devuelve el valor de la suma. La variable c del programa principal no tiene un valor
#   Le agregué el return


def suma(a,b):
    c = a + b
    return c


#%%
#Ejercicio 3.5. Función leer_camion()
# Comentario: Al no crear nuevamente el diccionario cada vez que queremos guardar nueva informacion,
# Dentro de la lista camion quedan lo que nos queda es una lista de muchas copias que hacen referencia al mismo diccionario.


def leer_camion(nombre_archivo):
    camion=[]

    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion


print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))


a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")


camion = leer_camion('../Data/camion.csv')
pprint(camion)