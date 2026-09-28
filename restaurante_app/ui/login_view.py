import tkinter as tk
from tkinter import ttk, messagebox
from ui.main_view import MainView

class LoginView(ttk.Frame):
    def __init__(self, parent, servicio):
        super().__init__(parent)
        self.parent = parent
        self.servicio = servicio
        self.crear_componentes()

    def crear_componentes(self):
        frame = ttk.LabelFrame(self, text=" Inicio de Sesión ")
        frame.pack(padx=20, pady=20)

        ttk.Label(frame, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.txt_user = ttk.Entry(frame)
        self.txt_user.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
        self.txt_pwd = ttk.Entry(frame, show="*")
        self.txt_pwd.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Ingresar", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        usr = self.txt_user.get().strip()
        pwd = self.txt_pwd.get().strip()

        # Buscar el usuario en el servicio
        usuarios = self.servicio.obtener_usuarios()
        usuario_encontrado = None
        for u in usuarios:
            if u.usuario == usr and u.contrasena == pwd:
                usuario_encontrado = u
                break

        if usuario_encontrado:
            # Destruir vista de login y cargar MainView enviando el usuario autenticado
            self.destroy()
            main_view = MainView(self.parent, self.servicio, usuario_encontrado)
            main_view.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")