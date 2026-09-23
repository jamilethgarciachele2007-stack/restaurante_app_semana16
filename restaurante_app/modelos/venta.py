from datetime import datetime

class Venta:
    def __init__(self, id_venta, usuario_id, producto_id, fecha=None):
        self.id_venta = id_venta
        self.usuario_id = usuario_id
        self.producto_id = producto_id
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            id_venta=data["id_venta"],
            usuario_id=data["usuario_id"],
            producto_id=data["producto_id"],
            fecha=data["fecha"]
        )

   