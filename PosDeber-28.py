carrito = {}

# Función para agregar productos al carrito
def agregar_producto(nombre, precio):
    if nombre in carrito:
        carrito[nombre] += precio
    else:
        carrito[nombre] = precio
    print(f"Producto '{nombre}' agregado al carrito.")

#mostrar el contenido del carrito
def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Contenido del carrito:")
        for producto, precio in carrito.items():
            print(f"- {producto}: ${precio:.2f}")
        print(f"Total: ${sum(carrito.values()):.2f}")

# Nueva función para eliminar un producto del carrito
def eliminar_producto():
    if not carrito:
        print("El carrito está vacío. No hay nada que eliminar.")
        return
    
    mostrar_carrito()
    
    producto_a_eliminar = input("Ingresa el nombre del producto que deseas eliminar: ").strip().capitalize()
    
    if producto_a_eliminar in carrito:
        precio_eliminado = carrito.pop(producto_a_eliminar)
        print(f"Producto '{producto_a_eliminar}' eliminado del carrito.")
        print(f"${precio_eliminado:.2f} restado del total.")
    else:
        print(f"El producto '{producto_a_eliminar}' no se encontró en el carrito.")

# Función principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar producto")
        print("2. Mostrar carrito")
        print("3. Eliminar producto")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del producto: ").strip().capitalize()
            try:
                precio = float(input("Ingresa el precio del producto: "))
                agregar_producto(nombre, precio)
            except ValueError:
                print("Por favor, ingresa un precio válido.")
        elif opcion == "2":
            mostrar_carrito()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Llamada a la función principal
main()