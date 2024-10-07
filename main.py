import mysql.connector
from product_electronico import ProductoElectronico
from product_alimenticio import ProductoAlimenticio

# def crear_tabla():
#     conn = mysql.connector.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS productos
#                       (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL, cantidad INTEGER, categoria TEXT, atributo_extra TEXT)''')
#     conn.commit()
#     conn.close()

# def agregar_producto(producto):
#     conn = mysql.connector.connect('database.db')
#     cursor = conn.cursor()
#     categoria = producto.__class__.__name__
#     atributo_extra = producto.garantia if categoria == "ProductoElectronico" else producto.fecha_expiracion
#     cursor.execute('''INSERT INTO productos (nombre, precio, cantidad, categoria, atributo_extra)
#                       VALUES (?, ?, ?, ?, ?)''', (producto.nombre, producto.precio, producto.cantidad, categoria, atributo_extra))
#     conn.commit()
#     conn.close()

# def leer_productos():
#     conn = mysql.connector.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM productos")
#     productos = cursor.fetchall()
#     conn.close()
#     return productos

# def actualizar_producto(id, campo, nuevo_valor):
#     conn = mysql.connector.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute(f"UPDATE productos SET {campo} = ? WHERE id = ?", (nuevo_valor, id))
#     conn.commit()
#     conn.close()

# def eliminar_producto(id):
#     conn = mysql.connector.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
#     conn.commit()
#     conn.close()

# def guardar_en_json():
#     productos = leer_productos()
#     with open('inventory.json', 'w') as f:
#         mysql.dump(productos, f)

# def main():
#     crear_tabla()

#     # Crear productos de ejemplo
#     p1 = ProductoElectronico("Laptop", 1000, 5, 2)
#     p2 = ProductoAlimenticio("Manzana", 1, 100, "2024-12-31")

#     # Agregar productos a la base de datos
#     agregar_producto(p1)
#     agregar_producto(p2)

#     # Leer y mostrar productos
#     productos = leer_productos()
#     for producto in productos:
#         print(producto)

#     # Guardar en archivo JSON
#     guardar_en_json()

# if __name__ == "__main__":
#     main()

# main.py

# from product import Producto
# import db

# # Funciones CRUD
# def agregar_producto():
#     tipo = input("Tipo de producto (1: General, 2: Electrónico, 3: Alimenticio): ")
#     nombre = input("Nombre del producto: ")
#     precio = float(input("Precio del producto: "))
#     cantidad = int(input("Cantidad en stock: "))

#     if tipo == "1":
#         producto = Producto(nombre, precio, cantidad)
#     elif tipo == "2":
#         garantia = int(input("Garantía (años): "))
#         producto = ProductoElectronico(nombre, precio, cantidad, garantia)
#     elif tipo == "3":
#         fecha_expiracion = input("Fecha de expiración (YYYY-MM-DD): ")
#         producto = ProductoAlimenticio(nombre, precio, cantidad, fecha_expiracion)
#     else:
#         print("Tipo de producto no válido.")
#         return
    
#     db.guardar_producto(producto)
#     print("Producto agregado exitosamente.")

# def eliminar_producto():
#     productos = db.eliminar_producto()
#     if not productos:
#         print("No hay productos para eliminar.")
#         return

#     for idx, producto in enumerate(productos, start=1):
#         print(f"{idx}. {producto['nombre']} - ${producto['precio']} - Cantidad: {producto['cantidad']}")
    
#     indice = int(input("Ingrese el número del producto a eliminar: "))
#     if 1 <= indice <= len(productos):
#         productos.pop(indice - 1)
#         with open('productos.json', 'w') as f:
#             for producto in productos:
#                 mysql.dump(producto, f)
#                 f.write('\n')
#         print("Producto eliminado exitosamente.")
#     else:
#         print("Índice no válido.")

# def modificar_producto():
#     productos = db.actualizar_producto()
#     if not productos:
#         print("No hay productos para modificar.")
#         return

#     for idx, producto in enumerate(productos, start=1):
#         print(f"{idx}. {producto['nombre']} - ${producto['precio']} - Cantidad: {producto['cantidad']}")
    
#     indice = int(input("Ingrese el número del producto a modificar: "))
#     if 1 <= indice <= len(productos):
#         producto = productos[indice - 1]
#         nombre = input(f"Nombre ({producto['nombre']}): ") or producto['nombre']
#         precio = input(f"Precio ({producto['precio']}): ") or producto['precio']
#         cantidad = input(f"Cantidad ({producto['cantidad']}): ") or producto['cantidad']
        
#         producto['nombre'] = nombre
#         producto['precio'] = float(precio)
#         producto['cantidad'] = int(cantidad)
        
#         with open('productos.json', 'w') as f:
#             for p in productos:
#                 mysql.dump(p, f)
#                 f.write('\n')
#         print("Producto modificado exitosamente.")
#     else:
#         print("Índice no válido.")

# def listar_productos():
#     productos = db.cargar_productos()
#     if not productos:
#         print("No hay productos disponibles.")
#         return

#     for producto in productos:
#         print(producto)

# # Menú principal
# def main():
#     while True:
#         print("\nSistema de Gestión de Productos")
#         print("1. Agregar producto")
#         print("2. Eliminar producto")
#         print("3. Modificar producto")
#         print("4. Listar productos")
#         print("5. Salir")
        
#         opcion = input("Seleccione una opción: ")

#         if opcion == "1":
#             agregar_producto()
#         elif opcion == "2":
#             eliminar_producto()
#         elif opcion == "3":
#             modificar_producto()
#         elif opcion == "4":
#             listar_productos()
#         elif opcion == "5":
#             print("Saliendo del sistema...")
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# if __name__ == "__main__":
#     main()


import db

# Funciones CRUD
def agregar_producto():
    tipo = input("Tipo de producto (1: General, 2: Electrónico, 3: Alimenticio): ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en stock: "))

    if tipo == "1":
        db.agregar_producto(nombre, precio, cantidad)
    elif tipo == "2":
        garantia = int(input("Garantía (años): "))
        db.agregar_producto(nombre, precio, cantidad, categoria="Electronico", garantia=garantia)
    elif tipo == "3":
        fecha_expiracion = input("Fecha de expiración (YYYY-MM-DD): ")
        db.agregar_producto(nombre, precio, cantidad, categoria="Alimenticio", fecha_expiracion=fecha_expiracion)
    else:
        print("Tipo de producto no válido.")
        return

    print("Producto agregado exitosamente.")

def eliminar_producto():
    listar_productos()
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    db.eliminar_producto(id_producto)
    print("Producto eliminado exitosamente.")

def modificar_producto():
    listar_productos()
    id_producto = int(input("Ingrese el ID del producto a modificar: "))
    nombre = input("Nuevo nombre: ")
    precio = float(input("Nuevo precio: "))
    cantidad = int(input("Nueva cantidad: "))

    db.actualizar_producto(id_producto, nombre, precio, cantidad)
    print("Producto modificado exitosamente.")

def listar_productos():
    productos = db.obtener_productos()
    if not productos:
        print("No hay productos disponibles.")
    else:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")

# Menú principal
def main():
    while True:
        print("\nSistema de Gestión de Productos")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Modificar producto")
        print("4. Listar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            listar_productos()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
