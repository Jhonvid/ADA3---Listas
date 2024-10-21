from collections import deque

# Definimos la función principal
def main():
    lista = deque()

    lista.append("Palabra")
    lista.append(5)
    lista.append(17)
    lista.append("palabra 2")

    lista.pop()  # Elimina el último elemento

    print("El tamaño de la lista es:", len(lista))
    print(lista[-1])  # Accede al último elemento

# Llamamos a la función principal
if __name__ == "__main__":
    main()
