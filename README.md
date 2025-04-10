# gestion_de_tareas
Este programa permite gestionar tareas pendientes a través de un menú interactivo por consola. Se pueden agregar, mostrar y completar tareas, las cuales se almacenan en un archivo de texto (tareas.txt) para conservar la información entre ejecuciones del programa.

🧱 Estructura del Código
El programa está organizado en tres partes principales:

Clase Tarea

Clase GestionTareas

Funciones del menú y ejecución del programa

1. 📦 Clase Tarea
Representa una tarea individual.

Atributos:
descripcion: Texto que describe la tarea.

completada: Estado de la tarea (inicialmente False).

Métodos:
__init__(self, descripcion): Constructor que inicializa la descripción y el estado.

__str__(self): Método que permite imprimir la tarea como una cadena legible, incluyendo su estado (Pendiente o Completada).

2. 🗃️ Clase GestionTareas
Administra la lista de tareas y las operaciones sobre el archivo tareas.txt.

Atributo:
archivo: Nombre del archivo donde se guardan las tareas (por defecto "tareas.txt").

Métodos:
_leer_archivo(self):
Lee el archivo línea por línea y retorna una lista de tareas en forma de texto. Si el archivo no existe, devuelve una lista vacía.

_guardar_tareas(self, tareas):
Guarda una lista de tareas en el archivo, sobrescribiendo el contenido anterior.

agregar_tarea(self, descripcion):
Crea una nueva tarea, la agrega a la lista de tareas y actualiza el archivo.

mostrar_tareas(self):
Muestra en pantalla todas las tareas almacenadas.

completar_tarea(self, descripcion):
Este método tiene un pequeño error lógico, ya que no elimina la tarea completada, solo la vuelve a guardar igual. La intención parece ser eliminarla, pero no se implementa correctamente.

3. 🎛️ Menú Interactivo y Ejecución
Funciones:
mostrar_menu(): Muestra las opciones disponibles al usuario.

ejecutar(): Lógica principal del programa. Crea una instancia de GestionTareas y ejecuta un bucle infinito para mostrar el menú y recibir las acciones del usuario.

📂 Uso del Programa
Al ejecutar el archivo, se muestra un menú con las siguientes opciones:

1: Agregar una tarea.

2: Ver todas las tareas guardadas.

3: Completar (eliminar) una tarea.

4: Salir del programa.
