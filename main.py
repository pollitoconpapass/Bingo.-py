from bingo import *

#MAIN 
if __name__ == "__main__":
    k = 1
    while True:
        # MENU PANTALLA
        print("\033[33m"," ==== JUEGO de BINGO ====", "\033[34m")
        print("1. Registrarse y Jugar \n2. Salir", "\033[37m" )
        opc = int(input("Ingrese su opcion > "))

        if(opc == 1):
            cant = Datos()
            ImprimeMatriz(k, cant)
            k = k+cant #dada la cantidad, se cuenta desde k + cantidad ingresada
            print("\033[32m")
            listo = input("\nPresione Enter para continuar... ")
            if(listo == ""):
                print("\033[33m")
                JugarBingo()
        
        elif (opc == 2):
            print("\033[33m","\n=== GRACIAS POR JUGAR! ===")
            break
        else:
            print( "\033[31m","INGRESE OPCION VALIDA", "\033[37m")
