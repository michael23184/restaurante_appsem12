from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

def menu():
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()

    # Cargar datos desde JSON
    restaurante.cargar_datos(archivo_servicio)

    while True:
        print("\n--- Menú Restaurante ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Registrar usuario")
        print("7. Registrar venta")
        print("8. Consultar ventas por usuario")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto = Producto(codigo, nombre, precio, stock)
            restaurante.registrar_producto(producto)
            archivo_servicio.guardar_productos(restaurante.productos)
            print("✅ Producto registrado.")

        elif opcion == "2":
            for p in restaurante.listar_productos():
                print(p)

        elif opcion == "3":
            codigo = input("Código del producto: ")
            producto = restaurante.buscar_producto(codigo)
            print(producto if producto else "Producto no encontrado.")

        elif opcion == "4":
            codigo = input("Código: ")
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))
            try:
                restaurante.actualizar_producto(codigo, nombre, precio)
                archivo_servicio.guardar_productos(restaurante.productos)
                print("✅ Producto actualizado.")
            except ValueError as e:
                print(e)

        elif opcion == "5":
            codigo = input("Código: ")
            try:
                restaurante.eliminar_producto(codigo)
                archivo_servicio.guardar_productos(restaurante.productos)
                print("✅ Producto eliminado.")
            except ValueError as e:
                print(e)

        elif opcion == "6":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            usuario = Usuario(identificacion, nombre, correo)
            restaurante.registrar_usuario(usuario)
            archivo_servicio.guardar_usuarios(restaurante.usuarios)
            print("✅ Usuario registrado.")

        elif opcion == "7":
            usuario_id = input("ID del usuario: ")
            producto_codigo = input("Código del producto: ")
            cantidad = int(input("Cantidad: "))
            venta = Venta(usuario_id, producto_codigo, cantidad)
            try:
                restaurante.registrar_venta(venta)
                archivo_servicio.guardar_ventas(restaurante.ventas)
                print("✅ Venta registrada.")
            except ValueError as e:
                print(e)

        elif opcion == "8":
            usuario_id = input("ID del usuario: ")
            ventas = restaurante.ventas_por_cliente(usuario_id)
            if ventas:
                for v in ventas:
                    print(v)
            else:
                print("No hay ventas para este usuario.")

        elif opcion == "9":
            print("👋 Saliendo del sistema...")
            break

if __name__ == "__main__":
    menu()