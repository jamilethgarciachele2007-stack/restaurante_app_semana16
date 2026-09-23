import os
import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.main_view import MainView

def main():
    root = tk.Tk()
    root.title("Sistema de Gestión - Restaurante App")
    root.geometry("850x600")

    # Establecer el icono de la ventana usando assets/logo/hamburguesa.png
    ruta_icono = os.path.join("assets", "logo", "hamburguesa.png")
    if os.path.exists(ruta_icono):
        try:
            icono = tk.PhotoImage(file=ruta_icono)
            root.iconphoto(True, icono)
        except Exception as e:
            print(f"No se pudo establecer el icono de la ventana: {e}")

    archivo_servicio = ArchivoServicio("datos")
    restaurante_servicio = RestauranteServicio(archivo_servicio)

    app = MainView(root, restaurante_servicio)
    app.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()