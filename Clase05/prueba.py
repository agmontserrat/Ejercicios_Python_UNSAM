import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[0]) # si tiene múltiples dimensiones, esto me da una "rebanada" de una dimensión menos

print(a[2]) # otra rebanada

print(a[2][3]) # accedo al cuarto elemento del tercer vector de a (sí, se cuentan primero filas, luego columnas).

print(a[2,3]) # o, equivalentemente, accedo al elemento en la tercera fila y cuarta columna de a

print(np.zeros(2)) #Creo arreglo de ceros

print(np.ones(2)) #Y a partir de unos

print(np.empty(2)) #Lo bueno de usar empty en lugar de zeros (o ones) es la velocidad - al no inicilizar los valores no perdemos tiempo. 

print(np.arange(4)) #crea a partir de un rango de valores

print(np.arange(2,10,2)) #contiene elementos equiespaciados, especificando el primer número, el límite, y el paso. El límite derecho nunca está en la lista.

print(np.linspace(0, 10, num=5)) #para crear un vector de valores equiespaciados especificando el primer número, el último número, y la cantidad de elementos

#Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange(). 
# Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?

conArange = np.arange(1,20,2)
conLinspace = np.linspace(1,19,10)
print(conArange)
print(conLinspace)

#Si no lo especificás, el tipo de datos (por omisión) de los arreglos es el punto flotante (np.float64). 
# Sin embargo, podés explicitar otro tipo de datos usando la palabra clave dtype.
x = np.ones(2, dtype=np.int64)

#En estos dos casos el 64 de los tipos de datos se refiere a la cantidad de bits usados para representar el número en el sistema binario: 64 bits.

#Ordenar un vector es sencillo usando np.sort()
#Fijate que el vector arr quedó desordenado. sort simplemente devolvió una copia ordenada de los datos pero no modificó el original.
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

#Otra operación usual es la concatenación. Si empezás con estos dos vectores:
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a, b)))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))


#Conocer el tamaño
#ndarray.ndim te dice la cantidad de ejes (o dimensiones) del arreglo.
#ndarray.shape te va a dar una tupla de enteros que indican la cantidad de elementos en cada eje. Si tenés una matriz con 2 filas y 3 columnas de va a dar (2, 3).
#ndarray.size te dice la cantidad de elementos (cantidad de números) de tu arreglo. Es el producto de la tupla shape. En el ejemplo del renglón anterior, el size es 6.

array_ejemplo=(np.array([ [[1,1,1,1], [2,2,2,2]], [[1,1,1,1], [2,2,2,2]],[[1,1,1,1], [2,2,2,2]] ]))
print (array_ejemplo.ndim)
print( array_ejemplo.shape) #3 filas, 2 listas en cada una,  4 elementos?
print( array_ejemplo.size)#3*2*4

#arr.reshape() le podés dar una nueva forma a tu arreglo sin cambiar los datos.
#Solo tené en cuenta que antes y después del reshape el arreglo tiene que tener la misma cantidad de elementos. 
a = np.arange(6)
b = a.reshape(3, 2)

#Agregar un nuevo eje a un arreglo
#tenemos un vector con n elementos y necesitamos pensarlo como una matriz de una fila y n columnas o de n filas y una columna. 
# Podés usar np.newaxis para agregarle dimensiones a un vector existente.
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape) #da (6,)

#Podés usar np.newaxis para agregarle una dimensión y convertirlo en un vector fila:
vec_fila = a[np.newaxis, :]
print(vec_fila)
print(vec_fila.shape)

#O, para convertirlo en un vector columna, podés unsertar un eje en la segunda dimensión:
vec_col = a[:, np.newaxis]
print(vec_col)
print(vec_col.shape)


#Índices y rebanadas
#Podés indexar y rebanar arreglos de numpy como hicimos con las listas.
data = np.array([1, 2, 3, 4, 5, 6, 7])
print(data[1])
print(data[0:2])
print(data[-2:])
print(data[data < 2]) #todos los valores menores a 2
five_up = (data >= 5) #da un arreglo de valores booleanos. 
print(data[five_up])
pares = data[data%2==0] 
print(pares)
c = data[(data > 2) & (data < 11)]
print(c)
#Finalmente, podés usar np.nonzero() para obtener las coordenadas de ciertos elementos de un arreglo.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#Podés usar np.nonzero() para imprimir los índices de los elementos que son, digamos, menores que 5:
b = np.nonzero(a < 5)
print(b) # El primer arreglo representa las filas de los elementos que satisfacen la condición y el segundo sus columnas.
#Si querés generar la lista de coordenadas donde se encuentran estos elementos, podés zipear los arreglos, convertir el resultado en una lista e imprimirla:
lista_de_coordenadas = list(zip(b[0], b[1]))

#Surge naturalmente la pregunta: ¿porqué tengo que convertir el objeto zip a una lista? Veremos en la segunda mitad de la materia más detalles sobre generadores en Python para entender exactamente lo que está pasando aquí. 
# Simplemente digamos que al zipear b[0] y b[1] no se genera la lista realmente, sino potencialmente. Sólo al solicitar sus elementos (iterando sobre ello o con list) se generan realmente las coordenadas.
for coord in lista_de_coordenadas:
    print(coord)



#Crear arreglos usando datos existentes
# Podés crear otro arreglo a partir de una sección de a, simplemente especificando qué parte querés.
a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]
# Es importante saber que este método genera una vista del arreglo original y no una verdadera copia. Si modificás un elemento de la vista, 
# ¡también se modificará en el original!
# Podés usar el método copy para copiar los datos.


#Broadcasting

# Hay veces en que necesitás realizar una operación entre un arreglo y un número (en matemática le decimos, un escalar). 
# Por ejemplo tenés un vector con distancias en millas (lo llamamos "data") y lo necesitás convertir a distancias en kilómetros.
# Podés hacer esta operación así:

data = np.array([1.0, 2.0])
data * 1.6

#numpy entiende que la multiplicación debe ocurrir en cada celda del vector. Este concepto se llama broadcasting. 
# El mecanismo de broadcasting le permite a numpy realizar operaciones en arreglos de diferente tamaño, pero los tamaños deben ser compatibles. 
# Por ejemplo si ambos arreglos tienen el mismo tamaño o si uno tiene tamaño 1 (escalar). 
# Si los tamaños no son compatibles, te va a dar un ValueError.

# numpy también te permite realizar operaciones que resumen los datos.
#  Además de min, max, y sum, podés usar mean para obtener el promedio, prod para calcular el producto, 
# std para obtener el desvío estándar de los datos, y más.