import json
import random

class Ticket:
    def __init__(self, location, price, date):
        self.id = random.randint(1000, 9999)
        self.location = location
        self.price = price
        self.date = date

tickets = [
    Ticket("Venecia", 100, "2023-08-16"),
    Ticket("Luxemburgo", 200, "2023-08-16"),
    Ticket("Manchester", 300, "2023-08-16")
]


class Client:
    def __init__(self, name, card_info, saldo, ticket_purchased=None):
        self.name = name
        self.card_info = card_info
        self.ticket_purchased = ticket_purchased if ticket_purchased is not None else []
        self.saldo = saldo

    def display_info(self):
        print("Nombre ingresado:", self.name)
        print("Informacion de la tarjeta:", self.card_info)
        print("Tickets comprados:", [ticket.location for ticket in self.ticket_purchased])
        print("Saldo:", self.saldo.valor)

class Saldo:
    def __init__(self, saldo_inicial=0):
        self.valor = saldo_inicial

saldo = Saldo()

def save_clients(clients):
    with open("clients.json", "w") as file:
        client_list = [
            {
                "name": client.name,
                "card_info": client.card_info,
                "ticket_purchased": [ticket.location for ticket in client.ticket_purchased]
            }
            for client in clients
        ]
        json.dump(client_list, file)

def load_clients():
    try:
        with open("clients.json", "r") as file:
            client_list = json.load(file)
            clients = []
            for client_data in client_list:
                name = client_data["name"]
                card_info = client_data["card_info"]
                ticket_names = client_data["ticket_purchased"]
                ticket_purchased = [ticket for ticket in tickets if ticket.location in ticket_names]
                new_client = Client(name, card_info, saldo, ticket_purchased)
                clients.append(new_client)
            return clients
    except FileNotFoundError:
        return []

