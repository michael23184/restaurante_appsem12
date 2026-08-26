from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.funciones import vender_producto, consultar_ventas_por_usuario

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
        print("6. Registrar usuario")
        print("7. Vender producto")
        print("8. Consultar ventas por usuario")
        print("9. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            producto = Producto(codigo, nombre, precio)
            restaurante.registrar(producto)
            ArchivoServicio.guardar_productos(restaurante.productos)
            print("✅ Producto registrado.")

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
            print("✅ Producto actualizado.")

        elif opcion == "5":
            codigo = input("Codigo a eliminar: ")
            restaurante.eliminar(codigo)
            ArchivoServicio.guardar_productos(restaurante.productos)
            print("✅ Producto eliminado.")

        elif opcion == "6":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            usuario = Usuario(identificacion, nombre, correo)
            print(f"✅ Usuario registrado: {usuario}")

        elif opcion == "7":
            identificacion = input("Identificación del usuario: ")
            nombre = input("Nombre del usuario: ")
            correo = input("Correo: ")
            usuario = Usuario(identificacion, nombre, correo)

            codigo = input("Código del producto: ")
            nombre_prod = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto = Producto(codigo, nombre_prod, precio)
            producto.stock = stock

            cantidad = int(input("Cantidad a vender: "))
            vender_producto(usuario, producto, cantidad)

        elif opcion == "8":
            nombre = input("Ingrese el nombre del usuario: ")
            consultar_ventas_por_usuario(nombre)

        elif opcion == "9":
            break

if __name__ == "__main__":
    menu()
