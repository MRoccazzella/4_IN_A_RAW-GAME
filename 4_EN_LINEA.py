#TPO 4 EN LINEA


def solicitarNumero():
 
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Presionar 1 para jugar \nPresionar 2 para ver las reglas\nPresionar 3 para salir\n\n"))
            assert 0 < num < 4
            correcto = True
        except ValueError:
            print("Por favor ingresar un número válido")
        except AssertionError:
            print("Ingrese un numero valido (1,2,3) \n")
    return num

def reglas():
    #Apertura de archivo
    try:
        inicio = open("Reglas.txt",mode="rt",encoding = "UTF8")
        for linea in inicio:
            print(linea)
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo",mensaje)

    except OSError as mensaje:
        print("No se puede leer el archivo",mensaje)

    finally:
#cierre de archivos
        try:
            inicio.close()
        
        except NameError:
            pass

def crearJugadores():    
    
    jugador1 = input("Jugador 1 ingrese su alias de juego por favor: \n\n")
    jugador2 = input("\nJugador 2 ingrese su alias de juego por favor: \n\n")
    return jugador1, jugador2    
            

def crearTablero():
    filas = 7
    columna = 6
    tablero = [["|    |"] * columna for i in range(filas)]
    return tablero

def imprimirTablero(tablero):
    print("  1      2      3      4      5      6  ")
    for f in range(7):
        for c in range(6):
            print(" {:4}".format(tablero[f][c]), end=" ")
        print()
        
def ingresarFicha(tablero,col):
    while True:
        try:
            columna = int(input("Ingrese en que columna va su ficha ( 1, 2, 3, 4, 5, 6 ) \n"))
            assert columna in col
            while tablero[0][columna-1] == "| o |" or tablero[0][columna-1] == "| x |":
                print("La columna escogida esta llena.\n")
                columna = int(input("Ingrese en que columna va su ficha ( 1, 2, 3, 4, 5, 6 ) \n\n")) 
            break
        except ValueError:
            print("Ingrese un valor correcto")
        except AssertionError:
            print("Ese valor no esta en el rango de los permitidos")
    return columna - 1

def actualizarTablero(pieza,tablero,turn):
    filas = 6
    while True:
        if turn % 2 == 1:
            if tablero[filas][pieza] == "|    |":
                tablero[filas][pieza] =  "| o |"
                return filas
        else:
            if tablero[filas][pieza] == "|    |":
                tablero[filas][pieza] = "| x |"
                return filas
        filas -= 1
            
def empatar(tablero):
    cont = 0
    for i in range(6):
        if tablero[0][i] == "| x |" or tablero[0][i] == "| o |":
            cont += 1
    return cont == 6
        
def chequeo_ganador(tablero,col,fila):
    if turno % 2 == 1:
        pieza = "| o |"
    else:
        pieza = "| x |"
#Chequeo horizontal
    for i in range(len(tablero[0]) - 3):
        if tablero[fila][i] == pieza and tablero[fila][i + 1] == pieza and tablero[fila][i + 2] == pieza and tablero[fila][i + 3] == pieza:
            return True
#Chequeo vertical
    for i in range(len(tablero) - 3):
        if tablero[i][col] == pieza and tablero[i + 1][col] == pieza and tablero[i + 2][col] == pieza and tablero[i + 3][col] == pieza:
            return True
#Chequeo diagonal principal
    for i in range(len(tablero[0]) - 3):
        for j in range(len(tablero) - 3):
            if tablero[j][i] == pieza and tablero[j + 1][i + 1] == pieza and tablero[j + 2][i + 2] == pieza and tablero[j + 3][i + 3] == pieza:
                return True
#Chequeo diagonal secundaria            
    for i in range(len(tablero[0]) - 3):
        for j in range(3,len(tablero)):
            if tablero[j][i] == pieza and tablero[j - 1][i + 1] == pieza and tablero[j - 2][i + 2] == pieza and tablero[j - 3][i + 3] == pieza:
                return True
    return False

def cuenta_regresiva(numero):
    
    numero -= 1
    if numero > 0:
        print (numero,"...\n")
        cuenta_regresiva(numero)
    else:
        print ("\nCOMIENZA EL JUEGO\n")
    
# Programa principal

salir = False
turno = 0
celda = ""
columnas = (1,2,3,4,5,6)
while not salir:
    
    victoria = False
    
    print ("Elige una opcion:\n")
 
    opcion = solicitarNumero()
    print("\n\n\n")
    if opcion == 1:
        cuenta_regresiva(6)
        j1,j2 = crearJugadores()
        matriz = crearTablero()
        while not victoria:
            if empatar(matriz):
                print("\n---------------EMPATE---------------\n")
                break
            turno += 1
            if turno % 2 == 1:
                print(f"\nTURNO DE {j1}\n")
            else:
                print(f"\nTURNO DE {j2}\n")
            imprimirTablero(matriz)
            print()
            ficha = ingresarFicha(matriz,columnas)
            print()
            pos_fila=actualizarTablero(ficha,matriz,turno)
            imprimirTablero(matriz)
            print()
            if chequeo_ganador(matriz,ficha,pos_fila): 
                if turno % 2 == 1:
                    print(f"\nEL GANADOR ES {j1}\n")
                    victoria = True
                    turno = 0
                else:
                    print(f"\nEL GANADOR ES {j2}\n")
                    victoria = True
                    turno = 0
    elif opcion == 2:
        reglas()
    elif opcion == 3:
        salir = True


print ("\n------------------FIN------------------")


