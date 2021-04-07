def invertir_lista(lista):
    """ Dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso.
    Aclaración: lo hice con el insert, pero ahora estoy dudando. Creo que el insert es solo de python
    Y la idea era hacer los ejercicios sin los metodos de python"""
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e) #agrego el elemento e al principio de la lista invertida
    return invertida
