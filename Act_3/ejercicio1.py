import json

# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, edad, salario_bruto):
        self.nombre = nombre
        self.edad = edad
        self.salario_bruto = salario_bruto

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "salario_bruto": self.salario_bruto
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["edad"], data["salario_bruto"])

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario Bruto: {self.salario_bruto}"

# Definición de la clase Director que hereda de Empleado
class Director(Empleado):
    def __init__(self, nombre, edad, salario_bruto, categoria):
        super().__init__(nombre, edad, salario_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def to_dict(self):
        data = super().to_dict()
        data["categoria"] = self.categoria
        data["subordinados"] = [e.to_dict() for e in self.subordinados]
        return data

    @classmethod
    def from_dict(cls, data):
        director = cls(data["nombre"], data["edad"], data["salario_bruto"], data["categoria"])
        director.subordinados = [Empleado.from_dict(e) for e in data["subordinados"]]
        return director

    def __str__(self):
        return super().__str__() + f", Categoría: {self.categoria}, Subordinados: {', '.join([e.nombre for e in self.subordinados])}"

# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "telefono": self.telefono
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["edad"], data["telefono"])

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Teléfono: {self.telefono}"

# Función para guardar datos en archivos JSON
def guardar_datos(empleados, clientes):
    with open("empleados.json", "w") as archivo_empleados:
        json.dump([e.to_dict() for e in empleados], archivo_empleados, indent=4)
    
    with open("clientes.json", "w") as archivo_clientes:
        json.dump([c.to_dict() for c in clientes], archivo_clientes, indent=4)

# Función para cargar datos desde archivos JSON
def cargar_datos():
    empleados = []
    clientes = []

    try:
        with open("empleados.json", "r") as archivo_empleados:
            datos_empleados = json.load(archivo_empleados)
            empleados = [Empleado.from_dict(e) for e in datos_empleados]

        with open("clientes.json", "r") as archivo_clientes:
            datos_clientes = json.load(archivo_clientes)
            clientes = [Cliente.from_dict(c) for c in datos_clientes]
    except FileNotFoundError:
        pass

    return empleados, clientes

# Función para el menú de Cliente
def menu_cliente():
    clientes = cargar_datos()[1]

    while True:
        print("Menú de Cliente")
        print("1. Registrarse como Cliente")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            edad = int(input("Ingrese la edad del cliente: "))
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = Cliente(nombre, edad, telefono)
            clientes.append(cliente)
            print("¡Cliente registrado exitosamente!")
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Función para iniciar sesión como Administrador
def inicio_sesion_administrador():
    contraseña = "1234"  # Contraseña del administrador

    while True:
        contraseña_admin = input("Ingrese la Contraseña del Administrador: ")
        if contraseña_admin == contraseña:
            menu_administrador()
            break
        else:
            print("Contraseña incorrecta. Por favor, inténtelo nuevamente.")

# Función para el menú de Administrador
def menu_administrador():
    empleados, clientes = cargar_datos()

    while True:
        print("Menú de Administrador")
        print("1. Agregar Empleado")
        print("2. Agregar Director")
        print("3. Mostrar Empleados")
        print("4. Mostrar Clientes")
        print("5. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del empleado: ")
            edad = int(input("Ingrese la edad del empleado: "))
            salario = float(input("Ingrese el salario bruto del empleado: "))
            empleado = Empleado(nombre, edad, salario)
            empleados.append(empleado)
            print("Empleado agregado exitosamente!")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del director: ")
            edad = int(input("Ingrese la edad del director: "))
            salario = float(input("Ingrese el salario bruto del director: "))
            categoria = input("Ingrese la categoría del director: ")
            director = Director(nombre, edad, salario, categoria)
            empleados.append(director)
            print("Director agregado exitosamente!")
        elif opcion == "3":
            for empleado in empleados:
                print(empleado)
        elif opcion == "4":
            for cliente in clientes:
                print(cliente)
        elif opcion == "5":
            guardar_datos(empleados, clientes)
            break
        else:
            print("Opción inválida. Por favor, inténtelo nuevamente.")

# Función principal que inicia el programa
def main():
    while True:
        print("Menú Principal")
        print("1. Menú de Cliente")
        print("2. Iniciar Sesión como Administrador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            inicio_sesion_administrador()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, inténtelo nuevamente.")

if __name__ == "__main__":
    main()
