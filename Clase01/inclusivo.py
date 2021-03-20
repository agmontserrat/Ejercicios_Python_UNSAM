# Traductor (rústico) al lenguaje inclusivo
# Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra.
# Completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'.
# Por ejemplo 'todos somos programadores' pasaría a ser 'todes somes programadores'.

frase = 'Todos somos programadores'
palabras = frase.split()
frase_t= ""
for palabra in palabras:
    if (palabra[-1] == 'o'):
        palabre = palabra[:-1] + 'e'
    elif len(palabra)>=2 and palabra[-2] == 'o':
        palabre = palabra[:-2] + 'e' + palabra[-1]
    else: palabre = palabra
    frase_t += palabre + ' '
print(frase_t)

