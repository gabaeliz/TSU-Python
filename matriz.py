def imprimir_linea(spaces, stars):
    print(' ' * spaces, end='')
    print('* ' * stars)


def arriba(centro):
    for i in range(centro):
        imprimir_linea(centro - i, i)


def abajo(centro):
    for i in range(centro - 1, -1, -1):
        imprimir_linea(centro - i, i)


def imprimir_rombo(centro):
    arriba(centro)
    abajo(centro)


if __name__ == '__main__':
    try:
        size = int(input("Introduce el tamaño del rombo: "))
        centro = size // 2 + 1
        if size % 2 == 0:
            raise ValueError(
                "Intenta de nuevo...\n El tamaño del rombo debe ser impar")
        imprimir_rombo(centro)
    except ValueError as ve:
        print("Error:", ve)
