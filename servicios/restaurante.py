from modelos.producto import Producto

class Restaurante:
    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def registrar(self, producto: Producto) -> None:
        if any(p.codigo == producto.codigo for p in self.productos):
            raise ValueError("Ya existe un producto con ese codigo.")
        self.productos.append(producto)

    def listar(self) -> list[Producto]:
        return self.productos

    def buscar(self, codigo: str) -> Producto | None:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar(self, codigo: str, nombre: str, precio: float) -> None:
        producto = self.buscar(codigo)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
        else:
            raise ValueError("Producto no encontrado.")

    def eliminar(self, codigo: str) -> None:
        producto = self.buscar(codigo)
        if producto:
            self.productos.remove(producto)
        else:
            raise ValueError("Producto no encontrado.")
