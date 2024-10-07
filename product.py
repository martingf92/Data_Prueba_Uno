class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def guardar_producto(self, nuevo_producto):
        self.guardar_producto = nuevo_producto

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Cantidad: {self.cantidad}"



