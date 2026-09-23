import os
import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):
    def __init__(self, parent, restaurante_servicio):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        
        self.pack(fill="both", expand=True, padx=15, pady=15)
        self.crear_widgets()

    def crear_widgets(self):
        # 1. Encabezado con Logo y Título
        frame_header = ttk.Frame(self)
        frame_header.pack(fill="x", pady=(0, 10))

        # Cargar y escalar el Logo desde assets/logo/hamburguesa.png
        ruta_logo = os.path.join("assets", "logo", "hamburguesa.png")
        if os.path.exists(ruta_logo):
            try:
                img_original = tk.PhotoImage(file=ruta_logo)
                # Reducimos proporcionalmente la imagen para ajustarla a tamaño icono de encabezado
                self.img_logo = img_original.subsample(12, 12)
                lbl_logo = ttk.Label(frame_header, image=self.img_logo)
                lbl_logo.pack(side="left", padx=(0, 10))
            except Exception as e:
                print(f"No se pudo cargar la imagen del logo: {e}")

        lbl_titulo = ttk.Label(
            frame_header, 
            text="Gestión de Ventas - Restaurante", 
            font=("Helvetica", 16, "bold")
        )
        lbl_titulo.pack(side="left")

        # 2. Formulario de Registro de Venta
        frame_form = ttk.LabelFrame(self, text="Registrar Nueva Venta", padding=10)
        frame_form.pack(fill="x", pady=(0, 10))

        # Combobox Usuario
        ttk.Label(frame_form, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.cbo_usuario = ttk.Combobox(frame_form, state="readonly", width=20)
        self.cbo_usuario.grid(row=0, column=1, padx=5, pady=5)

        # Combobox Producto
        ttk.Label(frame_form, text="Producto:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.cbo_producto = ttk.Combobox(frame_form, state="readonly", width=20)
        self.cbo_producto.grid(row=0, column=3, padx=5, pady=5)

        # Botón de registro
        btn_registrar = ttk.Button(
            frame_form, 
            text="Registrar venta", 
            command=self.registrar_venta_event
        )
        btn_registrar.grid(row=0, column=4, padx=10, pady=5)

        # 3. Historial / Tabla de Ventas (Treeview)
        frame_tabla = ttk.LabelFrame(self, text="Historial de Ventas", padding=10)
        frame_tabla.pack(fill="both", expand=True)

        columnas = ("id_venta", "usuario", "producto", "fecha")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("id_venta", text="ID Venta")
        self.tabla.heading("usuario", text="Usuario")
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("fecha", text="Fecha y Hora")

        self.tabla.column("id_venta", width=100, anchor="center")
        self.tabla.column("usuario", width=150, anchor="center")
        self.tabla.column("producto", width=200, anchor="w")
        self.tabla.column("fecha", width=180, anchor="center")

        self.tabla.pack(fill="both", expand=True)

        # Cargar opciones en combos y datos en la tabla
        self.actualizar_combos()
        self.actualizar_tabla_ventas()

    def actualizar_combos(self):
        usuarios = self.restaurante_servicio.listar_usuarios()
        productos = self.restaurante_servicio.listar_productos()

        self.dict_usuarios = {u.get("nombre", u.get("usuario")): u.get("usuario") for u in usuarios}
        self.dict_productos = {p.nombre: p.id_producto for p in productos}

        self.cbo_usuario["values"] = list(self.dict_usuarios.keys())
        self.cbo_producto["values"] = list(self.dict_productos.keys())

        if self.cbo_usuario["values"]:
            self.cbo_usuario.current(0)
        if self.cbo_producto["values"]:
            self.cbo_producto.current(0)

    def actualizar_tabla_ventas(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        ventas = self.restaurante_servicio.listar_ventas()
        for v in ventas:
            self.tabla.insert("", "end", values=(
                v.id_venta,
                v.usuario_id,
                v.producto_id,
                v.fecha.strftime("%Y-%m-%d %H:%M:%S") if hasattr(v.fecha, 'strftime') else str(v.fecha)
            ))

    def registrar_venta_event(self):
        nombre_usr = self.cbo_usuario.get()
        nombre_prod = self.cbo_producto.get()

        if not nombre_usr or not nombre_prod:
            messagebox.showwarning("Atención", "Debe seleccionar un usuario y un producto.")
            return

        usr_id = self.dict_usuarios.get(nombre_usr, nombre_usr)
        prod_id = self.dict_productos.get(nombre_prod, nombre_prod)

        try:
            self.restaurante_servicio.registrar_venta(usr_id, prod_id)
            self.actualizar_tabla_ventas()
            messagebox.showinfo("Éxito", f"Venta de '{nombre_prod}' registrada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar la venta: {e}")