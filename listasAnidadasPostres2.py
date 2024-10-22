# Lista de postres con ingredientes (listas anidadas)
postres = [
    ["cheesecake", ["queso crema", "azúcar", "huevos", "galletas", "queso crema"]],
    ["flan", ["leche", "huevos", "azúcar", "vainilla", "vainilla"]],
    ["tiramisu", ["queso mascarpone", "café", "huevos", "azúcar", "bizcochos", "café"]]
]

# Función para mostrar los postres disponibles
def mostrar_postres():
    if postres:
        print("Postres disponibles:")
        for postre in postres:
            print(f"- {postre[0]}")
    else:
        print("No hay postres disponibles.")

# Función para buscar un postre en la lista
def buscar_postre(postre):
    for i in range(len(postres)):
        if postres[i][0] == postre:
            return i
    return -1

# a) Función para imprimir la lista de ingredientes de un postre
def imprimir_ingredientes(postre):
    indice = buscar_postre(postre)
    if indice != -1:
        if postres[indice][1]:
            print(f"Los ingredientes de {postre} son: {', '.join(postres[indice][1])}")
        else:
            print(f"El postre '{postre}' no tiene ingredientes.")
    else:
        print(f"El postre '{postre}' no existe.")

# b) Función para insertar nuevos ingredientes a un postre, con opción de especificar la posición
def agregar_ingredientes(postre, nuevos_ingredientes, posicion=None):
    indice = buscar_postre(postre)
    if indice != -1:
        if posicion is not None and posicion < len(postres[indice][1]):
            # Inserta en una posición específica
            for i, ingrediente in enumerate(nuevos_ingredientes):
                postres[indice][1].insert(posicion + i, ingrediente)
            print(f"Se agregaron los ingredientes: {', '.join(nuevos_ingredientes)} en la posición {posicion} de {postre}.")
        else:
            # Agrega al final si no se especifica la posición o si es mayor que el tamaño
            postres[indice][1].extend(nuevos_ingredientes)
            print(f"Se agregaron los ingredientes: {', '.join(nuevos_ingredientes)} al final de {postre}.")
    else:
        print(f"El postre '{postre}' no existe.")

# c) Función para eliminar un ingrediente de un postre
def eliminar_ingrediente(postre, ingrediente):
    indice = buscar_postre(postre)
    if indice != -1:
        if ingrediente in postres[indice][1]:
            postres[indice][1].remove(ingrediente)
            print(f"Se eliminó el ingrediente '{ingrediente}' de {postre}.")
        else:
            print(f"El ingrediente '{ingrediente}' no está en {postre}.")
    else:
        print(f"El postre '{postre}' no existe.")

# Función para eliminar todos los ingredientes de un postre sin eliminar el postre
def eliminar_todos_ingredientes(postre):
    indice = buscar_postre(postre)
    if indice != -1:
        postres[indice][1].clear()  # Vaciar la lista de ingredientes
        print(f"Se han eliminado todos los ingredientes de {postre}.")
    else:
        print(f"El postre '{postre}' no existe.")

# d) Función para dar de alta un nuevo postre con ingredientes
def dar_alta_postre(postre, ingredientes):
    if buscar_postre(postre) == -1:
        postres.append([postre, ingredientes])
        print(f"El postre '{postre}' fue agregado con los ingredientes: {', '.join(ingredientes)}.")
    else:
        print(f"El postre '{postre}' ya existe.")

# e) Función para dar de baja (eliminar) un postre
def dar_baja_postre(postre):
    indice = buscar_postre(postre)
    if indice != -1:
        postres.pop(indice)
        print(f"El postre '{postre}' ha sido eliminado.")
    else:
        print(f"El postre '{postre}' no existe.")

# Nueva función para eliminar ingredientes repetidos de cada postre
def eliminar_ingredientes_repetidos():
    for postre in postres:
        # Convertimos la lista de ingredientes a un conjunto y de vuelta a una lista para eliminar duplicados
        ingredientes_unicos = list(set(postre[1]))
        postre[1] = ingredientes_unicos  # Asignamos la nueva lista sin repetidos
    print("Se han eliminado los ingredientes repetidos de todos los postres.")

# Función para imprimir los postres y sus ingredientes
def imprimir_postres():
    for postre in postres:
        print(f"{postre[0].capitalize()}: {', '.join(postre[1])}")

# Menú principal para interactuar con el programa
def menu():
    while True:
        print("\n--- MENÚ DE POSTRES ---")
        print("1. Imprimir ingredientes de un postre")
        print("2. Agregar ingredientes a un postre")
        print("3. Eliminar un ingrediente de un postre")
        print("4. Eliminar todos los ingredientes de un postre")
        print("5. Dar de alta un nuevo postre")
        print("6. Dar de baja un postre")
        print("7. Eliminar ingredientes repetidos de todos los postres")
        print("8. Salir")

        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            mostrar_postres()
            postre = input("Ingresa el nombre del postre: ").lower()
            imprimir_ingredientes(postre)
        elif opcion == "2":
            mostrar_postres()
            postre = input("Ingresa el nombre del postre: ").lower()
            ingredientes = input("Ingresa los ingredientes separados por comas: ").lower().split(", ")
            pos = input("¿En qué posición deseas agregar los ingredientes? (Deja en blanco para agregar al final): ")
            if pos.isdigit():
                agregar_ingredientes(postre, ingredientes, int(pos))
            else:
                agregar_ingredientes(postre, ingredientes)
        elif opcion == "3":
            mostrar_postres()
            postre = input("Ingresa el nombre del postre: ").lower()
            ingrediente = input("Ingresa el ingrediente que deseas eliminar: ").lower()
            eliminar_ingrediente(postre, ingrediente)
        elif opcion == "4":
            mostrar_postres()
            postre = input("Ingresa el nombre del postre: ").lower()
            eliminar_todos_ingredientes(postre)
        elif opcion == "5":
            postre = input("Ingresa el nombre del nuevo postre: ").lower()
            ingredientes = input("Ingresa los ingredientes separados por comas: ").lower().split(", ")
            dar_alta_postre(postre, ingredientes)
        elif opcion == "6":
            mostrar_postres()
            postre = input("Ingresa el nombre del postre a eliminar: ").lower()
            dar_baja_postre(postre)
        elif opcion == "7":
            eliminar_ingredientes_repetidos()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()
