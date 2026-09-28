import uuid
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio

    def obtener_usuarios(self):
        datos = self.archivo_servicio.cargar_json("datos/usuarios.json")
        if not datos:
            return []
        return [Usuario.from_dict(d) for d in datos]

    def obtener_usuario_por_id(self, id_usuario):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if str(u.id_usuario).strip() == str(id_usuario).strip():
                return u
        return None

    def registrar_usuario(self, usuario, contrasena, nombre, rol):
        usuarios = self.obtener_usuarios()
        nuevo_id = f"U{len(usuarios) + 1}"
        nuevo_usuario = Usuario(nuevo_id, usuario, contrasena, nombre, rol)
        usuarios.append(nuevo_usuario)
        
        datos_dict = [u.to_dict() for u in usuarios]
        return self.archivo_servicio.guardar_json("datos/usuarios.json", datos_dict)

    def actualizar_usuario(self, id_usuario, usuario, contrasena, nombre, rol):
        usuarios = self.obtener_usuarios()
        encontrado = False
        for u in usuarios:
            if str(u.id_usuario).strip() == str(id_usuario).strip():
                u.usuario = usuario
                u.nombre = nombre
                u.rol = rol
                # Si la contraseña no se modificó o son asteriscos, mantener la existente
                if contrasena and contrasena != "****":
                    u.contrasena = contrasena
                encontrado = True
                break
                
        if encontrado:
            datos_dict = [u.to_dict() for u in usuarios]
            return self.archivo_servicio.guardar_json("datos/usuarios.json", datos_dict)
        return False

    def eliminar_usuario(self, id_usuario):
        usuarios = self.obtener_usuarios()
        usuarios_filtrados = [u for u in usuarios if str(u.id_usuario).strip() != str(id_usuario).strip()]
        datos_dict = [u.to_dict() for u in usuarios_filtrados]
        return self.archivo_servicio.guardar_json("datos/usuarios.json", datos_dict)