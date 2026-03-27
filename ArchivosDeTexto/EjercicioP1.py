tareas = []
print("Bienvenido a nuestro sistema de gestión de tareas, usuario.")
while(True):
    print("-------------------------------------\n¿Qué quieres hacer a continuación?")
    print("1. Agregar una tarea\n2. Ver todas las tareas\n3. Marcar una tarea como hecha.\n4. Salir\n-------------------------------------")
    opcion = input("")
    match(opcion):
        case "1":
            tareaNueva = input("¿Qué tarea desea añadir?\n")
            with open("tareas.txt","a") as file:
                    file.write(tareaNueva+"\n")

        case "2":
            with open("tareas.txt","r") as file:
                    for i, tarea in enumerate(file, 1):
                        print(f"{i}. {tarea.strip()}")

        case "3":
                with open("tareas.txt","r") as file:
                    lineas = file.readlines()

                indice = int(input("Número de tarea a marcar como hecha: "))

                if 0 <= indice-1 <= len(lineas):
                    lineas[indice-1] = lineas [indice-1].strip() +" (Hecha)\n"

                    with open("tareas.txt", "w") as file:
                        file.writelines(lineas)
                else:
                    print("Número de tarea inválido.")

        case "4":
            print("Saliendo del sistema...")
            break

        case _:
            print("La opción digitada es inválida... Intente de nuevo.")

print("Has salido del sistema.")