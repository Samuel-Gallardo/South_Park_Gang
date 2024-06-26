import getpass, time
Usuarios_Registrados=[]
material_reciclable=["Plastico", "Carton", "Vidrio", "Pilas", "Metal"]
plastico_reciclable=["Botellas(Shampoo, Agua, Detergente)","Tapas", "Otro:"]
carton_reciclable=["Caja", "Otro:"]
vidrio_reciclable=["Botellas", "Frascos", "Otro:"]
metal_reciclable=["Acero", "Aluminio", "Cobre", "Otro:"]
puntos_material=[1,5,10,15,20,25,30]
mis_puntos=[]
sugerencias=[]
               
def inicio_sesion():
    opc=(int(input("¿Que desea hacer?\n1.- Inicio Sesion\n2.- Registrar Nuevo Usuario\n>")))
    match opc:
        case 1:
            verificar_user=input("Ingrese su Nombre de Usuario").title()
            if verificar_user in Usuarios_Registrados:
                print("Ingrese Su Contraseña\n>")
            else:
                print("Este usuario no esta en nuestro sistema")
        case 2:
            usuario=input("Ingrese el Nombre y el Apellido del Usuario : ").title()
            if usuario not in Usuarios_Registrados :
                Usuarios_Registrados.append(usuario)
                Contraseña=getpass.getpass("Crea una Contraseña (Si no te aparecen caracteres, no te preocupes, Se esta registrando igual para mantener tu privacidad)\n>")
                while True:
                    otra_contraseña=getpass.getpass("Vuelve a ingresar tu contraseña\n>")
                    if otra_contraseña==Contraseña:
                        print(f"Bienvenido {usuario}")
                        Opciones()
                        break
                    else:
                        print("Contraseña incorrecta")
            else:
                print("Este nombre ya esta registrado")

def Opciones():
    while True:
        print("")
        opc=int(input("1.- Registrar producto reciclado\n2.- Ver lista de todos los Usuarios\n3.- Ver Productos Reciclables\n4.- Ver puntos de reciclaje cercanos\n5.- Ver canjes\n6.- Cerrar sesion\n>"))
        match opc:
            case 1:
                registrar_producto()
            case 2:
                if opc==2 and Usuarios_Registrados==[]:
                    print("No has registrado a ningun usuario")
                else:
                    Ver_Lista_Usuarios()
            case 3 :
                for i in range(len(material_reciclable)):
                    material_reciclable.sort()
                    puntos_material.sort()
                    print(f"{i+1}.- {material_reciclable[i]}")
            case 4 :
                print()
            case 5:
                print()
            case 6:
                print("Gracias por aportar con el medio ambiente")
                time.sleep(1)
                print("Cerrando sesion...")
                time.sleep(2)
                inicio_sesion()
            case any:
                print("Opcion no valida")

