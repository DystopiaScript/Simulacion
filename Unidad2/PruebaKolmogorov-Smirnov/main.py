import numpy as np
from scipy.stats import kstest

def main():
    semilla = int(input("Ingrese la semilla para el generador de números aleatorios: "))
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    # Setear la semilla 
    np.random.seed(semilla)
    # Generar n números aleatorios 
    datos = np.random.rand(n)
    # Mostrar los datos generados
    print("Datos generados:")
    print(datos)  # Puedes imprimir el array completo o iterar si prefieres cada valor en una línea
    
    # Realizar la prueba de Kolmogórov-Smirnov para la distribución uniforme en [0, 1]
    estadistico, p_valor = kstest(datos, 'uniform')
    
    # Mostrar los resultados de la prueba
    print("\nEstadístico K-S:", estadistico)
    print("p-valor:", p_valor)
    
    # Interpretación de resultados (nivel de significancia = 0.05)
    if p_valor < 0.05:
        print("Se rechaza la hipótesis nula: los datos NO siguen una distribución uniforme.")
    else:
        print("No se rechaza la hipótesis nula: los datos podrían seguir una distribución uniforme.")
    input("Presiona Enter para salir...")

if __name__ == '__main__':
    main()
