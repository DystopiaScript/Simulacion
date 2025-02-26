def congruencial_lineal(seed, a, c, m, n):
    # Generar n números aleatorios usando el método congruencial lineal
    numeros = []
    Xn = seed  # Semilla inicial
    for _ in range(n):
        Xn = (a * Xn + c) % m
    #    numeros.append(Xn / m)  # Normalizamos el número generado para que esté en [0, 1)
    return numeros

def main():
    # Obtener la semilla y la cantidad de números aleatorios del usuario
    seed = int(input("Ingrese la semilla para el generador de números aleatorios: "))
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    
    # Parámetros del generador congruencial lineal
    a = 1664525    # Multiplicador
    c = 1013904223 # Incremento
    m = 2**32      # Módulo (comúnmente 2^32)

    # Generar los números aleatorios
    numeros_aleatorios = congruencial_lineal(seed, a, c, m, n)

    # Mostrar todos los números generados
    print("\nTodos los números generados:")
    for numero in numeros_aleatorios:
        print(numero)

if __name__ == '__main__':
    main()
