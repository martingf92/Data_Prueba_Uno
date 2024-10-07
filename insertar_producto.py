import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ",
        database="Datos"
    )
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error: {err}")



import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password=" ",
            database="Datos"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insertar_producto(nombre, precio, cantidad, categoria):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO productos (Nombre, Precio, Cantidad, Categoria) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nombre, precio, cantidad, categoria))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Producto insertado correctamente.")
    else:
        print("No se pudo conectar a la base de datos.")

# Llamada de prueba
insertar_producto("Test Producto", 10.99, 5, "Test Categoria")
