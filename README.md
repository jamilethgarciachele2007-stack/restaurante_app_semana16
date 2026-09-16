# Fundamentos de manejo de eventos con Tkinter

## Tema

Semana 15: conceptos fundamentales de manejo de eventos en una aplicacion de biblioteca con Tkinter.

## Objetivo

Evolucionar el proyecto de la Semana 14 sin reconstruirlo desde cero. La aplicacion conserva el login, la arquitectura por capas, la persistencia JSON, la consulta de usuarios y el CRUD de libros. En esta semana se agrega una operacion sencilla de venta para observar el flujo entre una accion del usuario, un boton con `command=`, un callback, el servicio, la persistencia y la respuesta visual.

## Continuidad desde Semana 14

La interfaz mantiene los mismos colores, estilos, iconos, menu lateral, barra de estado y organizacion general. La nueva seccion `Ventas` se integra como una capacidad adicional de la misma aplicacion.

## Nueva funcionalidad

La venta relaciona:

```text
Usuario + Libro + Fecha -> Venta
```

La seccion `Ventas` permite:

- seleccionar un usuario registrado con `ttk.Combobox`;
- seleccionar un libro registrado con `ttk.Combobox`;
- pulsar el boton `Registrar venta`;
- ejecutar el callback `registrar_venta()` mediante `command=`;
- guardar la venta en `datos/ventas.json`;
- mostrar las ventas registradas en un `ttk.Treeview`.

Flujo educativo:

```text
Accion del usuario -> Boton -> command= -> callback -> servicio -> JSON -> Treeview actualizado
```

## Estructura del proyecto

```text
biblioteca_app/
├── assets/
│   ├── icons/
│   │   ├── home.png
│   │   ├── users.png
│   │   ├── books.png
│   │   ├── sales.png        # opcional para la seccion Ventas
│   │   ├── logout.png
│   │   ├── add.png
│   │   ├── edit.png
│   │   ├── delete.png
│   │   ├── search.png
│   │   └── clean.png
│   └── logo/
│       ├── logo.png
│       └── icono.png
├── datos/
│   ├── libros.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── usuario.py
│   ├── libro.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── biblioteca_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
└── main.py
```

## Capas

`modelos/`: define las clases `Usuario`, `Libro` y `Venta`, con validaciones basicas para evitar campos vacios.

`servicios/`: contiene la logica de consulta, registro, actualizacion, eliminacion y persistencia. `BibliotecaServicio` tambien registra ventas.

`datos/`: guarda la informacion persistente en archivos JSON.

`ui/`: contiene las vistas creadas con Tkinter.

`assets/icons/`: contiene iconos PNG usados por los botones. Si falta un icono, la aplicacion sigue funcionando con texto.

## Icono opcional de Ventas

Para el nuevo boton del menu lateral se espera opcionalmente este archivo:

```text
biblioteca_app/assets/icons/sales.png
```

No es obligatorio incluirlo. La funcion `cargar_icono()` devuelve `None` si no lo encuentra y el boton se muestra solo con texto.

## Pantallas principales

`LoginView`: pantalla de inicio de sesion.

`Inicio`: panel de resumen con usuarios, libros y ventas.

`Usuarios`: pantalla de consulta de usuarios registrados.

`Libros`: pantalla de gestion con formulario, botones y tabla para el CRUD basico.

`Ventas`: pantalla nueva para seleccionar un usuario, seleccionar un libro y registrar una venta simple.

## Componentes Tkinter utilizados

`Label`: textos y titulos.

`Entry`: campos de entrada para login y formulario de libros.

`ttk.Combobox`: selectores de usuario y libro en la vista de ventas.

`ttk.Button`: botones de navegacion y acciones con `command=`.

`ttk.Treeview`: tablas de usuarios, libros y ventas.

`ttk.Scrollbar`: barra de desplazamiento para las tablas.

`messagebox`: mensajes simples de confirmacion o error.

## Persistencia

Los usuarios, libros y ventas se cargan desde JSON al iniciar la aplicacion.

```text
biblioteca_app/datos/usuarios.json
biblioteca_app/datos/libros.json
biblioteca_app/datos/ventas.json
```

Al registrar una venta, el servicio agrega el objeto a la coleccion en memoria, convierte las ventas a datos serializables y escribe `ventas.json`.

## Que NO se trabaja todavia

En Semana 15 no se utilizan eventos avanzados. No se implementa:

- `bind()`;
- doble clic;
- eventos de teclado;
- eventos de mouse;
- `<<TreeviewSelect>>`;
- carga automatica desde tablas;
- seleccion reactiva de filas.

Estos conceptos quedan para la siguiente semana de manejo de eventos.

## Como ejecutar

Desde la carpeta del proyecto:

```powershell
cd "C:\Users\Usuario\OneDrive\Documentos\Clase Semana 15 POO\biblioteca_app"
py main.py
```

Si `python` esta disponible:

```powershell
python main.py
```

## Credenciales de demostracion

Usuario: `admin`

Contrasena: `1234`

Tambien puede usarse:

Usuario: `docente`

Contrasena: `abcd`

## Nota educativa

El proyecto mantiene una implementacion sencilla para que el estudiante pueda seguir el crecimiento progresivo de la aplicacion:

```text
Semana 14: componentes y contenedores
Semana 15: accion -> command= -> callback -> servicio -> persistencia -> respuesta visual
```

La venta no representa todavia un sistema comercial completo. Solo muestra una relacion clara entre un usuario y un libro para estudiar los fundamentos del manejo de eventos mediante botones.
