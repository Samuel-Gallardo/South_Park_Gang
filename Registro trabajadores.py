Salud=[]
afp=[]
trabajadores=[]
Cargo=[]
Sueldo=[]

def Opciones():
    while True:
        print("")
        opc=int(input("1.- Registrar Trabajador\n2.- Ver lista de todos los trabajadores\n3.- Imprimir lista de los sueldos\n4.-Salir\n"))
        match opc:
            case 1:
                Registrar_Trabajador()
            case 2:
                if opc==2 and trabajadores==[]:
                    print("No has registrado a ningun Trabajador")
                else:
                    Ver_Lista_Trabajadores()
            case 3 :
                if opc==3 and trabajadores==[]:
                    print("No has registrado a ningun Trabajador")
                else:
                    Imprimir_Lista_Sueldos()
            case 4 :
                exit()
            case any:
                print("Opcion no valida")

def Registrar_Trabajador():
    while True:
        trabajador=input("Ingrese el Nombre y el Apellido del trabajador (Mayuscula al inicio del Nombre y Apellido): ").title()
        if trabajador not in trabajadores :
            trabajadores.append(trabajador)
            break
        else:
            print("Este nombre ya esta registrado")
    cargo=int(input("Seleccione su Cargo\n1.- CEO\n2.- Desarrollador\n3.- Analista de Datos\n"))    

    match cargo:
        case 1 :
            if cargo==1 :
                cargo="CEO"
                Cargo.append(cargo)
        case 2 :
            if cargo==2:
                cargo="Desarrollador"
                Cargo.append(cargo)
        case 3 :
            if cargo==3:
                cargo="Analista de Datos"
                Cargo.append(cargo)
        
    sueldo=int(input("Ingrese su sueldo: "))
    Sueldo.append(sueldo)
    Salud.append(sueldo*0.07)
    afp.append(sueldo*0.12)
def Ver_Lista_Trabajadores():
    for i in range(len(trabajadores)):
        print(f"{i+1}.-{trabajadores[i]}")
def Imprimir_Lista_Sueldos():
    with open('registrosTrabajadores.txt','w') as registros:
        print("="*15,"LISTA DE SUELDO","="*15)
        for i in range(len(trabajadores)): #anotar en otro archivo
            registros.write(f"{i+1}.-{trabajadores[i]} | {Cargo[i]} | {Sueldo[i]} | {round(Salud[i])} | {round(afp[i])} | {Sueldo[i] - (Salud[i]+afp[i])}\n")

        for i in range(len(trabajadores)): #anotar en la terminal
            print(f"{i+1}.-{trabajadores[i]} | {Cargo[i]} | {Sueldo[i]} | {round(Salud[i])} | {round(afp[i])} | {Sueldo[i] - (Salud[i]+afp[i])}")
        print("="*47)
Opciones()    
