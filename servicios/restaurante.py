from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class Restaurante:
    def __init__(self) -> None:
        # Productos
        self.productos: list[Producto] = []
        self.productos_por_codigo: dict[str, Producto] = {}

        # Usuarios
        self.usuarios: list[Usuario] = []
        self.usuarios_por_id: dict[str, Usuario] = {}

        # Ventas
        self.ventas: list[Venta] = []
        self.ventas_por_usuario: dict[str, list[Venta]] = {}

    # ------------------ PRODUCTOS ------------------
    def registrar_producto(self, producto: Producto) -> None:
        if producto.codigo in self.productos_por_codigo:
            raise ValueError("Ya existe un producto con ese código.")
        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(self, codigo: str, nombre: str, precio: float) -> None:
        producto = self.productos_por_codigo.get(codigo)
        if producto:
            producto.nombre = nombre
            producto.precio = precio
        else:
            raise ValueError("Producto no encontrado.")

    def eliminar_producto(self, codigo: str) -> None:
        producto = self.productos_por_codigo.get(codigo)
        if producto:
            self.productos.remove(producto)
            del self.productos_por_codigo[codigo]
        else:
            raise ValueError("Producto no encontrado.")

    # ------------------ USUARIOS ------------------
    def registrar_usuario(self, usuario: Usuario) -> None:
        if usuario.identificacion in self.usuarios_por_id:
            raise ValueError("Ya existe un usuario con esa identificación.")
        self.usuarios.append(usuario)
        self.usuarios_por_id[usuario.identificacion] = usuario

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        return self.usuarios_por_id.get(identificacion)

    def eliminar_usuario(self, identificacion: str) -> None:
        usuario = self.usuarios_por_id.get(identificacion)
        if usuario:
            self.usuarios.remove(usuario)
            del self.usuarios_por_id[identificacion]
        else:
            raise ValueError("Usuario no encontrado.")

    # ------------------ VENTAS ------------------
    def registrar_venta(self, venta: Venta) -> None:
        self.ventas.append(venta)
        if venta.usuario_id not in self.ventas_por_usuario:
            self.ventas_por_usuario[venta.usuario_id] = []
        self.ventas_por_usuario[venta.usuario_id].append(venta)

        # Actualizar stock del producto
        producto = self.productos_por_codigo.get(venta.producto_codigo)
        if producto:
            if producto.stock >= venta.cantidad:
                producto.stock -= venta.cantidad
            else:
                raise ValueError("Stock insuficiente para la venta.")
        else:
            raise ValueError("Producto no encontrado.")

    def listar_ventas(self) -> list[Venta]:
        return self.ventas

    def ventas_por_cliente(self, usuario_id: str) -> list[Venta]:
        return self.ventas_por_usuario.get(usuario_id, [])

   # ------------------ RECONSTRUCCIÓN DE ÍNDICES ------------------
    def cargar_datos(self, archivo_servicio) -> None:
        # Cargar productos desde JSON
        self.productos = archivo_servicio.leer_productos()
        self.productos_por_codigo = {p.codigo: p for p in self.productos}

        # Cargar usuarios desde JSON
        self.usuarios = archivo_servicio.leer_usuarios()
        self.usuarios_por_id = {u.identificacion: u for u in self.usuarios}

        # Cargar ventas desde JSON
        self.ventas = archivo_servicio.leer_ventas()
        self.ventas_por_usuario = {}
        for v in self.ventas:
            if v.usuario_id not in self.ventas_por_usuario:
                self.ventas_por_usuario[v.usuario_id] = []
            self.ventas_por_usuario[v.usuario_id].append(v)