# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
# Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso.
# Probá tu función para la lista ['banana', 'manzana', 'mandarina']


def palabra_geringosa(cadena):
    capadepenapa = ''
    for c in cadena:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p' + c
    return capadepenapa

def diccionario_geringoso(lista):
    diccionario = dict()
    for each in lista:
        palabra = palabra_geringosa(each)
        diccionario[each] = palabra
    return diccionario

lista = ["banana", "manzana", "mandarina"]
diccionario = diccionario_geringoso(lista)
print(diccionario)