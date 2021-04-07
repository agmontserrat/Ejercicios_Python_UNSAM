def buscar_u_elemento(lista, e):
    """ Recibe una lista y un elemento
    Devuelve la posición de la última aparición de ese elemento en la lista
    (o -1 si el elemento no pertenece a la lista).
    """
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista):  # recorremos la lista
        if z == e:  # si encontramos a e
            pos = i  # guardamos su posición
    return pos


def buscar_n_elemento(lista, e):
    """ Recibe una lista y un elemento
     Devuelve la cantidad de veces que aparece el elemento en la lista.
     """
    cant = 0  # Comenzamos con el peor caso, no hay apariciones
    for each in lista:
        if each == e:
            cant += 1  # Si encontré el elemento, incremento cant
    return cant


def maximo(lista):
    """Devuelve el máximo de una lista,
    la lista debe ser no vacía.
    """
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = -999999  # Lo inicializo en un numero super bajo
    try:
        for e in lista:  # Recorro la lista y voy guardando el mayor
            if e > m:
                m = e
        return m
    except TypeError:
        print("La funcion maximo() requiere una lista como parametro!")

def minimo(lista):
    """Devuelve el mínimo de una lista,
    la lista debe ser no vacía.
    """
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = 999999  # Lo inicializo en un numero super bajo
    try:
        for e in lista:  # Recorro la lista y voy guardando el mayor
            if e < m:
                m = e
        return m
    except TypeError:
        print("La funcion maximo() requiere una lista como parametro!")

