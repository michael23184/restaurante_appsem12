# Proyecto Restaurante POO10

**Autor:** Michael Heras  
**Carrera:** TIC - Segundo semestre  
**Asignatura:** Programación Orientada a Objetos - Semana 10  

## Descripción
Este proyecto implementa un sistema de restaurante en Python utilizando Programación Orientada a Objetos.  
La mejora principal consiste en incorporar **persistencia de productos** mediante un archivo JSON.

## Estructura del proyecto
restaurante_poo10/
├── datos/
│   └── productos.json
├── modelos/
│   ├── init.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── init.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

- **datos/**: contiene el archivo `productos.json` donde se guardan los productos.  
- **modelos/**: define las clases principales (`Producto`, `Usuario`).  
- **servicios/**: maneja la lógica de persistencia (`archivo_servicio.py`) y la gestión de productos (`restaurante.py`).  
- **main.py**: archivo principal que ejecuta el menú interactivo.  
- **README.md**: documentación del proyecto.  

## Ejecución
1. Abrir la carpeta del proyecto en VS Code.  
2. Ejecutar el archivo principal:  
   ```bash
   python main.py
Seleccionar una opción del menú para registrar, listar, buscar, actualizar o eliminar productos.
Ejemplo de uso.
Registrar producto:
Codigo: P001
Nombre: Hamburguesa
Precio: 5.50
El producto se guarda en datos/productos.json y se mantiene al reiniciar el programa.

Al listar productos, se muestra:
P001 - Hamburguesa ($5.5)
Validaciones:
El código y el nombre no pueden estar vacíos.

El precio debe ser mayor a 0.

No se permite registrar dos productos con el mismo código.
Notas.
El archivo productos.json se crea automáticamente al registrar el primer producto.

Se recomienda ejecutar siempre desde la raíz del proyecto.

El repositorio incluye .gitignore para mantener limpio el control de versiones.