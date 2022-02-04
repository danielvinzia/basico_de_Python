pesos = input("¿Cuantos pesos argentinos tienes?: ")
pesos = float(pesos)
valor_dolar = 218
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + "dólares")