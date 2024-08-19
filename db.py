# db.py
import json

def guardar_producto(producto):
    with open('productos.json', 'a') as f:
        json.dump(producto.__dict__, f)
        f.write('\n')

def cargar_productos():
    productos = []
    try:
        with open('productos.json', 'r') as f:
            for line in f:
                datos = json.loads(line.strip())
                productos.append(datos)
    except FileNotFoundError:
        pass
    return productos
