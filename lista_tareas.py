class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
    
    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} [{estado}]"


class GestionTareas:
    def __init__(self, archivo="tareas.txt"):
        self.archivo = archivo

    def _leer_archivo(self):
        """Leer el archivo y devolver una lista de tareas."""
        try:
            with open(self.archivo, "r") as f:
                tareas = f.readlines()
            return [linea.strip() for linea in tareas]
        except FileNotFoundError:
            # Si el archivo no existe, devolvemos una lista vacía
            return []

    def _guardar_tareas(self, tareas):
        """Guardar las tareas en el archivo."""
        try:
            with open(self.archivo, "w") as f:
                for tarea in tareas:
                    f.write(tarea + "\n")
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")

    def agregar_tarea(self, descripcion):
        """Agregar una nueva tarea al archivo."""
        tarea = Tarea(descripcion)
        tareas = self._leer_archivo()
        tareas.append(str(tarea))
        self._guardar_tareas(tareas)
        print("Tarea agregada con éxito.")

    def mostrar_tareas(self):
        """Mostrar todas las tareas guardadas en el archivo."""
        tareas = self._leer_archivo()
        if tareas:
            print("\nLista de tareas:")
            for tarea in tareas:
                print(tarea)
        else:
            print("No hay tareas guardadas.")

    def completar_tarea(self, descripcion):
       tareas = self._leer_archivo()
       tareas_actualizadas = [tarea for tarea in tareas if descripcion not in tarea]
       self._guardar_tareas(tareas_actualizadas)
       print(f"Tarea '{descripcion}' marcada como completada y eliminada.")


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Salir")

def ejecutar():
    gestor = GestionTareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            descripcion = input("Ingrese la descripción de la tarea a completar: ")
            gestor.completar_tarea(descripcion)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    ejecutar()