def registrar_producto():
    material=int(input("Seleccione el tipo de material el que esta reciclando\n1.- Plastico\n2.- Carton\n3.- Vidrio\n4.- Pilas\n5.- Metales\n>"))    
    if material == 1:
        material="Plastico"
        for i in range(len(plastico_reciclable)):
            print(f"{i+1}.- {plastico_reciclable[i]}")
        objeto=int(input("¿Que objeto es el que esta reciclando?"))
        match objeto:
            case 1:
                print(f"Producto Reciclado, Has obtenido {puntos_material[2]} puntos")
                mis_puntos.append(puntos_material[2])
            case 2:
                cant=int(input(f"¿Cuantas {plastico_reciclable[1]} tienes?"))
                print(f"Producto Reciclado, Has obtenido {puntos_material[0]*cant} puntos")
                mis_puntos.append(puntos_material[0]*cant)
            case 3:
                otro_plastico=input("¿Que material es?")
                print("Evaluaremos el producto para añadirlo a nuestro sistema\nPor tu aporte, te daremos 10 puntos")
                mis_puntos.append(puntos_material[1])
                with open('plasticos.txt', 'w') as archivo:
                    archivo.write(f"{otro_plastico}\n")

    if material == 2:
        material="Carton"
        for i in range(len(carton_reciclable)):
            print(f"{i+1}.- {carton_reciclable[i]}")
        objeto=int(input("¿Que objeto es el que esta reciclando?"))
        match objeto:
            case 1:
                tamaño=int(input("¿De que tamaño es la caja?\n1.- Pequeña\n2.- Mediana\n3.- Grande\n"))
                match tamaño:
                    case 1 :
                        print(f"Producto Reciclado, Has obtenido {puntos_material[1]} puntos")
                        mis_puntos.append(puntos_material[1])
                    case 2 :
                        print(f"Producto Reciclado, Has obtenido {puntos_material[2]} puntos")
                        mis_puntos.append(puntos_material[2])
                    case 3 :
                        print(f"Producto Reciclado, Has obtenido {puntos_material[3]} puntos")
                        mis_puntos.append(puntos_material[3])
            case 2:
                otro_Carton=input("¿Que material es?")
                print("Evaluaremos el producto para añadirlo a nuestro sistema\nPor tu aporte, te daremos 10 puntos")
                mis_puntos.append(puntos_material[1])
                with open('carton.txt', 'w') as archivo:
                    archivo.write(f"{otro_plastico}\n")
            case any :
                print("Opcion Invalida")
                
            
    if material == 3:
        material="Vidrio"
        for i in range(len(vidrio_reciclable)):
            print(f"{i+1}.- {vidrio_reciclable[i]}")
        objeto=int(input("¿Que objeto es el que esta reciclando?"))
        match objeto:
            case 1:
                print(f"Producto Reciclado, Has obtenido {puntos_material[2]} puntos")
                mis_puntos.append(puntos_material[2])
            case 2:
                print(f"Producto Reciclado, Has obtenido {puntos_material[1]} puntos")
                mis_puntos.append(puntos_material[1])

            case 3 :
                otro_vidrio=input("¿Que material es?")
                print("Evaluaremos el producto para añadirlo a nuestro sistema\nPor tu aporte, te daremos 10 puntos")
                mis_puntos.append(puntos_material[1])
                with open('vidrio.txt', 'w') as archivo:
                    archivo.write(f"{otro_vidrio}\n")

    if material == 4:
        material="Pilas"
        cant=int(input(f"¿Cuantas {material_reciclable[3]} tienes?"))
        print(f"Producto Reciclado, Has obtenido {puntos_material[0]*cant} puntos")
        mis_puntos.append(puntos_material[0]*cant)
        
    if material == 5:
        material="Metales"
        for i in range(len(metal_reciclable)):
            print(f"{i+1}.- {metal_reciclable[i]}")
        objeto=int(input("¿Que objeto es el que esta reciclando?"))
        match objeto:
            case 1:
                print(f"Producto Reciclado, Has obtenido {puntos_material[3]} puntos")
                mis_puntos.append(puntos_material[3])
            case 2:
                print(f"Producto Reciclado, Has obtenido {puntos_material[3]} puntos")
                mis_puntos.append(puntos_material[3])
            case 3 :
                print(f"Producto Reciclado, Has obtenido {puntos_material[3]} puntos")
                mis_puntos.append(puntos_material[3])

            case 4:
                otro_metal=input("¿Que material es?")
                print("Evaluaremos el producto para añadirlo a nuestro sistema\nPor tu aporte, te daremos 10 puntos")
                mis_puntos.append(puntos_material[2])
                with open('metal.txt', 'w') as archivo:
                    archivo.write(f"{otro_metal}\n")

def Ver_Lista_Usuarios():
    for i in range(len(Usuarios_Registrados)):
        Usuarios_Registrados.sort() #ordenar Alfabeticamente
        print(f"{i+1}.-{Usuarios_Registrados[i]}    |   Puntos: {sum(mis_puntos)}")

inicio_sesion()