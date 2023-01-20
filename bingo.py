# --- LIBRERIAS ---
import os
import pandas as pd
import random

# --- LISTAS ---
nombres = []
cantidades = []
numeros_bingo = []
numeros_ganadores = []
dicc = {}
dicc_bingoganador = {}

# --- FUNCIONES DEL JUEGO ---
def Datos(): # Le pide datos al usuario / jugador
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)
    cant= input(f"{nombre} cuantos bingos deseas: ")
    cantidades.append(cant)

    return int(cant)

def Unico(x, l): # Verific q los numeros sean unicos
    esUnico = True
    for i in range(len(l)):
        if x == l[i]: # si se repite 
            esUnico = False
            break
    return esUnico

def Numeros(men, may): # Sortea los numeros
    l = []
    j = 0
    while j < 5:
        x = random.randint(men, may)
        if Unico(x,l): # -> si es verdadero entonces...
            l.append(x) # agregar a la lista
            j+= 1 
    return l

def ImprimeMatriz(k,cant): # -> Mostrara los bingos en la pantalla
    cont = 0
    while cont < cant:
        lin1 = Numeros(1, 15)
        lin2 = Numeros(16, 30)
        lin3 = Numeros(31, 45)
        lin4 = Numeros(46, 60)
        lin5 = Numeros(61, 75)

        dataframe = pd.DataFrame({"B": lin1, "I": lin2,"N":lin3, "G":lin4, "O": lin5})
        print("\033[35m","Num. Bingo:",k+cont, "\033[33m")
        dicc[f"{cont+k}"] = lin1 + lin2 + lin3 + lin4 + lin5 # -> almacena el bingo creado
        dicc_bingoganador[f"{cont+k}"] = lin1 + lin2 + lin3 + lin4 + lin5 # -> copia del bingo ganador
        print(dataframe.to_string(index = False))
        print("\n")
        cont += 1

def EmpezarJuego(dicc, dicc_bingoganador): # -> Comenzara el juego
    while True:
        tecla = input("Ingrese J para jugar: ")
        if(tecla == "j" or tecla == "J"):
            x = random.choice(numeros_bingo)
            num = x # para que al borrarlo de la lista, se quede en otra variable
            numeros_bingo.remove(x)
            llave = list(dicc.keys())
            llave_bingos = list(llave)
            for i in range(len(llave_bingos)):
                l = dicc[llave_bingos[i]]
                for j in range(len(l)):
                    if(l[j] == num):
                        numeros_ganadores.append(num)
            os.system("cls") # limpiar pantalla
            for a in range(len(llave_bingos)):
                l = dicc[llave_bingos[a]]
                for b in range(len(l)):
                    if(l[b] == num): #si el numero esta dentro de mi bingo,
                        l[b] = f"X" # lo cambio por una x
                        datito = llave_bingos[a] 
                        print("\033[34m")
                        print(f"\nSe eligio el {num}\n")
                        print("\033[33m")
                        dataframe = pd.DataFrame({"B":l[0:5], "I":l[5:10], "N":l[10:15], "G": l[15:20], "O":l[20:25]})
                        print("Num. ",datito, "\n")
                        print(dataframe.to_string(index = False))
                        # Determinar Ganador
                        if len(set(l)) == 1: # si la lista solo tiene un elemento -> x
                            os.system("cls")
                            datito = llave_bingos[a] 
                            listita = dicc_bingoganador[datito]
                            dataframe = pd.DataFrame({"B":l[0:5], "I":l[5:10], "N":l[10:15], "G": l[15:20], "O":l[20:25]})
                            print("\n")
                            print(dataframe.to_string(index = False))
                            print("\nNum", datito)
                            print("\033[35m","¡Felicidades!")
                            print("BINGO GANADOR", "\033[33m")
                            dataframe = pd.DataFrame({"B":listita[0:5], "I":listita[5:10], "N":listita[10:15], "G": listita[15:20], "O":listita[20:25]})
                            print("\n")
                            print(dataframe.to_string(index = False))
                            exit()


def AlmacenaNumeros(): # -> lo almacena en la lista de numeros utilizados
    for i in range(1,76):
        numeros_bingo.append(i)

def JugarBingo(): # -> ya que no se puede enviar el diccionario como parametro en main
    os.system("cls")
    AlmacenaNumeros()
    EmpezarJuego(dicc, dicc_bingoganador) 
