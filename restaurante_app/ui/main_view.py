import tkinter as tk
from tkinter import ttk, messagebox
from ui.usuarios_view import VistaUsuarios

class MainView(ttk.Frame):
    def __init__(self, parent, servicio, usuario_actual):
        super().__init__(parent)
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        # Encabezado con información del usuario autenticado y su rol
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=10, pady=5)
        
        lbl_welcome = ttk.Label(
            header_frame, 
            text=f"Bienvenido/a: {self.usuario_actual.nombre} ({self.usuario_actual.rol})", 
            font=("Arial", 11, "bold")
        )
        lbl_welcome.pack(side="left")

        # Control de Pestañas (Notebook)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        # 1. Pestaña de Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Productos")
        self.cargar_seccion_productos()

        # 2. Pestaña de Ventas
        self.tab_ventas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_ventas, text="Ventas")
        self.cargar_seccion_ventas()

        # 3. Pestaña de Gestión de Usuarios (SOLO PARA ADMINISTRADOR)
        # Limpia espacios y convierte primera letra a mayúscula para validar sin errores
        rol_normalizado = str(self.usuario_actual.rol).strip().capitalize()
        if rol_normalizado == "Administrador":
            self.tab_usuarios = ttk.Frame(self.notebook)
            self.notebook.add(self.tab_usuarios, text="Gestión de Usuarios")

            # Instanciación de la vista de usuarios
            self.vista_usuarios = VistaUsuarios(self.tab_usuarios, self.servicio, self.usuario_actual)
            self.vista_usuarios.pack(fill="both", expand=True)

    def cargar_seccion_productos(self):
        """Espacio reservado para el módulo de Productos"""
        lbl = ttk.Label(self.tab_productos, text="Módulo de Gestión de Productos", font=("Arial", 12))
        lbl.pack(padx=20, pady=20)

    def cargar_seccion_ventas(self):
        """Espacio reservado para el módulo de Ventas"""
        lbl = ttk.Label(self.tab_ventas, text="Módulo de Gestión de Ventas", font=("Arial", 12))
        lbl.pack(padx=20, pady=20)