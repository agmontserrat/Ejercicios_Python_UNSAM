#bbinaria.py
# Modificando la función busqueda_binaria(lista, x) adecuadamente, definí una función donde_insertar(lista, x) 
# de forma que reciba una lista ordenada y un elemento y devuelva la posición de ese elemento en la lista 
# (si se encuentra en la lista) o la posición donde se podría insertar el elemento para que la lista permanezca 
# ordenada (si no está en la lista).

# Por ejemplo: el elemento 3 podría insertarse en la posición 2 en la lista [0,2,4,6] para mantenerla ordenada. 
# Por lo tanto, el llamado donde_insertar([0,2,4,6], 3) deberá devolver 2, 
# al igual que el llamado donde_insertar([0,2,4,6], 4).

# Usando lo que hiciste en el parrafo anterior, agregale al archivo bbin.py una función insertar(lista, x) 
# que reciba una lista ordenada y un elemento. 
# Si el elemento se encuentra en la lista solamente devuelve su posición; 
# si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. 
# En este segundo caso, también debe devolver su posición.

def donde_insertar(lista, x):
    '''Recibe una lista ordenada y un elemento.
    Devuelve True y la posición de ese elemento en la lista (si se encuentra en la lista) 
    o False y la posición donde se podría insertar el elemento para que la lista permanezca ordenada (si no está en la lista).'''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado, lo devuelvo!
            return (True,pos)
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    pos = medio #Si dimos vueltas y el elemento no se encontro, guardo la posicion mas cercana

    return (False,pos)

def insertar(lista, x):
    donde = donde_insertar(lista, x) #Me devuelve el True/False y la posicion
    if donde[0] == False: #Si no se encontró, agrego en la posicion en la que deberia estar
        lista.insert(donde[1], x)
    return donde[1] #Devuelvo la posicion
