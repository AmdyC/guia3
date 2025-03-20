def add(task_list):
    description = input("Ingrese la descripción de la tarea: ")
    deadline = input("Ingrese la fecha límite (DD-MM-YYYY): ")
    priority = input("Ingrese la prioridad (Alta/Media/Baja): ")
    task_list.append({"Descripción": description, "Fecha límite": deadline, "Prioridad": priority})
    print("\nTarea agregada con éxito!\n")

def show(task_list):
    if not task_list:
        print("\nNo hay tareas registradas.\n")
    else:
        print("\nLista de Tareas:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
        print()

def main():
    tasks = []
    while True:
        option = input("1. Agregar tarea\n2. Mostrar tareas\n3. Salir\nSeleccione una opción: ")
        if option == "1":
            add(tasks)
        elif option == "2":
            show(tasks)
        elif option == "3":
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