def main():
    clients = load_clients()

    tickets = [
        Ticket("Venecia", 100, "2023-08-16"),
        Ticket("Luxemburgo", 200, "2023-08-16"),
        Ticket("Manchester", 300, "2023-08-16")
    ]
    
    while True:
        print("Bienvenido a la estacion Plaza Sesamo. Por favor, selecciona una opción:")
        print("1. Crear cuenta")
        print("2. Iniciar sesion")
        print("3. SALIR")
        choice = input("Seleccione una opcion: ")

        if choice == "1":
            while True:
                name = input("Ingrese su nombre (máximo 30 caracteres todo junto sin espacios): ")
                if not name.isalpha():
                    print("El nombre no debe contener números ni caracteres especiales. Intente nuevamente.")
                elif len(name) > 30:
                    print("El nombre excede el límite de 30 caracteres. Intente nuevamente.")
                else:
                    break

            while True:
                owner_card = input("Ingrese el propietario de la tarjeta (Nombre completo todo junto sin espacios y en mayusculas)")
                owner_card = owner_card.lower()
                if len(owner_card) > 30:
                    print("El Nombre propietario excede el limite de 30 caracteres. Intente nuevamente.")
                elif not name.isalpha():
                    print("El nombre no debe contener números ni caracteres especiales. Intente nuevamente.")
                else:
                    break

            while True:
                card_brand = input("Ingrese la marca de su tarjeta (Visa, Mastercard, American Express, Diners Club): ")
                card_brand = card_brand.lower()

                if card_brand in ["visa", "mastercard", "american express", "diners club"]:
                    break
                else:
                    retry = input("La marca de tarjeta no es válida. ¿Desea intentarlo nuevamente? (Si/No: ")
                    if retry.lower() != "si":
                        break
            
            while True:
                while True:
                    card_number = input("Ingrese el número de tarjeta (sin espacios): ")

                    if not card_number.isdigit():
                        print("El número de tarjeta solo puede contener dígitos.")
                        continue

                    card_number_length = len(card_number)
                    if card_number_length < 13 or card_number_length > 18:
                        print("La longitud del número de tarjeta debe estar entre 13 y 18 dígitos.")
                        continue

                    break
                
                
                if any(client.card_info["numero de tarjeta"] == str(card_number) for client in clients):
                    print("Este número de tarjeta ya está registrado. Por favor, intente con otra tarjeta.")
                    continue

                break
            while True:
                card_expiry = input("Ingrese la fecha de vencimiento (MM/YY sin el /): ")
                card_expiry_year = int("20" + card_expiry[2:4]) if len(card_expiry) == 4 else None

                if not card_expiry.isdigit() or len(card_expiry) != 4 or not (2024 <= card_expiry_year <= 2029):
                    print("La fecha de vencimiento es incorrecta o inválida.")
                    continue

                break
            
            while True:
                card_cvv = input("Ingrese el código de verificación (CVV, tres dígitos): ")
                if not card_cvv.isdigit() or len(card_cvv) != 3:
                    print("El CVV es inválido. Debe tener tres dígitos.")
                    continue

                def check_duplicate_card(card_number, card_expiry):
                    for c in clients:
                        if c.card_info["numero de tarjeta"] == card_number and c.card_info["vencimiento"] == card_expiry:
                            return True
                    return False
                
                if check_duplicate_card(card_number, card_expiry):
                    print("Esta combinación de número de tarjeta y fecha de vencimiento ya está registrada.")
                    print("Por favor, intente con otra tarjeta o fecha de vencimiento.")
                    continue
                break

            if len(clients) < 10:
                new_saldo = Saldo(500)
                print("¡Bienvenido a la estacion Plaza Sesamo! Por ser uno de los primeros en generar la cuenta, se le otorga un saldo de $500.")
            else:
                new_saldo = Saldo()

            card_info ={
                "Propietario": owner_card,
                "marca": card_brand,
                "numero de tarjeta": str(card_number),
                "vencimiento": card_expiry,
                "codigo de verificacion": card_cvv
            }
            new_client = Client(name, card_info, new_saldo)
            clients.append(new_client)  # Aquí agregamos el nuevo cliente a la lista clients
            save_clients(clients)  
            print("Cuenta creada exitosamente.")

        elif choice == "2":
            name = input("Ingrese su nombre: ")
            found_client = None
            for client in clients:
                if client.name == name:
                    found_client = client
                    break
            if found_client:
                while True:
                    print("Menu")
                    print("1. Ver la informacion de cuenta")
                    print("2. Comprar un Ticket")
                    print("3. Mirar los horarios de salida")
                    print("4. Cerrar sesion")
                    user_choice = input()

                    if user_choice == "1":
                        found_client.display_info()
                    elif user_choice == "2":
                        buy_ticket(found_client, clients, tickets)
                    elif user_choice == "3":
                        print("HORARIOS DE SALIDA")
                        for ticket in tickets:
                            print(f"Ubicación: {ticket.location} - Hora de salida: {ticket.date}")
                    elif user_choice == "4":
                        print("SESION CERRADA GRACIAS POR SU PREFERENCIA")
                        save_clients(clients)
                        break
                    else:
                        print("Opcion invalida, porfavor selesccione una opcion valida")
            else:
                print("Nombre de usuario incorrecto")
        elif choice == "3":
            print("Gracias por consultarnos tenga un buen dia ")

def buy_ticket(client, clients, tickets):

    print("Tickets disponibles")
    for idx, ticket in enumerate(tickets, start=1):
        print(f"{idx}. ID: {ticket.id}, Ubicación: {ticket.location} - ${ticket.price} - Fecha de salida: {ticket.date}")

    try:
        ticket_choice = int(input("Seleccione el ticket que desea comprar (1 - 3): ")) - 1

        if 0 <= ticket_choice < len(tickets):
            selected_ticket = tickets[ticket_choice]

            if selected_ticket in client.ticket_purchased:
                print("Ya se ha comprado este ticket")
            elif client.saldo.valor >= selected_ticket.price:
                client.ticket_purchased.append(selected_ticket)
                client.saldo.valor -= selected_ticket.price
                print(f"¡HAS COMPRADO {selected_ticket.location} por ${selected_ticket.price}! Saldo restante: ${client.saldo.valor}")
                print(f"ID de tu ticket: {selected_ticket.id}")
                save_clients(clients)
            else:
                print("SALDO INSUFICIENTE PARA COMPRAR ESTE TICKET")
        else:
            print("Opción inválida")
    except ValueError:
        print("Opción inválida")

if __name__ == "__main__":
    main()