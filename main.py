# Sistema de Gestión Básica de Productos
import os
os.system("cls" if os.name == "nt" else "clear")

productos = [
             ["Teclado", "Periféricos", 15000],
             ["Mouse", "Periféricos", 8000],
             ["Monitor", "Pantallas", 120000]
            ]

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    print("\n=== SISTEMA DE GESTIÓN DE PRODUCTOS ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # AGREGAR PRODUCTO
    if opcion == "1":

        limpiar_pantalla()

        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            nombre = input("Error. Ingrese un nombre válido: ").strip()

        categoria = input("Ingrese la categoría: ").strip()
        while categoria == "":
            categoria = input("Error. Ingrese una categoría válida: ").strip()

        while True:
            precio = input("Ingrese el precio (sin centavos): ")

            if precio.isdigit():
                precio = int(precio)
                break
            else:
                print("Error. Debe ingresar un número válido.")

        producto = [nombre, categoria, precio]
        productos.append(producto)

        print("✅ Producto agregado correctamente.")

        input("\nPulse Enter para volver al menú...")
        limpiar_pantalla()

    # MOSTRAR PRODUCTOS
    elif opcion == "2":

        limpiar_pantalla()

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")

            for i, producto in enumerate(productos, start=1):
                print(
                    f"{i}. Nombre: {producto[0]} | "
                    f"Categoría: {producto[1]} | "
                    f"Precio: ${producto[2]}"
                )
        input("\nPulse Enter para volver al menú...")
        limpiar_pantalla()

    # BUSCAR PRODUCTO
    elif opcion == "3":
        limpiar_pantalla()
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            buscar = input("Ingrese el nombre a buscar: ").strip().lower()

            encontrado = False

            for producto in productos:
                if buscar in producto[0].lower():
                    print(
                        f"Nombre: {producto[0]} | "
                        f"Categoría: {producto[1]} | "
                        f"Precio: ${producto[2]}"
                    )
                    encontrado = True

            if not encontrado:
                print("No se encontraron resultados.")

        input("\nPulse Enter para volver al menú...")
        limpiar_pantalla()

    # ELIMINAR PRODUCTO
    elif opcion == "4":
        limpiar_pantalla()
        if len(productos) == 0:
            print("No hay productos para eliminar.")
        else:
            print("\n--- PRODUCTOS REGISTRADOS ---")

            for i, producto in enumerate(productos, start=1):
                print(f"{i}. {producto[0]}")

            posicion = input("Ingrese el número del producto a eliminar: ")

            if posicion.isdigit():
                posicion = int(posicion)

                if 1 <= posicion <= len(productos):
                    eliminado = productos.pop(posicion - 1)
                    print(f"✅ Producto '{eliminado[0]}' eliminado.")
                else:
                    print("Número fuera de rango.")
            else:
                print("Debe ingresar un número válido.")

            input("\nPulse Enter para volver al menú...")
            limpiar_pantalla()

    # SALIR
    elif opcion == "5":
        print("Gracias por utilizar el sistema.")
        break

    # OPCIÓN INVÁLIDA
    else:
        print("Opción inválida. Intente nuevamente.")