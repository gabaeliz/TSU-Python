import re

variables = {}

def asignar_variable(expresion):
    variable, valor = expresion.split('=')
    variables[variable.strip()] = float(valor.strip())

def realizar_operaciones(expresion):
    try:
        operaciones = {'+': lambda x, y: x + y,
                       '-': lambda x, y: x - y,
                       '*': lambda x, y: x * y,
                       '/': lambda x, y: x / y,
                       '^': lambda x, y: x ** y}

        print("Expresión recibida:", expresion)  # Agregamos esta línea para depurar

        numeros = re.findall(r'\d+\.?\d*', expresion)
        operadores = re.findall(r'[\+\-\*\/\^]', expresion)

        print("Números encontrados:", numeros)  # Agregamos esta línea para depurar
        print("Operadores encontrados:", operadores)  # Agregamos esta línea para depurar

        if not numeros or not operadores:
            raise ValueError("Expresión matemática inválida.")

        resultado = float(numeros[0])
        for i in range(1, len(numeros)):
            operador = operadores[i - 1]
            numero = float(numeros[i])
            resultado = operaciones[operador](resultado, numero)

        return resultado

    except ZeroDivisionError:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    except Exception as e:
        raise ValueError(str(e))
    
def evaluar_expresion(expresion):
    expresion = expresion.replace(' ', '')
    while '(' in expresion:
        parentesis_regex = re.compile(r'\(([^()]*)\)')
        subexpresion = parentesis_regex.search(expresion).group(1)
        resultado_subexpresion = realizar_operaciones(subexpresion)
        expresion = expresion.replace(
            f'({subexpresion})', str(resultado_subexpresion))
    # Reemplazar variables con sus valores
    for var, val in variables.items():
        expresion = expresion.replace(var, str(val))
    return realizar_operaciones(expresion)

def solicitar_variables():
    while True:
        entrada = input('Ingresa la asignación de variable (Ejemplo: a = 56): ')
        asignar_variable(entrada)
        continuar = input("¿Deseas ingresar otra variable? (s/n): ")
        if not validar_respuesta(continuar):
            break

def validar_respuesta(respuesta):
    respuesta = respuesta.lower()
    while respuesta not in {'s', 'n'}:
        print("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")
        respuesta = input("¿Deseas ingresar otra variable? (s/n): ").lower()
    return respuesta == 's'

def main():
    usar_variables = input("¿Planeas utilizar variables? (s/n): ").lower()
    if usar_variables == 's':
        while True:
            entrada = input('Ingresa la asignación de variable (Ejemplo: a = 56): ')
            asignar_variable(entrada)
            print("Variables actuales:", variables)  # Agregamos esta línea para depurar
            continuar = input("¿Deseas ingresar otra variable? (s/n): ").lower()
            if continuar != 's':
                break

    while True:
        expresion = input('Ingresa la expresión matemática: (Ejemplo: a+b) ')
        print("Expresión ingresada:", expresion)  # Agregamos esta línea para depurar
        try:
            resultado = evaluar_expresion(expresion)
            print("El resultado de la operación es:", resultado)
        except ValueError as error:
            print(f"Error: {error}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

        continuar = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()