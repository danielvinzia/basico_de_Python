def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3958.17)
elif opcion == 2:
    conversor("Argentinos", 105.42)
elif opcion == 3:
    conversor("Mexicanos", 20.71)
else:
    print("Ingresa una opcion correcta por favor")
