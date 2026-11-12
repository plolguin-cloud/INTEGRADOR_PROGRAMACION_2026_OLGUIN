import Menu
import Gestion_stock


def main():
    Gestion_stock.inicializar()
    while True:
        opcion = Menu.mostrar_menu()
        if opcion == 1:
            Gestion_stock.cargar_stock()
        elif opcion == 2:
            Gestion_stock.mostrar_stock()
        elif opcion == 3:
            categoria = Menu.pedir_categoria()
            Gestion_stock.contar(Gestion_stock.stock_cantidades[categoria])
        elif opcion == 4:
            print("cerrando el sistema")
            break
        else:
            print("Ingrese una opcion válida")


if __name__ == "__main__":
    main()