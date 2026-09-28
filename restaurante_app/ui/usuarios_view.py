import tkinter as tk
from tkinter import ttk, messagebox

class VistaUsuarios(ttk.Frame):
    def __init__(self, parent, servicio, usuario_actual):
        super().__init__(parent)
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.usuario_seleccionado_id = None

        self.crear_interfaz()
        self.asociar_eventos()
        self.cargar_usuarios_tabla()

    def crear_interfaz(self):
        # 1. Formulario de datos
        form_frame = ttk.LabelFrame(self, text=" Datos del Usuario ")
        form_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.txt_nombre = ttk.Entry(form_frame)
        self.txt_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Usuario:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.txt_usuario = ttk.Entry(form_frame)
        self.txt_usuario.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.txt_password = ttk.Entry(form_frame, show="*")
        self.txt_password.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Rol:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.combo_rol = ttk.Combobox(form_frame, values=["Cliente", "Empleado", "Administrador"], state="readonly")
        self.combo_rol.set("Cliente")
        self.combo_rol.grid(row=1, column=3, padx=5, pady=5)

        # 2. Botones de acción
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(btn_frame, text="Registrar", command=self.guardar_usuario).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Actualizar", command=self.actualizar_usuario).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_usuario).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Limpiar (Esc)", command=self.limpiar_formulario).pack(side="left", padx=5)

        # 3. Tabla Treeview
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columnas = ("ID", "Nombre", "Usuario", "Rol")
        self.tree = ttk.Treeview(tree_frame, columns=columnas, show="headings", selectmode="browse")
        
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True)

    def asociar_eventos(self):
        # Asignación de eventos Tkinter requeridos
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.combo_rol.bind("<<ComboboxSelected>>", self.on_combobox_change)
        
        self.txt_nombre.bind("<Return>", lambda e: self.guardar_usuario())
        self.txt_usuario.bind("<Return>", lambda e: self.guardar_usuario())
        self.txt_password.bind("<Return>", lambda e: self.guardar_usuario())
        
        self.bind_all("<Escape>", lambda e: self.limpiar_formulario())

    # --- CALLBACKS DE EVENTOS ---

    def on_tree_select(self, event):
        seleccion = self.tree.selection()
        if not seleccion:
            return

        item = self.tree.item(seleccion[0])
        valores = item['values']
        if not valores:
            return

        usuario_id = str(valores[0])
        usuario = self.servicio.obtener_usuario_por_id(usuario_id)

        if usuario:
            self.usuario_seleccionado_id = usuario.id_usuario
            
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, usuario.nombre)

            self.txt_usuario.delete(0, tk.END)
            self.txt_usuario.insert(0, usuario.usuario)

            self.txt_password.delete(0, tk.END)
            self.txt_password.insert(0, usuario.contrasena)

            self.combo_rol.set(usuario.rol)

    def on_combobox_change(self, event):
        print(f"Rol seleccionado en Combobox: {self.combo_rol.get()}")

    def cargar_usuarios_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree.insert("", "end", values=(u.id_usuario, u.nombre, u.usuario, u.rol))

    def guardar_usuario(self):
        if self.usuario_seleccionado_id:
            messagebox.showinfo("Aviso", "Tiene un usuario seleccionado. Presione 'Limpiar (Esc)' antes de registrar uno nuevo.")
            return

        nombre = self.txt_nombre.get().strip()
        user = self.txt_usuario.get().strip()
        pwd = self.txt_password.get().strip()
        rol = self.combo_rol.get()

        if not nombre or not user or not pwd:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        self.servicio.registrar_usuario(user, pwd, nombre, rol)
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        self.limpiar_formulario()
        self.cargar_usuarios_tabla()

    def actualizar_usuario(self):
        if not self.usuario_seleccionado_id:
            messagebox.showwarning("Atención", "Seleccione un usuario de la tabla para actualizar.")
            return

        nombre = self.txt_nombre.get().strip()
        user = self.txt_usuario.get().strip()
        pwd = self.txt_password.get().strip()
        rol = self.combo_rol.get()

        if not nombre or not user:
            messagebox.showwarning("Atención", "El nombre y usuario son obligatorios.")
            return

        exito = self.servicio.actualizar_usuario(self.usuario_seleccionado_id, user, pwd, nombre, rol)
        if exito:
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self.limpiar_formulario()
            self.cargar_usuarios_tabla()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el usuario.")

    def eliminar_usuario(self):
        if not self.usuario_seleccionado_id:
            messagebox.showwarning("Atención", "Seleccione un usuario de la tabla para eliminar.")
            return

        if str(self.usuario_seleccionado_id) == str(self.usuario_actual.id_usuario):
            messagebox.showerror("Error", "No puede eliminar la cuenta con la que ha iniciado sesión.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el usuario seleccionado?"):
            self.servicio.eliminar_usuario(self.usuario_seleccionado_id)
            self.limpiar_formulario()
            self.cargar_usuarios_tabla()

    def limpiar_formulario(self):
        self.usuario_seleccionado_id = None
        self.txt_nombre.delete(0, tk.END)
        self.txt_usuario.delete(0, tk.END)
        self.txt_password.delete(0, tk.END)
        self.combo_rol.set("Cliente")
        
        for item in self.tree.selection():
            self.tree.selection_remove(item)