# Proyecto Restaurante POO10
**Autor:** Michael Heras  
**Carrera:** TIC - Segundo semestre  
**Asignatura:** Programación Orientada a Objetos - Semana 10  

# Restaurante App

## 📌 Descripción 
Sistema de gestión de productos, usuarios y ventas para un restaurante, con persistencia en archivos JSON y optimización mediante colecciones auxiliares.

---

## 📌 Semana 11
- Implementación inicial usando **listas** para almacenar productos, usuarios y ventas.
- Métodos básicos: registrar, listar, buscar, actualizar y eliminar.
- Persistencia en JSON mediante `archivo_servicio.py`.

---

## 📌 Semana 12
Se optimizó el sistema con **diccionarios auxiliares** para mejorar la eficiencia en las búsquedas:

- **Productos**
  - Lista principal: `self.productos`
  - Índice auxiliar: `self.productos_por_codigo`
  - Búsqueda rápida por código.

- **Usuarios**
  - Lista principal: `self.usuarios`
  - Índice auxiliar: `self.usuarios_por_id`
  - Búsqueda rápida por identificación.

- **Ventas**
  - Lista principal: `self.ventas`
  - Índice auxiliar: `self.ventas_por_usuario`
  - Consultas rápidas de ventas por cliente.
  - Actualización automática de stock al registrar una venta.

- **Reconstrucción de índices**
  - Al cargar datos desde JSON, se reconstruyen los diccionarios auxiliares para mantener la eficiencia.

---

## 📌 Archivos del proyecto
- `modelos/producto.py` → Clase Producto con validaciones y conversión a diccionario.
- `modelos/usuario.py` → Clase Usuario con atributos básicos y conversión a diccionario.
- `modelos/venta.py` → Clase Venta con referencias por ID y conversión a diccionario.
- `servicios/restaurante.py` → Lógica principal con colecciones optimizadas.
- `servicios/archivo_servicio.py` → Lectura y escritura de JSON.
- `main.py` → Menú interactivo para pruebas.
- `productos.json`, `usuarios.json`, `ventas.json` → Archivos de persistencia.

---

## 📌 Pruebas mínimas
1. Registrar producto, usuario y venta.
2. Buscar producto por código.
3. Buscar usuario por identificación.
4. Consultar ventas de un usuario.
5. Verificar actualización de stock.
6. Cerrar y volver a abrir el programa para comprobar reconstrucción de índices.

---

## 📌 Ejecución
```bash
python main.py