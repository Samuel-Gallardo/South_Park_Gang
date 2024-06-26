import csv

def obtener_diccionario():
    temperaturaCiudades = {}
    promediosCiudades = {}
    with open('registros_temperaturas.csv', 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            ciudad = fila['Ciudad']
            temperatura = float(fila['Temperatura'])
            if ciudad in temperaturaCiudades.keys():
                temperaturaCiudades[ciudad].append(temperatura)
            else:
                temperaturaCiudades[ciudad] = [temperatura]
        for ciudad, temperaturas in temperaturaCiudades.items():
            promedio = sum(temperaturas) / len(temperaturas)
            promediosCiudades[ciudad] = promedio
        
    print(f"Ciudades: {temperaturaCiudades}\nPromedios: {promediosCiudades}")
    with open('guardar_datos.csv','w') as registro:
        escritor=csv.writer(registro)
        escritor.writerow(temperaturaCiudades)
        escritor.writerow(promediosCiudades)


obtener_diccionario()
