import Metodos.generation as generation 
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Explicación de la generación de números aleatorios del metodo de cuadrados medios")
    print("2. Generar lista de números aleatorios")
    print("3. Generar números aleatorios en un archivo")
    print("4. Salir")

def opcion_1():
    generation.generationExplication()

def opcion_2():
    randomNumber = int(input("Ingrese la semilla: "))
    n = int(input("\nIngrese la cantidad de números aleatorios que desea generar: "))
    lista_generada = generation.Generacion(randomNumber, n)  # Capturar la lista
    print("\nLista generada:", lista_generada)  # Mostrar la lista
def opcion_3():
    archive = open("numeros_aleatorios.txt", "w")
    print("\nIngrese la cantidad de números aleatorios que desea generar: ")    
    u = input()
    n = int(u)
    lista = generation.generarLista(n)
    for i in lista:
        archive.write(str(i) + "\n")
        archive.close()
    print("Archivo generado con éxito")
