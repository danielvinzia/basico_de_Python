def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        ciclos = str(i)
        if i == 1 or i == numero:
            continue
        elif numero % 2 == 0:
            contador += 1
            break
        elif numero % 3 == 0:
            contador += 1
            break
        elif numero % 5 == 0:
            contador += 1
            break
        elif numero % 7 == 0:
            contador += 1
            break
        elif numero % i == 0:
            contador += 1
    print("cantidad de ciclos: " + ciclos)
    if contador == 0:
        return True
    else:
        return False



def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()
