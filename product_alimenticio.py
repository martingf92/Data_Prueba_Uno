from product import Producto

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def __str__(self):
        return f"{super().__str__()}, Expira el: {self.fecha_expiracion}"
