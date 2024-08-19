from product import Producto

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia

    def __str__(self):
        return f"{super().__str__()}, Garantía: {self.garantia} años"
