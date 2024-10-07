import mysql.connector

def conectar_bd():
    conexion = mysql.connector.connect(
        host="localhost",  # Cambia por tu host
        user="root",  # Cambia por tu usuario
        password="",  # Cambia por tu contraseña
        database="Datos"  # Cambia por tu base de datos
    )
    return conexion

def crear_tablas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            cantidad INT NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()

# Ejecutar la creación de tablas
crear_tablas()

def agregar_producto(nombre, precio, cantidad):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute('''
        INSERT INTO productos (nombre, precio, cantidad)
        VALUES (%s, %s, %s)
    ''', (nombre, precio, cantidad))

    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    conexion.close()
    return productos


def actualizar_producto(id, nombre, precio, cantidad):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute('''
        UPDATE productos
        SET nombre = %s, precio = %s, cantidad = %s
        WHERE id = %s
    ''', (nombre, precio, cantidad, id))

    conexion.commit()
    conexion.close()


def eliminar_producto(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute('DELETE FROM productos WHERE id = %s', (id,))

    conexion.commit()
    conexion.close()



