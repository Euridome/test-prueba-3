import os
limpiar = lambda: os.system("cls")
#Listas
principiantes = {}
avanzados = {}
expertos = {}
#Valores predeterminados
fifa = 0
valorant = 0
fornite = 0
#Funciones principales
def esperar():
    global tecla
    tecla = input("Presione Enter para continuar.")
def registro():
    while True:
        global fornite, fifa, valorant
        limpiar()
        id_jugador = input("Ingrese el id del jugador: ")
        nombre = input("Ingrese el nombre del jugador: ")
        tipo = input("Ingrese el tipo de usuario\n1. Principiante\n2. Avanzado\n3. Experto\nIngrese opcion: ")
        if tipo.isdigit():
            limpiar()
            tipo = int(tipo)
            if tipo == 1:
                limpiar()
                puntos()
                principiantes[id_jugador] = {"Nombre": nombre, "Puntos Valorant":valorant,"Puntos Fornite":fornite,"Puntos FIFA":fifa}
            elif tipo == 2:
                limpiar()
                puntos()
                avanzados[id_jugador] = {"Nombre": nombre, "Puntos Valorant":valorant,"Puntos Fornite":fornite,"Puntos FIFA":fifa}
            elif tipo == 3:
                limpiar()
                puntos()
                expertos[id_jugador] = {"Nombre": nombre, "Puntos Valorant":valorant,"Puntos Fornite":fornite,"Puntos FIFA":fifa}
            elif tipo == 0:
                continue
        else:
            print("Ingrese una opcion valida.")
            esperar()
        
        continuar = input("¿Desea agregar a otro jugador?\n1. Si\n2. No\nIngrese opcion: ")
        if continuar.isdigit():
            continuar = int(continuar)
            if continuar == 1:
                continue
            elif continuar == 2:
                break
            else:
                print("Ingrese una opcion valida.")
                esperar()
        else:
            print("Ingrese una opcion valida.")
            esperar()
        
def puntos():
    global valorant, fornite, fifa
    valorant = 0
    fornite = 0
    fifa = 0
    while True:
        limpiar()
        opcion = input("Seleccione el juego a ingresar puntos, si no desea ingresar mas puntos, marque 0.\n1. Valorant\n2. Fornite\n3. Fifa\nIngrese opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                valorant = input("Ingrese la cantidad de puntos obtenidos: ")
                if valorant.isdigit():
                    valorant = int(valorant)
                    print("Valor ingresado correctamente.")
                    esperar()
                else:
                    print("Valor ingresado no valido, intente nuevamente.")
                    esperar()
            elif opcion == 2:
                fornite = input("Ingrese la cantidad de puntos obtenidos: ")
                if fornite.isdigit():
                    fornite = int(fornite)
                    print("Valor ingresado correctamente.")
                    esperar()
                else:
                    print("Valor ingresado no valido, intente nuevamente.")
                    esperar()
            elif opcion == 3:
                fifa = input("Ingrese la cantidad de puntos obtenidos: ")
                if fifa.isdigit():
                    fifa = int(fifa)
                    print("Valor ingresado correctamente.")
                    esperar()
                else:
                    print("Valor ingresado no valido, intente nuevamente.")
                    esperar()
            elif opcion == 0:
                 break
        else:
            print("Opcion no valida, intente nuevamente.")
            esperar()
def listar():
    print(f"{"ID":<10} {"Nombre":<20} {"Puntaje Valorant":<20} {"Puntaje Fornite":<20} {"Puntaje Fifa":<20}")
    for jugador, datos in principiantes.items():
        print(f"{jugador:<10} {datos["Nombre"]:<20} {datos["Puntos Valorant"]:<20} {datos["Puntos Fornite"]:<20} {datos["Puntos FIFA"]:<20}")
        print()
    for jugador, datos in avanzados.items():
        print(f"{jugador:<10} {datos["Nombre"]:<20} {datos["Puntos Valorant"]:<20} {datos["Puntos Fornite"]:<20} {datos["Puntos FIFA"]:<20}")
        print()
    for jugador, datos in expertos.items():
        print(f"{jugador:<10} {datos["Nombre"]:<20} {datos["Puntos Valorant"]:<20} {datos["Puntos Fornite"]:<20} {datos["Puntos FIFA"]:<20}")
        print()
    esperar()
def impresion_principiantes():
    with open("principiantes.txt","w",newline="") as archivo:
        archivo.write(f"{"ID":<10} {"Nombre":<20} {"Puntaje Valorant":<20} {"Puntaje Fornite":<20} {"Puntaje Fifa":<20}\n")
        for jugador, datos in principiantes.items():
            archivo.write(f"{jugador:<10} {datos["Nombre"]:<20} {datos["Puntos Valorant"]:<20} {datos["Puntos Fornite"]:<20} {datos["Puntos FIFA"]:<20}")
            archivo.write("\n")
    print("Datos de principiantes exportados a TXT.")
def impresion_avanzados():
    with open("avanzados.txt","w",newline="") as archivo:
        archivo.write(f"{"ID":<10} {"Nombre":<20} {"Puntaje Valorant":<20} {"Puntaje Fornite":<20} {"Puntaje Fifa":<20}\n")
        for jugador, datos in avanzados.items():
            archivo.write(f"{jugador:<10} {datos["Nombre"]:<20} {datos["Puntos Valorant"]:<20} {datos["Puntos Fornite"]:<20} {datos["Puntos FIFA"]:<20}")
            archivo.write("\n")
    print("Datos de avanzados exportados a TXT.")
def impresion_expertos():
    with open("expertos.txt","w",newline="") as archivo:
        archivo.write(f"{"ID":<10} {"Nombre":<20} {"Puntaje Valorant":<20} {"Puntaje Fornite":<20} {"Puntaje Fifa":<20}\n")
        for jugador, datos in expertos.items():
            archivo.write(f"{jugador:<10} {datos["Nombre"]:<20} {datos["Puntos Valorant"]:<20} {datos["Puntos Fornite"]:<20} {datos["Puntos FIFA"]:<20}")
            archivo.write("\n")
    print("Datos de expertos exportados a TXT.")
def listar_tipo():
    while True:
        limpiar()
        op1 = input("\t\tTIPOS\t\t\n1. Principiante\n2. Avanzados\n3. Expertos\n4. Volver al menu\nIngrese opcion: ")
        if op1.isdigit():
            op1 = int(op1)
            if op1 == 1:
                limpiar()
                impresion_principiantes()
                esperar()
            elif op1 == 2:
                limpiar()
                impresion_avanzados()
                esperar()
            elif op1 == 3:
                limpiar()
                impresion_expertos()
                esperar()
            elif op1 == 4:
                break
            else:
                print("Ingrese una opcion valida.")
                esperar()
        else:
            print("Entrada no valida, intente nuevamente.")
            esperar()
def app():
    try:
        while True:
            limpiar()
            menu = input("MENU\n1. Registrar puntajes torneo\n2. Listar todos los puntajes\n3. Imprimir por tipo\n4. Salir del programa\nIngrese opcion: ")
            if menu.isdigit():
                menu = int(menu)
                if menu == 1:
                    registro()
                elif menu == 2:
                    limpiar()
                    listar()
                elif menu == 3:
                    listar_tipo()
                elif menu == 4:
                    print("Finalizando programa...")
                    break
                else:
                    print("Ingrese una opcion valida.")
                    esperar()
            else:
                print("Ingrese una opcion valida.")
                esperar()
    except ValueError:
        print("algo salio mal")
app()