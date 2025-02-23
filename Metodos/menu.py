import Metodos.generation as generation 
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Explicación de la generación de números aleatorios del metodo de cuadrados medios")
    print("2. Generar lista de números aleatorios")
    print("3. Generar números aleatorios en un archivo")
    print("4. Salir")

def opcion_1():
    generation.generationExplication()
    print("\nAhora este nuevo numero es la semilla para el siguiente número aleatorio y se repite el proceso")
    input("Presiona Enter para regresar...")
def opcion_2():
    randomNumber = int(input("Ingrese la semilla de 4 digitos: "))
    n = int(input("\nIngrese la cantidad de números aleatorios que desea generar: "))
    lista_generada = generation.Generacion(randomNumber, n)  # Capturar la lista
    print("\nLista generada:", lista_generada)  # Mostrar la lista
    input("Presiona Enter para regresar...")
def opcion_3():
    randomNumber = int(input("Ingrese la semilla de 4 dígitos: "))
    n = int(input("\nIngrese la cantidad de números aleatorios que desea generar: "))
    lista = generation.Generacion(randomNumber, n)  # Assuming 1234 is the seed
    
    with open("numeros_aleatorios.txt", "w") as archive:  # Usamos "with" para manejar el archivo
        for i in lista:
            archive.write(str(i) + "\n")

    print("Archivo generado con éxito, si llega algún punto donde este llegue a 0000, el programa llegará a un bucle infinito 0000")
    input("Presiona Enter para regresar...")