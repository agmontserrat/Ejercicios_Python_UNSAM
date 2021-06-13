esta carpeta contiene los archivos .py correspondientes a la ejercitación de la clase 5

Apuntes:

Elecciones con reposición:
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras)) ------- para varios elementos print(random.choices(caras,k=5))


Elecciones sin reposición:
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.sample(naipes,k=3) --- saca 3 cartas. la variable k no puede ser mayor que la cantidad total de cartas


