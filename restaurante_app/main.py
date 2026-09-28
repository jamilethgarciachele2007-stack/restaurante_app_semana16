import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView

def main():
    root = tk.Tk()
    root.title("Restaurante App")
    root.geometry("900x600")

    # Intentar cargar ícono si existe
    try:
        root.iconphoto(False, tk.PhotoImage(file="assets/logo/icono.png"))
    except Exception:
        pass

    # Instanciar servicios
    archivo_servicio = ArchivoServicio()
    servicio = RestauranteServicio(archivo_servicio)

    # Cargar primero la vista de LoginView
    app = LoginView(root, servicio)
    app.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()