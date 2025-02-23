import random
def generationExplication():
    while True:  # Repetir hasta obtener un número válido
        print("Primero generamos un número aleatorio de 4 dígitos")
        randomNumber = random.randint(1000, 9999)
        print("\nNúmero original:", randomNumber)
        print("\nElevamos el número al cuadrado")
        randomNumberSquared = pow(randomNumber, 2)
        print("\nCuadrado:", randomNumberSquared)
        print("\nSi el número no tiene 8 dígitos, agregamos ceros al inicio")
        digits = list(str(randomNumberSquared))
        while len(digits) < 8:
            print("\nAgregamos un 0 al inicio del número")
            digits.insert(0, '0')
            print("\nCuadrado ajustado:", digits)
        if len(digits) == 8:
            print("\nSi no, lo dejamos como esta")
        digits1 = ''.join(digits)
        print("\nExcluimos los 2 primeros y los 2 últimos")
        start = (len(digits1) // 2) - 2
        result = digits1[start:start + 4]
        print("\nDígitos medios:", result)
        print("\nAhora este nuevo numero es la semilla para el siguiente número aleatorio y se repite el proceso")
def Generacion(randomNumber, n):
    size=len(str(randomNumber))
    xi = randomNumber
    ri = []
    for _ in range(n):
        xi = xi ** 2
        c=center(size, xi)
        xi = int(c)
        ri.append(c)
    return ri
def center(size, number):
    number_str = str(number).zfill(size * 2)  # Asegura que tenga el doble de dígitos
    start = (len(number_str) // 2 - size // 2)  # Índice de inicio
    end = start + size  # Índice de fin
    return number_str[start:end]  # Retorna los dígitos centrales