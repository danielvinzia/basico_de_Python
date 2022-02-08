numeros = [1, 2, 3, 4, 5]
numeros
[1, 2, 3, 4, 5]
numeros.append("hola")
numeros
[1, 2, 3, 4, 5, 'hola']
numeros.pop(5)
'hola'
"hola" + " " + "mundo"
'hola mundo'
numeros2 = [6, 7, 8, 9]
numeros
[1, 2, 3, 4, 5]
numeros2
[6, 7, 8, 9]
lista_final =  numeros + numeros2
lista_final
[1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros * 5
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)
mi_tupla
(1, 2, 3, 4, 5)
# LAS TUPLAS SON LISTAS ESTATICAS, PESAN MENOS PERO NO SE PUEDEN ALTERAR
mi_tupla.append(5)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'
mi_tupla.pop(2)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'pop'
for numero in mi_tupla:
    print(numero)
1
2
3
4
5