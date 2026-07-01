def mostrar_menu():
    print("========== MENÚ PRINCIPAL ===========")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    print("====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            continue

        if 1 <= opcion <= 6:
            return opcion

        print("Error: Opción inválida. Debe ingresar un número entre 1 y 6.")


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_edad(edad):
    try:
        edad_num = int(edad)
        return edad_num > 0
    except ValueError:
        return False


def validar_temperatura(temperatura):
    try:
        temp_num = float(temperatura)
        return 35.0 <= temp_num <= 42.0
    except ValueError:
        return False


def agregar_paciente(pacientes):
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    temperatura = input("Ingrese la temperatura del paciente: ")

    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío.")
        return

    if not validar_edad(edad):
        print("Error: La edad debe ser un número entero mayor que cero.")
        return

    if not validar_temperatura(temperatura):
        print("Error: La temperatura debe ser un número decimal entre 35.0 y 42.0.")
        return

    paciente = {
        "nombre": nombre,
        "edad": int(edad),
        "temperatura": float(temperatura),
        "atendido": False,
    }
    pacientes.append(paciente)
    print("Paciente agregado correctamente.")


def buscar_paciente(pacientes, nombre):
    for i, paciente in enumerate(pacientes):
        if paciente["nombre"] == nombre:
            return i
    return -1


def actualizar_estado(pacientes):
    for paciente in pacientes:
        paciente["atendido"] = paciente["temperatura"] <= 37.0


def mostrar_pacientes(pacientes):
    actualizar_estado(pacientes)
    print("=== LISTA DE PACIENTES ===")
    for paciente in pacientes:
        estado = "ATENDIDO" if paciente["atendido"] else "REQUIERE ATENCION"
        print(f"Nombre: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Temperatura: {paciente['temperatura']}")
        print(f"Estado: {estado}")
        print("********************************************")


pacientes = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_paciente(pacientes)
    elif opcion == 2:
        nombre = input("Ingrese el nombre del paciente a buscar: ")
        posicion = buscar_paciente(pacientes, nombre)
        if posicion != -1:
            paciente = pacientes[posicion]
            print(f"Paciente encontrado en la posición {posicion}.")
            print(f"Nombre: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}")
            print(f"Temperatura: {paciente['temperatura']}")
            estado = "ATENDIDO" if paciente["atendido"] else "REQUIERE ATENCION"
            print(f"Estado: {estado}")
        else:
            print(f"No se encontró al paciente {nombre}.")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del paciente a eliminar: ")
        posicion = buscar_paciente(pacientes, nombre)
        if posicion != -1:
            del pacientes[posicion]
            print(f"Paciente {nombre} eliminado correctamente.")
        else:
            print(f"El paciente '{nombre}' no se encuentra registrado.")
    elif opcion == 4:
        actualizar_estado(pacientes)
        print("Estados actualizados correctamente.")
    elif opcion == 5:
        mostrar_pacientes(pacientes)
    else:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
