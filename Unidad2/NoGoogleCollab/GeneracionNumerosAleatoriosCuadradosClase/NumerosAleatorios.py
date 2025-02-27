#Semilla inicial
semilla = 2005
n = 4  # Define the number of digits to extract
iteraciones = 10  # Define the number of iterations
resultados = []
for _ in range(iteraciones):
  #Elevar la semilla al cuadrado
  cuadrado = str(semilla ** 2).zfill(2 * n) #Agregar los espacios necesarios
  #Extraer los dígitogs centraoles 
  inicio = (len(cuadrado)- n)//2
  semilla=int(cuadrado[inicio:inicio+n])
  resultados.append(semilla)

  #Imprimir resultados
  for i, numero in enumerate(resultados, 1):
    print(f"Número Aleatorio {i}: {numero}")

