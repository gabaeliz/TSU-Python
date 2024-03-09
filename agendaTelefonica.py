class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        if nombre in self.contactos:
            print(f'El contacto {nombre} ya existe en la agenda.')
        elif not telefono.isdigit() or len(telefono) != 10:
            print('El número de teléfono debe contener 10 dígitos.')
        else:
            self.contactos[nombre] = telefono
            print(f"Contacto {nombre} agregado.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def actualizar_contacto(self, nombre, nuevo_telefono):
        if nombre in self.contactos:
            self.contactos[nombre] = nuevo_telefono
            print(f"Contacto {nombre} actualizado.")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def buscar_contacto_por_nombre(self, nombre):
        if nombre in self.contactos:
            print(f"Nombre: {nombre}, Teléfono: {self.contactos[nombre]}")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def buscar_contacto_por_numero(self, telefono):
        encontrado = False
        for nombre, num in self.contactos.items():
            if num == telefono:
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
                encontrado = True
        if not encontrado:
            print(f"No se encontró ningún contacto con el número {telefono}.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for nombre, telefono in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("La agenda está vacía.")


def mostrar_menu():
    print(
        '''
    ------------
    | Opciones |
    ------------

    1. Agregar contacto
    2. Eliminar contacto
    3. Actualizar contacto  
    4. Buscar contacto por nombre
    5. Mostrar todos los contactos
    6. Agregar múltiples contactos
    7. Buscar contacto por número
    8. Salir
    ''')


def obtener_opcion():
    return input("Ingrese el número de la opción que desee: ")


def ingresar_multiples_contactos(agenda):
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agenda.agregar_contacto(nombre, telefono)
        decide = input('¿Desea agregar otro contacto?: si/no ')
        if decide.lower() != 'si':
            break


def main():
    agenda = Agenda()
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agenda.agregar_contacto(nombre, telefono)
        elif opcion == "2":
            nombre = input(
                "Ingrese el nombre del contacto que desea eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == "3":
            nombre = input(
                "Ingrese el nombre del contacto que desea actualizar: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            agenda.actualizar_contacto(nombre, nuevo_telefono)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            agenda.buscar_contacto_por_nombre(nombre)
        elif opcion == "5":
            agenda.mostrar_contactos()
        elif opcion == "6":
            ingresar_multiples_contactos(agenda)
        elif opcion == '7':
            telefono = input(
                "Ingrese el número del contacto que desea buscar: ")
            if not telefono.isdigit() or len(telefono) != 10:
                print(f'{telefono} no es una opción válida')
            else:
                agenda.buscar_contacto_por_numero(telefono)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")


if __name__ == "__main__":
    main()
