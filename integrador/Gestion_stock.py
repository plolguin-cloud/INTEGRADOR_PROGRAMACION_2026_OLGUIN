import menu

stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}


def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []


def cargar_stock():
    categoria = menu.pedir_categoria()
    producto = input("Producto a añadir: ").strip()
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad >= 0:
                break
            print("La cantidad debe ser positiva")
        except ValueError:
            print("Ingrese un número entero.")
    stock_productos[categoria].append(producto)
    stock_cantidades[categoria].append(cantidad)
    print(f"Se cargaron {cantidad} de '{producto}' en {categoria}")


def mostrar_stock():
    print("Stock de productos:")
    for categoria, productos in stock_productos.items():
        print(f"{categoria}: {productos}")
    print("Stock de cantidades:")
    for categoria, cantidades in stock_cantidades.items():
        print(f"{categoria}: {cantidades}")


def contar(lista_productos):
    print(f"Cantidad de productos: {len(lista_productos)}")
    print(f"Suma de las cantidades: {sum(lista_productos)}")