import json
import os

class ArchivoServicio:
    def __init__(self, carpeta_datos="datos"):
        self.carpeta_datos = carpeta_datos
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)

    def _obtener_ruta(self, nombre_archivo):
        if nombre_archivo.startswith(self.carpeta_datos):
            return nombre_archivo
        return os.path.join(self.carpeta_datos, nombre_archivo)

    def cargar(self, nombre_archivo):
        ruta = self._obtener_ruta(nombre_archivo)
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def cargar_json(self, nombre_archivo):
        return self.cargar(nombre_archivo)

    def guardar(self, nombre_archivo, datos):
        ruta = self._obtener_ruta(nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def guardar_json(self, nombre_archivo, datos):
        self.guardar(nombre_archivo, datos)