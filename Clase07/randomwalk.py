import numpy as np
import matplotlib.pyplot as plt


N = 10000 # Largo máximo
cantidad_caminatas = 12 
caminatas = []

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def maximo_y_minimo(caminatas):
    '''
    Devuelve los indices de la lista "caminatas" de las caminatas que mas y menos desvian
    '''
    trayectos = np.absolute(caminatas)
    mayor_devio = 0
    menor_devio = 0
    max = trayectos[0].max()
    min = max

    for i,camino in enumerate(trayectos):
        if camino.max() > max:
            max = camino.max()
            mayor_devio = i
        elif camino.max() < min:
            min = camino.max()
            menor_devio = i
    return (mayor_devio,menor_devio)


plt.figure(figsize=(10, 6), dpi=80)


# Inicia primer subplot, 12 caminatas
plt.subplot(2, 1, 1) # define la figura de arriba
for i in range(cantidad_caminatas):
    caminata = randomwalk(N)
    caminatas.append(caminata)
    plt.plot(caminata)
plt.title("12 caminatas al azar")
plt.yticks([-500,0,500]) # pone las marcas


max,min = maximo_y_minimo(caminatas)

plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot(caminatas[max])
plt.xticks([])
plt.yticks([-500,0,500])
plt.title("La caminata que más se aleja")

plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot(caminatas[min])
plt.xticks([])
plt.yticks([-500,0,500])
plt.title("La caminata que menos se aleja")

plt.show()