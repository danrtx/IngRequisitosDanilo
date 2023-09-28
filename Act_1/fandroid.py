import json

class Saldo:
    def __init__(self, saldo_inicial=0):
        self.valor = saldo_inicial

saldo = Saldo()

class Application:
    def __init__(self, name, price):
        self.name = name
        self.price = price

applications = [
    Application("Subway Surfers", 8000),
    Application("Plantas Vs Zombies", 12000),
    Application("Calculadora", 15000)
]

class Customer:
    def __init__(self, name, card_info, points, saldo, password, apps_purchased=[]):
        self.name = name
        self.card_info = card_info
        self.points = points
        self.saldo = saldo
        self.password = password
        self.apps_purchased = apps_purchased

    def display_info(self):
        print("Nombre:", self.name)
        print("Información de tarjeta:", self.card_info)
        print("Puntos acumulados:", self.points)
        print("Saldo:", self.saldo.valor)
        print("Aplicaciones compradas:",self.apps_purchased)


def save_customers(customers):
    with open("customers.json", "w") as file:
        customer_list = [
            {
                "name": customer.name.lower(),
                "card_info": customer.card_info,
                "points": customer.points,
                "saldo": customer.saldo.valor,
                "password": customer.password,
                "apps_purchased": customer.apps_purchased
            }
            for customer in customers
        ]
        json.dump(customer_list, file)

def load_customers():
    try:
        with open("customers.json", "r") as file:
            customer_list = json.load(file)
            customers = []
            for customer_data in customer_list:
                name = customer_data["name"]
                card_info = customer_data["card_info"]
                points = customer_data["points"]
                saldo = Saldo(customer_data["saldo"])
                password = customer_data["password"]
                apps_purchased = customer_data.get("apps_purchased", [])
                customer = Customer(name, card_info, points, saldo, password, apps_purchased)
                customers.append(customer)
            return customers
    except FileNotFoundError:
        return []


customers = load_customers()

def main():
    customers = []
    customers = load_customers()

    while True:
        print("\nBienvenido a Fandroid - Plataforma de Venta de Aplicaciones")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            while True:
                name = input("Ingrese su nombre (máximo 30 caracteres): ")
                if len(name) > 30:
                    print("El nombre excede el límite de 30 caracteres. Intente nuevamente.")
                else:
                    break
            
            while True:
                password = input("Ingrese una contraseña (mínimo 6 caracteres, debe contener al menos una letra y un número): ")
                if len(password) < 6:
                    print("La contraseña debe tener al menos 6 caracteres.")
                elif not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                    print("La contraseña debe contener al menos una letra y un número.")
                else:
                    break
            
            while True:
                owner_card = input("Ingrese el propietario de la tarjeta (Nombre completo con espacios y en mayusculas)")
                owner_card = owner_card.lower()
                if len(owner_card) > 30:
                    print("El Nombre propietario excede el limite de 30 caracteres. Intente nuevamente.")
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
            
                if any(customer.card_info["número de tarjeta"] == card_number for customer in customers):
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
                
                if any(
                    customer.card_info["número de tarjeta"] == card_number and
                    customer.card_info["vencimiento"] == card_expiry
                    for customer in customers
                ):
                    print("Esta combinación de número de tarjeta y fecha de vencimiento ya está registrada.")
                    print("Por favor, intente con otra tarjeta o fecha de vencimiento.")
                    continue

                break
            if len(customers) < 10:
                new_saldo = Saldo(50000)
                print("¡Bienvenido a Fandroid! Por ser uno de los primeros en generar la cuenta, se le otorga un saldo de $50000.")
            else:
                new_saldo = Saldo()
            
            card_info = {
                "Propietario" : owner_card,
                "marca": card_brand,
                "número de tarjeta": card_number,
                "vencimiento": card_expiry,
                "código de verificación": card_cvv
            }
            customer = Customer(name, card_info, 0, new_saldo,password)
            customers.append(customer)
            save_customers(customers)  
            print("Cuenta creada exitosamente.")
        elif choice == "2":
            name = input("Ingrese su nombre: ").lower()
            password = input("Ingrese su contraseña: ")
            found_customer = None
            for customer in customers:
                if customer.name == name and customer.password == password:
                    found_customer = customer
                break

            if found_customer:
                print("¡Bienvenido,", found_customer.name, "!")
                while True:
                    print("Menú")
                    print("1. Ver la información de la cuenta")
                    print("2. Comprar una aplicación")
                    print("3. Consulta de puntos acumulados")
                    print("4. Canjeo de puntos por premios")
                    print("5. Cerrar sesión")
                    user_choice = input("Seleccione una opción: ")

                    if user_choice == "1":
                        found_customer.display_info()
                    elif user_choice == "2":
                        buy_application(found_customer)
                    
                    elif user_choice == "3":
                        print("Puntos acumulados:", found_customer.points)

                    elif user_choice == "4":
                        print("Puntos acumulados:", found_customer.points)
                        print("Opciones de canje:")
                        print("1. Canjear 1000 puntos por un bono de $100000")
                        print("2. Canjear 2000 puntos por un bono de $250000")
                        print("3. Canjear 3000 puntos por un bono de $400000")
                        print("4. Volver al Menú Principal")

                        redemption_choice = input("Seleccione una opción de canje (1-4): ")

                        if redemption_choice == "1":
                            if found_customer.points >= 1000:
                                found_customer.points -= 1000
                                saldo += 100000
                                print("¡Canje realizado! Ha obtenido un bono de $100000.")
                                save_customers(customers)
                            else:
                                print("No tiene suficientes puntos para realizar este canje.")

                        elif redemption_choice == "2":
                            if found_customer.points >= 2000:
                                found_customer.points -= 2000
                                saldo += 250000
                                print("¡Canje realizado! Ha obtenido un bono de $250000.")
                                save_customers(customers)
                            else:
                                print("No tiene suficientes puntos para realizar este canje.")

                        elif redemption_choice == "3":
                            if found_customer.points >= 3000:
                                found_customer.points -= 3000
                                saldo += 400000
                                print("¡Canje realizado! Ha obtenido un bono de $400000.")
                                save_customers(customers)
                            else:
                                print("No tiene suficientes puntos para realizar este canje.")

                        elif redemption_choice == "4":
                            print("Volviendo al Menú Principal.")

                        else:
                            print("Opción no válida. Por favor, seleccione una opción válida.")
                    


                    elif user_choice == "5":
                        print("Sesión cerrada.")
                        save_customers(customers)
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")

            else:
                print("Nombre de usuario o contraseña incorrectos.")

        elif choice == "3":
            print("Gracias por usar Fandroid. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def buy_application(customer):
    print("\nCatálogo de aplicaciones:")
    for idx, app in enumerate(applications, start=1):
        print(f"{idx}. {app.name} - ${app.price}")

    app_choice = input("\nSeleccione la aplicación que desea comprar (1-3): ")
    app_choice = int(app_choice) - 1

    if 0 <= app_choice < len(applications):
        selected_app = applications[app_choice]
        
        if selected_app.name in customer.apps_purchased:
            print("Ya ha comprado esta aplicación previamente.")
        elif customer.saldo.valor >= selected_app.price:
            customer.saldo.valor -= selected_app.price
            customer.points += int(selected_app.price / 1000)
            customer.apps_purchased.append(selected_app.name)
            print(f"¡Ha comprado {selected_app.name} por ${selected_app.price}! Saldo restante: ${customer.saldo.valor}")
            save_customers(customers)
        else:
            print("Saldo insuficiente para comprar esta aplicación.")
    else:
        print("Opción no válida.")
if __name__ == "__main__":
    main()