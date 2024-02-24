def validar_numero(num_str):
    try:
        num = float(num_str)
        if num >= 1:
            return num
        else:
            print(f'{num} no es válido, ingrese un número válido mayor o igual a 1.')
            return None
    except ValueError:
        print(f'{num_str} no es un número válido.')
        return None


def encontrar_numeros_primos(valor_min, valor_max):
    numeros_primos = []
    for num in range(int(valor_min), int(valor_max) + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                numeros_primos.append(num)
    return numeros_primos


def pedir_numero():
    valor_min = validar_numero(
        input('Hola! Ingresa el número menor del rango: '))
    valor_max = validar_numero(input('Ingresa el número mayor del rango: '))

    if valor_min is not None and valor_max is not None:
        if valor_min <= valor_max:
            return encontrar_numeros_primos(valor_min, valor_max)
        else:
            print(
                "El número menor del rango debe ser menor o igual al número mayor del rango.")
            return None
    else:
        return None


if __name__ == '__main__':
    result = pedir_numero()
    if result is not None:
        if len(result) > 0:
            print(result)
        else:
            print('No hay números primos en el rango dado.')
    else:
        print('Lo siento, ha ocurrido un error.')
