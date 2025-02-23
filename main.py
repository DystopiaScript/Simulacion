import Metodos.menu as menu
def main():
    while True:
        menu.mostrar_menu()
        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == "1":
           menu.opcion_1()
           break
        elif opcion == "2":
            menu.opcion_2()
            break
        elif opcion == "3":
            menu.opcion_3()
            break
        elif opcion == "4":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()



