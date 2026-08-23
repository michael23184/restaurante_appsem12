import json
import os
from modelos.producto import Producto

class ArchivoServicio:
    RUTA = "datos/productos.json"

    @staticmethod
    def cargar_productos() -> list[Producto]:
        productos = []
        if not os.path.exists(ArchivoServicio.RUTA):
            return productos
        try:
            with open(ArchivoServicio.RUTA, "r", encoding="utf-8") as f:
                data = json.load(f)
                for registro in data:
                    try:
                        producto = Producto(
                            codigo=registro["codigo"],
                            nombre=registro["nombre"],
                            precio=float(registro["precio"])
                        )
                        productos.append(producto)
                    except (KeyError, ValueError):
                        print("Registro invalido en JSON, se omitio.")
        except json.JSONDecodeError:
            print("Error: El archivo JSON esta corrupto.")
        except PermissionError:
            print("Error: No hay permisos para leer el archivo.")
        return productos

    @staticmethod
    def guardar_productos(productos: list[Producto]) -> None:
        try:
            with open(ArchivoServicio.RUTA, "w", encoding="utf-8") as f:
                data = [p.to_dict() for p in productos]
                json.dump(data, f, ensure_ascii=False, indent=4)
        except PermissionError:
            print("Error: No hay permisos para escribir el archivo.")
