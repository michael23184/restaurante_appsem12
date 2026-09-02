import json
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    def __init__(self, ruta_productos="productos.json",
                       ruta_usuarios="usuarios.json",
                       ruta_ventas="ventas.json") -> None:
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

    # ------------------ PRODUCTOS ------------------
    def leer_productos(self) -> list[Producto]:
        try:
            with open(self.ruta_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Producto(**p) for p in datos]
        except FileNotFoundError:
            return []

    def guardar_productos(self, productos: list[Producto]) -> None:
        with open(self.ruta_productos, "w", encoding="utf-8") as f:
            json.dump([p.__dict__ for p in productos], f, ensure_ascii=False, indent=4)

    # ------------------ USUARIOS ------------------
    def leer_usuarios(self) -> list[Usuario]:
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Usuario(**u) for u in datos]
        except FileNotFoundError:
            return []

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        with open(self.ruta_usuarios, "w", encoding="utf-8") as f:
            json.dump([u.__dict__ for u in usuarios], f, ensure_ascii=False, indent=4)

    # ------------------ VENTAS ------------------
    def leer_ventas(self) -> list[Venta]:
        try:
            with open(self.ruta_ventas, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Venta(**v) for v in datos]
        except FileNotFoundError:
            return []

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        with open(self.ruta_ventas, "w", encoding="utf-8") as f:
            json.dump([v.__dict__ for v in ventas], f, ensure_ascii=False, indent=4)