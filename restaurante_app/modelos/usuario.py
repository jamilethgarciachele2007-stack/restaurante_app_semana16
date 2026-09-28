class Usuario:
    def __init__(self, id_usuario, usuario, contrasena, nombre, rol="Cliente"):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.rol = rol  # 'Administrador', 'Empleado' o 'Cliente'

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            id_usuario=data.get("id_usuario", ""),
            usuario=data.get("usuario", ""),
            contrasena=data.get("contrasena", ""),
            nombre=data.get("nombre", ""),
            rol=data.get("rol", "Cliente")
        )