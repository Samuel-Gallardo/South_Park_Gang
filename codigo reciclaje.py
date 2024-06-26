
import json
import os
import platform


USERS_FILE = 'users.json'
PRODUCTS_FILE = 'products.json'

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def clear_screen():

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def register_user(users):
    clear_screen()
    username = input("Ingrese nombre de usuario: ")
    if username in users:
        print("El usuario ya existe.")
    else:
        users[username] = 0
        save_data(USERS_FILE, users)
        print(f"Usuario {username} registrado con éxito.")
    input("\nPresione Enter para continuar...")

def delete_user(users):
    clear_screen()
    username = input("Ingrese el nombre de usuario a eliminar: ")
    if username in users:
        del users[username]
        save_data(USERS_FILE, users)
        print(f"Usuario {username} eliminado con éxito.")
    else:
        print("Usuario no encontrado.")
    input("\nPresione Enter para continuar...")

def add_product(products):
    clear_screen()
    product_name = input("Ingrese el nombre del producto: ")
    points = int(input("Ingrese los puntos de recompensa por reciclar este producto: "))
    products[product_name] = points
    save_data(PRODUCTS_FILE, products)
    print(f"Producto {product_name} agregado con éxito.")
    input("\nPresione Enter para continuar...")

def recycle_product(users, products):
    clear_screen()
    username = input("Ingrese su nombre de usuario: ")
    if username not in users:
        print("Usuario no encontrado.")
        return

    product_name = input("Ingrese el nombre del producto a reciclar: ")
    if product_name not in products:
        print("Producto no encontrado.")
        return

    users[username] += products[product_name]
    save_data(USERS_FILE, users)
    print(f"Producto {product_name} reciclado. {username} ha recibido {products[product_name]} puntos. Total de puntos: {users[username]}")
    input("\nPresione Enter para continuar...")

def show_users(users):
    clear_screen()
    print("Usuarios registrados:\n")
    if not users:
        print("No hay usuarios registrados.")
    else:
        for username, points in users.items():
            print(f"Usuario: {username}, Puntos: {points}")
    input("\nPresione Enter para continuar...")

def show_products(products):
    clear_screen()
    print("Productos registrados:\n")
    if not products:
        print("No hay productos registrados.")
    else:
        for product, points in products.items():
            print(f"Producto: {product}, Puntos: {points}")
    input("\nPresione Enter para continuar...")

def welcome_message():
    clear_screen()
    print("\n" + "="*40)
    print("¡Bienvenido a la Aplicación de Reciclaje!")
    print("="*40 + "\n")
    print("Con esta aplicación, puedes:")
    print("1. Registrar nuevos usuarios")
    print("2. Añadir productos reciclables y sus recompensas")
    print("3. Registrar productos reciclados y obtener puntos")
    print("4. Consultar los puntos acumulados")
    print("5. Ver usuarios registrados")
    print("6. Ver productos registrados")
    print("7. Eliminar usuarios\n")
    print("¡Gracias por contribuir al reciclaje!")
    print("="*40 + "\n")

def main():
    users = load_data(USERS_FILE)
    products = load_data(PRODUCTS_FILE)

    welcome_message()

    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Añadir producto")
        print("3. Reciclar producto")
        print("4. Salir")
        print("5. Ver usuarios registrados")
        print("6. Ver productos registrados")
        print("7. Eliminar usuario")

        choice = input("Seleccione una opción: ")
        clear_screen()
        if choice == '1':
            register_user(users)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            recycle_product(users, products)
        elif choice == '4':
            clear_screen()
            print("Saliendo de la aplicación.")
            break
        elif choice == '5':
            show_users(users)
        elif choice == '6':
            show_products(products)
        elif choice == '7':
            delete_user(users)
        else:
            print("Opción no válida.")
            input("\nPresione Enter para continuar...")
if __name__ == "__main__":
    main()
