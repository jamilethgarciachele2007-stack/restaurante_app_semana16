# Restaurante App - Semana 16

## Descripción
Evolución del sistema de gestión de restaurante implementando el manejo de eventos en Tkinter para la gestión de usuarios y roles.

## Arquitectura del Proyecto
- `datos/`: Archivos JSON de persistencia (`usuarios.json`).
- `modelos/`: Clases de datos (`usuario.py`).
- `servicios/`: Lógica de negocio y manejo de archivos (`restaurante_servicio.py`).
- `ui/`: Vistas de la aplicación (`login_view.py`, `main_view.py`, `usuarios_view.py`).
- `main.py`: Punto de entrada de la aplicación.

## Manejo de Eventos Implementados
- `<<TreeviewSelect>>`: Carga los datos del usuario seleccionado en la tabla hacia el formulario.
- `<Return>`: Atajo con la tecla Enter para ejecutar acciones en las entradas de texto.
- `<Escape>`: Atajo con la tecla Esc para limpiar el formulario y deseleccionar elementos.
- `<<ComboboxSelected>>`: Captura los eventos al cambiar la opción del rol.

## Ejecución
1. Asegurar la versión de Python 3.x.
2. Ejecutar el comando:
   ```bash
   python main.py