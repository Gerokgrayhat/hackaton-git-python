import os

# Nombre del archivo donde se guardarán las tareas
TAREAS_FILE = 'tareas.txt'

def agregar_tarea(nombre, descripcion):
    with open(TAREAS_FILE, 'a') as f:
        f.write(f"{nombre};{descripcion}\n")
    print("Tarea agregada exitosamente.")

def listar_tareas():
    if not os.path.exists(TAREAS_FILE):
        print("No hay tareas guardadas.")
        return
    
    with open(TAREAS_FILE, 'r') as f:
        tareas = f.readlines()
    
    if not tareas:
        print("No hay tareas guardadas.")
        return
    
    print("Tareas guardadas:")
    for tarea in tareas:
        nombre, descripcion = tarea.strip().split(';')
        print(f"- {nombre}: {descripcion}")

def eliminar_tarea(nombre):
    if not os.path.exists(TAREAS_FILE):
        print("No hay tareas guardadas.")
        return
    
    with open(TAREAS_FILE, 'r') as f:
        tareas = f.readlines()
    
    with open(TAREAS_FILE, 'w') as f:
        tarea_encontrada = False
        for tarea in tareas:
            if tarea.strip().split(';')[0] != nombre:
                f.write(tarea)
            else:
                tarea_encontrada = True
    
    if tarea_encontrada:
        print("Tarea eliminada exitosamente.")
    else:
        print("Tarea no encontrada.")

def main():
    while True:
        print("\nAdministrador de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(nombre, descripcion)
        elif opcion == '2':
            listar_tareas()
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la tarea a eliminar: ")
            eliminar_tarea(nombre)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
