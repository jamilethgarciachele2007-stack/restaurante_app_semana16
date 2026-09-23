class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            id_producto=data["id_producto"],
            nombre=data["nombre"],
            precio=data["precio"],
            categoria=data["categoria"]
        )