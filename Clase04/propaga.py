
def propagate(fosforos, pos):
    try:
        if fosforos[pos] == 0:
            fosforos[pos] = 1
            propagate(fosforos, pos - 1)
    except IndexError:
        pass

def propagar(lista):
    fosforos = lista.copy()
    largo = len(fosforos)
    for pos, each in enumerate(fosforos, start = 0):
        if each == 1:
            propagate(fosforos, pos+1)
            propagate(fosforos, pos-1)
    return fosforos

