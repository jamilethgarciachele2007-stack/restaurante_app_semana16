import uuid
from modelos.venta import Venta
from modelos.producto import Producto

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.archivo_usuarios = "usuarios.json"
        self.archivo_productos = "productos.json"
        self.archivo_ventas = "ventas.json"
        
        self.usuarios = []
        self.productos = []
        self.ventas = []
        self.cargar_datos()

    def cargar_datos(self):
        datos_usr = self.archivo_servicio.cargar(self.archivo_usuarios) or []
        self.usuarios = datos_usr
        
        datos_prod = self.archivo_servicio.cargar(self.archivo_productos) or []
        self.productos = [Producto.from_dict(p) for p in datos_prod]

        datos_ven = self.archivo_servicio.cargar(self.archivo_ventas) or []
        self.ventas = [Venta.from_dict(v) for v in datos_ven]

    def validar_acceso(self, usuario, contrasena):
        for u in self.usuarios:
            if u.get("usuario") == usuario and u.get("contrasena") == contrasena:
                return u
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def cantidad_ventas(self):
        return len(self.ventas)

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def listar_ventas(self):
        return self.ventas

    def registrar_venta(self, usuario_id, producto_id):
        if not usuario_id or not producto_id:
            raise ValueError("Debe seleccionar un usuario y un producto válidos.")

        nuevo_id = f"V-{str(uuid.uuid4())[:6].upper()}"
        nueva_venta = Venta(id_venta=nuevo_id, usuario_id=usuario_id, producto_id=producto_id)
        
        self.ventas.append(nueva_venta)
        
        datos_guardar = [v.to_dict() for v in self.ventas]
        self.archivo_servicio.guardar(self.archivo_ventas, datos_guardar)
        return nueva_venta