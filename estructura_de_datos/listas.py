numero = 1
numero
1
numero = 4
numero
4
numeros = [1, 3, 6, 8, 45, 90]
numeros
[1, 3, 6, 8, 45, 90]
objetos = ["hola", 3, 4.5, True]
objetos
['hola', 3, 4.5, True]
objetos[1]
3
objetos[0]
'hola'
objetos[3]
True
objetos
['hola', 3, 4.5, True]
objetos.append(False)
objetos
['hola', 3, 4.5, True, False]
objetos.append(1)
objetos
['hola', 3, 4.5, True, False, 1]
objetos.pop(1)
3
objetos
['hola', 4.5, True, False, 1]
for elemento in objetos:
    print(elemento)
hola
4.5
True
False
1
objetos[::-1]
[1, False, True, 4.5, 'hola']
objetos[1:3:]
[4.5, True]
