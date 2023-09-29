import json
from datetime import datetime

# Clase para representar un Cliente
class Cliente:
    def __init__(self, codigo, cedula, nombre, direccion, telefono):
        self.codigo = codigo
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

# Clase para representar un Coche
class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

# Clase para representar una Reserva
class Reserva:
    def __init__(self, cliente, agencia, fecha_inicio, fecha_fin, precio_alquiler, litros_gasolina, entregado):
        self.cliente = cliente
        self.agencia = agencia
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_alquiler = precio_alquiler
        self.litros_gasolina = litros_gasolina
        self.entregado = entregado
        self.autos = []

    def agregar_auto(self, coche):
        self.autos.append(coche)

# Función para guardar los datos en un archivo JSON
def guardar_datos(clientes):
    data = {
        "clientes": [cliente.__dict__ for cliente in clientes]
    }
    with open("datos.json", "w") as archivo_json:
        json.dump(data, archivo_json, indent=4)

# Función para cargar los datos desde un archivo JSON
def cargar_datos():
    try:
        with open("datos.json", "r") as archivo_json:
            data = json.load(archivo_json)
            clientes = [Cliente(**cliente_data) for cliente_data in data["clientes"]]
            return clientes
    except FileNotFoundError:
        return []

# Función para crear un cliente interactivamente
def crear_cliente():
    codigo = int(input("Ingrese el código del cliente: "))
    cedula = input("Ingrese la cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    return Cliente(codigo, cedula, nombre, direccion, telefono)

# Función para crear un coche interactivamente
def crear_coche():
    matricula = input("Ingrese la matrícula del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    color = input("Ingrese el color del coche: ")
    marca = input("Ingrese la marca del coche: ")
    garaje = input("Ingrese el garaje del coche: ")
    return Coche(matricula, modelo, color, marca, garaje)

# Función para crear una reserva interactivamente
def crear_reserva():
    cliente = crear_cliente()
    agencia = input("Ingrese la agencia de alquiler: ")
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    precio_alquiler = float(input("Ingrese el precio de alquiler: "))
    litros_gasolina = float(input("Ingrese los litros de gasolina: "))
    entregado = input("¿El auto fue entregado? (Sí/No): ").lower() == "sí"

    reserva = Reserva(cliente, agencia, fecha_inicio, fecha_fin, precio_alquiler, litros_gasolina, entregado)

    num_autos = int(input("¿Cuántos autos alquiló el cliente?: "))
    for _ in range(num_autos):
        coche = crear_coche()
        reserva.agregar_auto(coche)

    cliente.agregar_reserva(reserva)
    return reserva

# Función para mostrar la información de un cliente y sus reservas
def mostrar_info_cliente(cliente):
    print("Información del Cliente:")
    print("Código:", cliente.codigo)
    print("Cédula:", cliente.cedula)
    print("Nombre:", cliente.nombre)
    print("Dirección:", cliente.direccion)
    print("Teléfono:", cliente.telefono)
    print("Reservas:")
    for reserva in cliente.reservas:
        print("- Fecha de inicio:", reserva.fecha_inicio)
        print("- Fecha de fin:", reserva.fecha_fin)
        print("- Autos alquilados:")
        for auto in reserva.autos:
            print("  - Matrícula:", auto.matricula)
            print("  - Modelo:", auto.modelo)
            print("  - Color:", auto.color)
            print("  - Marca:", auto.marca)
            print("  - Garaje:", auto.garaje)
        print("- Precio de alquiler:", reserva.precio_alquiler)
        print("- Litros de gasolina:", reserva.litros_gasolina)
        print("- Entregado:", "Sí" if reserva.entregado else "No")
        print("")

# Cargar datos existentes o crear una lista vacía si no hay datos
clientes = cargar_datos()

while True:
    print("\nBienvenido al sistema de gestión de reservas de alquiler de automóviles")
    print("1. Crear reserva")
    print("2. Mostrar información de cliente")
    print("3. Guardar y salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        reserva = crear_reserva()
        print("Reserva creada exitosamente.")

    elif opcion == "2":
        codigo_cliente = int(input("Ingrese el código del cliente: "))
        cliente_encontrado = None
        for cliente in clientes:
            if cliente.codigo == codigo_cliente:
                cliente_encontrado = cliente
                break
        if cliente_encontrado:
            mostrar_info_cliente(cliente_encontrado)
        else:
            print("Cliente no encontrado.")

    elif opcion == "3":
        guardar_datos(clientes)
        print("Datos guardados correctamente. Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
