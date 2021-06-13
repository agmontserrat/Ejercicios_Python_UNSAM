# Ejercicio 7.9
# Modificá el siguiente código para reproducir el gráfico que se muestra. 
# Prestá atención a cómo se numeran los subplots.


import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 3x3
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segundaa de abajo, que sería la quinta si fuera una grilla regular de 3x3
plt.axhline(0.5)
plt.plot()
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la tercera de abajo, que sería la sexta figura si fuera una grilla regular de 3x3
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()