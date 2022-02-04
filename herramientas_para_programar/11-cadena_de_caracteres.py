# USANDO METODOS 
#¿Cual es tu nombre?: daniel
nombre
'daniel '
# cambio a mayusculas
nombre.upper()
'DANIEL '
# pongo la primera en mayusculsa y el resto en minusculas
nombre.capitalize()
'Daniel '
nombre
'daniel '
# guardo los cambios
nombre = nombre.capitalize()
nombre
'Daniel '
# borro los espacios de mas
nombre = nombre.strip()
nombre
'Daniel'
# lo paso a minusculas
nombre = nombre.lower()
nombre
'daniel'
# remplazo una letra por otra
nombre = nombre.replace("n","d")
nombre
'dadiel'
# la cadena de caracteres se recorre como un arreglo
nombre[0]
'd'
nombre[1]
'a'
letra = nombre[3]
letra
'i'
# longitud de lineas de caracter
len(nombre)
6
len(letra)
1
len("Hola este es el curso de python")
31
