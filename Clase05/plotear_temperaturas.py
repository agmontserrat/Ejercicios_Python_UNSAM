import matplotlib.pyplot as plt
import numpy as np



temperaturas = np.load('../Data/temperaturas.npy')
plt.hist(temperaturas,bins=75)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.