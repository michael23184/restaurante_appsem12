import datetime

class Venta:
    def __init__(self, usuario, producto, cantidad):
        self.usuario = usuario
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total = producto.precio * cantidad

    def to_dict(self):
        return {
            "usuario": self.usuario.nombre,
            "producto": self.producto.nombre,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
            "total": self.total
        }
