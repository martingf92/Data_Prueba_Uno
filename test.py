# test_producto.py

import unittest
from product import Producto

class TestProducto(unittest.TestCase):

    def test_producto_str(self):
        p = Producto("Laptop", 1000.0, 5)
        self.assertEqual(str(p), "Producto: Laptop, Precio: 1000.0, Cantidad: 5")

if __name__ == '__main__':
    unittest.main()
