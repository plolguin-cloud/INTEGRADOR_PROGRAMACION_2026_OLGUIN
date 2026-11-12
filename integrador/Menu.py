categorias = ['enlatados', 'frutas', 'congelados', 'panaderia']

def mostrar_menu():
    print("Menú")
    print("1. Cargar stock")
    print("2. Mostrar total del stock")
    print("3. Mostrar cantidad de productos")
    print("4. Salir")
    while True:
        try:
            return int(input("Elija una opción: "))
        except ValueError:
            print("Opción inválida")

def pedir_categoria():
    while True:
        categoria = input("Categoría (" + ", ".join(categorias) + "): ").strip().lower()
        categoria = categoria.replace("í", "i")  
        if categoria in categorias:
            return categoria
        print("Categoría inválida.")