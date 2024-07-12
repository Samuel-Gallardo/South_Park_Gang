Alimentos=["Uvas","Peras","Manzanas","Zanahorias"]
stock=[20,20,20,20]
Precios=[1000,1500,2000,2500]
productoComprado=[]
carrito=[]
total=[]


sueldosmax=max(sueldos)
    sueldomin=min(sueldos)
    promediosueldo=sum(sueldos)/10
    producto=prod(sueldos)
    mediaG=producto**(1/10)
    
    print(f"Sueldo Maximo: {sueldosmax}")
    print(f"Sueldo Minimo: {sueldomin}")
    print(f"Promedio de Sueldos: {promediosueldo}")
    print(f"Media Geometrica: {mediaG:.2f}")


def opciones():
    while True:
        print("\n1.- Comprar Productos\n2.- Ver Carrito de Compra\n3.- Pagar\n4.- Salir")
        opc=int(input(">"))
        match opc:
            case 1 :
                Comprar()
            case 2:
                if total==[]:
                    print("No has comprado nada aun")
                else:
                    for i in range(len(carrito)):
                        print(f"Producto: {carrito[i]}    |   Cantidad: {productoComprado[i]}   |   Precio: {total[i]}")
            case 3:
                if total==[]:
                    print("No has comprado nada aun")
                else:
                    Pagar_Compras()

def Productos():
    for i in range(len(Alimentos)):
        print(f"{i+1}.- {Alimentos[i]}  |   Precio: {Precios[i]}    |   Restante: {stock[i]}")

def Comprar():
    Productos()
    compra=int(input("¿Que desea comprar?"))
    match compra:
        case 1:
            cant=int(input(f"¿Cuantas {Alimentos[0]} desea llevar"))
            if cant<=stock[0]:
                stock[0]-=cant
                carrito.append(Alimentos[0])
                productoComprado.append(cant)
                total.append(cant*1000)
            else:
                print("Producto Insuficiente")
        case 2:
            cant=int(input(f"¿Cuantas {Alimentos[1]} desea llevar"))
            if cant<=stock[1]:
                stock[1]-=cant
                carrito.append(Alimentos[1])
                productoComprado.append(cant)
                total.append(cant*1500)
            else:
                print("Producto Insuficiente")
        case 3:
            cant=int(input(f"¿Cuantas {Alimentos[2]} desea llevar"))
            if cant<=stock[2]:
                stock[2]-=cant
                carrito.append(Alimentos[2])
                productoComprado.append(cant)
                total.append(cant*2000)
            else:
                print("Producto Insuficiente")
        case 4:
            cant=int(input(f"¿Cuantas {Alimentos[3]} desea llevar"))
            if cant<=stock[3]:
                stock[3]-=cant
                carrito.append(Alimentos[3])
                productoComprado.append(cant)
                total.append(cant*2500)
            else:
                print("Producto Insuficiente")
def Pagar_Compras():
    pago=int(input(f"Total a pagar: {sum(total)}\nIngrese el Pago: "))
    if pago==sum(total):
        print("Gracias por su compra\nHasta Luego")
        exit()
    elif pago<sum(total):
        print("Saldo Insuficiente\nSu compra se anulara")
        productoComprado.clear()
        carrito.clear()
        total.clear()
    elif pago>sum(total):
        print(f"Gracias por su compra, Su vuelto es: {pago-(sum(total))}\nHasta Luego")
        exit()





opciones()

