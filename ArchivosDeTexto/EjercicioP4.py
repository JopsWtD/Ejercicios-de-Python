from csv import DictWriter
import csv

print("Bienvenido a nuestro sistema de gestión de productos, usuario.")
while(True):
    print("-------------------------------------\n¿Qué quieres hacer a continuación?")
    print("1. Ver inventario completo\n2. Agregar producto nuevo\n3. Actualizar stock de un producto existente\n"
    "4. Mostrar productos con stock menor a 10 \n-------------------------------------")
    opcion = input("")
    match(opcion):
        case "1":
            with open("inventario.csv") as file:
                    lector = csv.DictReader(file)
                    for i, producto in enumerate(lector,1):
                        print(f"{i}. {producto}")

        case "2":
            headers = ["producto","precio","stock"]
            listaProductos = []

            print("Datos del producto a registrar: ")
            nombre = input("Nombre: ")
            precio = int(input("Precio: "))
            stock = int(input("¿Cuántas unidades hay?: "))
            productoDB = {"producto":nombre, "precio":precio, "stock":stock}
            listaProductos.append(productoDB)
            with open("inventario.csv","w", newline="") as file:
                    writer = DictWriter(file,fieldnames=headers)
                    writer.writeheader()
                    for producto in listaProductos:
                         writer.writerow(producto)


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

