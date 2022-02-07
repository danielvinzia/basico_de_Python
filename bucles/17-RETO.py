def main():
    print("Ingresa que vez en el cielo: ")
    variable = input("Escribe 1 para nube, 2 para trueno, 3 para megarayo o 4 para supernova: ")
    trueno = 0
    while trueno < 5:
        if variable == "1":
            print("se necesitan truenos para cargar la energia, seguir esperando")
            variable = input(
                "Escribe 1 para nube, 2 para trueno, 3 para megarayo o 4 para supernova: ")
        elif variable == "2":
            print("los truenos estan cargando las celdas, ya falta menos :)")
            trueno += 1
            if trueno == 5:
                print("Sistema cargado")
                break
            variable = input(
                "Escribe 1 para nube, 2 para trueno, 3 para megarayo o 4 para supernova: ")
        elif variable == "3":
            print("super carga :0")
            break
        elif variable == "4":
            print("Destruccion del sistema :.(")
            break


if __name__ == '__main__':
    main()
    