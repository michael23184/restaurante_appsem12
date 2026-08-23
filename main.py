from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto

def menu():
    restaurante = Restaurante()
    restaurante.productos = ArchivoServicio.cargar_productos()

    while True:
        print("\n--- Menu Restaurante ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                producto = Producto(codigo, nombre, precio)
                restaurante.registrar(producto)
                ArchivoServicio.guardar_productos(restaurante.productos)
                print("Producto registrado.")
            elif opcion == "2":
                for p in restaurante.listar():
                    print(p)
            elif opcion == "3":
                codigo = input("Codigo a buscar: ")
                producto = restaurante.buscar(codigo)
                print(producto if producto else "No encontrado.")
            elif opcion == "4":
                codigo = input("Codigo a actualizar: ")
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                restaurante.actualizar(codigo, nombre, precio)
                ArchivoServicio.guardar_productos(restaurante.productos)
                print("Producto actualizado.")
            elif opcion == "5":
                codigo = input("Codigo a eliminar: ")
                restaurante.eliminar(codigo)
                ArchivoServicio.guardar_productos(restaurante.productos)
                print("Producto eliminado.")
            elif opcion == "6":
                break
            else:
                print("Opcion invalida.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
