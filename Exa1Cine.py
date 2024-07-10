import os
# Lista para almacenar asientos comprados
lugarescomprados = []
# Matriz que representa los asientos disponibles en el concierto
lugaresconcierto = [
    [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]
# Diccionario para almacenar las entradas vendidas y el dinero recaudado por cada tipo de entrada
recaudacionconcierto = {
    "PLATINUM": [0, 0],
    "GOLD": [0, 0],
    "SILVER": [0, 0]   
}
# Función para actualizar la recaudación del concierto
def actualizarrecaudacionconcierto(tipoentrada, costoentrada):
    # Incrementa el contador de las entradas vendidas 
    recaudacionconcierto[tipoentrada][0] += 1
    # Suma el costo de la entrada al total
    recaudacionconcierto[tipoentrada][1] += costoentrada 
# Opción 1: Comprar entrada
def comprar_entrada():
    try:
            #solicitar tipo de entrada
            print("-------------------------------------------------")
            print("|      Bienvenido a la compra de entradas       |")
            print("-------------------------------------------------")
            print("|Los precios de las entradas son los siguientes:|")
            print("|1.- PLATINUM, $120.000. (Asientos del 1 al 20).|")
            print("|2.- GOLD, $80.000. (Asientos del 21 al 50).    |")
            print("|3.- SILVER, $50.000. (Asientos del 51 al 100). |")
            print("-------------------------------------------------")
            tipodeentrada =int(input("Ingrese el tipo de entrada que desea (1-3) :"))
            if tipodeentrada < 1 or tipodeentrada > 2: 
                print("El tipo de entrada ingresado no es válido")
                return
            else:
                if tipodeentrada == 1:
                    precio = 120000
                    rangoasiento = (1,20) 
                    tipoentrada = "PLATINUM"
                elif tipodeentrada == 2:
                    precio = 80000
                    rangoasiento = (21,50) 
                    tipoentrada = "GOLD"
                elif tipodeentrada == 3:
                    precio = 80000
                    rangoasiento = (51,100) 
                    tipoentrada = "SILVER"
                else:
                    print("El tipo de entrada no es válido")
                    return
            # Solicita la cantidad de entradas que desea comprar
            cantidadentradas = int(input("Ingrese la cantidad de entradas que desea comprar (1-3) : "))
            if cantidadentradas < 0 or cantidadentradas > 3:
                print("La cantidad debe ser mayor que 0 y menor o igual a 3")
                return
            # Solicita el asiento que desea comprar
            for i in range(cantidadentradas):
                print("-----------------------------------------")
                print("|              ESCENARIO                |")
                print("-----------------------------------------")
                print(mostrar_ubicaciones_disponibles())
                print(f"Tipo de entrada seleccionada : {tipoentrada}")
                print("Ejemplo PLATUNUM (1-20),GOLD (21-50),SIlVER (51-100).")
                print("El asiento debe estar dentro de el rango de asientos del tipo de entrada ")
                while True:
                    try:
                        asiento = int(input(f"Ingrese el asiento { i + 1 }que desea comprar : "))
                        if asiento < rangoasiento[0] or asiento > rangoasiento[1]:#rango ejemplo 1-20 ,21-50,51-100segun el tipo de entrada
                            print("El asiento no es válido  esta debe estar dentro del rango del tipo de entrada")
                        else:
                            break
                    except:
                        print("El asiento no es válido")
                #registrar cliente 
                print("-------------------------------------------------")
                print("|          Registro de cliente                  |")
                print("-------------------------------------------------")
                print("Ingrese RUT del cliente")
                rut = input("Ingrese RUT del comprador sin puntos ni guion :")
                if "." in rut or "-" in rut or len(rut) != 8:
                    print("El RUT no es válido")
                    return
                else:

                    #registro usuario
                    registro = {
                                "RUT": rut,
                                "Tipo de entrada": tipoentrada,
                                "Asiento": asiento,
                                "Cantidad de entradas": cantidadentradas,
                                }
                    #Marcar asiento vendido con X
                    for fila in lugaresconcierto:
                        if asiento in fila:
                            fila[fila.index(asiento)] = "X"
                            break
                    #Actualizar Recaudacion
                    actualizarrecaudacionconcierto(tipoentrada,precio)
                    #Almacenar asiento comprado
                    lugarescomprados.append(registro)
                    print("Registro y Compra exitosa")
                    print("-------------------------------------------------")
                    print(f"RUT: {registro['RUT']}, Tipo de entrada: {registro['Tipo de entrada']}, Asiento: {registro['Asiento']}, Cantidad de entradas: {registro['Cantidad de entradas']}\n")
    except ValueError:
        print("El valor ingresado no es válido")
# Opción 2: Mostrar ubicaciones disponibles
def mostrar_ubicaciones_disponibles():
   for filalugares in lugaresconcierto:
        print(filalugares)
# Opción 3: Ver listado de asistentes ordenados por RUN de menor a mayor
def ver_listado_asistentes():
    #rut ordenado
    lugarescomprados.sort(key=lambda x: x['RUT'])
    with open("planilla_listar.csv", "w") as plantilla:
        for registro in lugarescomprados:
            plantilla.write(f"RUT: {registro['RUT']}, Tipo de entrada: {registro['Tipo de entrada']}, Asiento: {registro['Asiento']}, Cantidad de entradas: {registro['Cantidad de entradas']}\n")
    print("Archivo 'planilla_listar.csv' creado con exito.")
    with open("planilla_listar.json", "w") as plantilla:
        for registro in lugarescomprados:
            plantilla.write(f"RUT: {registro['RUT']}, Tipo de entrada: {registro['Tipo de entrada']}, Asiento: {registro['Asiento']}, Cantidad de entradas: {registro['Cantidad de entradas']}\n")
    print("Archivo 'planilla_listar.csv' creado con exito.")
# Opción 4: Mostrar ganancias totales
def mostrar_ganancias_totales():
    print("\nGANANCIAS ENTRADAS PLATINUM ")
    print(f"Total de entradas platinum vendidas: {recaudacionconcierto['PLATINUM'][0]}")
    print(f"Total de dinero recaudado: ${recaudacionconcierto['PLATINUM'][1]:,}")
    print(" GANANCIAS ENTRADAS GOLD ")
    print(f"Total de entradas gold vendidas: {recaudacionconcierto['GOLD'][0]}")
    print(f"Total de dinero recaudado: ${recaudacionconcierto['GOLD'][1]:,}")
    print(f"GANANCIAS ENTRADAS SILVER")
    print(f"Total de entradas silver vendidas: {recaudacionconcierto['SILVER'][0]}")
    print(f"Total de dinero recaudado: ${recaudacionconcierto['SILVER'][1]:,}\n")
    print("ESTADÍSTICAS GENERALES")
    print(f"Total de entradas del concierto vendidas: {recaudacionconcierto['PLATINUM'][0] + recaudacionconcierto['GOLD'][0] + recaudacionconcierto['SILVER'][0]}")
    print(f"Total de dinero recaudado con el concierto: ${recaudacionconcierto['PLATINUM'][1] + recaudacionconcierto['GOLD'][1] + recaudacionconcierto['SILVER'][1]:,}\n")
# Opción 5: Salir del programa
def salir():
    print("Saliendo del programa")
    print("Maria Martinez")
    print(f"Fecha: (dd/mm/aa)")
# Menú principal
def menu():
    try:
        while True:
            print("---------------------------------------")
            print("|            Creativos.cl             |")
            print("----------------MENU-------------------")
            print("|1.-Comprar entradas.                 |")
            print("|2.-Mostrar ubicaciones disponibles.  |")
            print("|3.-Ver listado de asistentes.        |")
            print("|4.-Mostrar ganancias totales.        |")
            print("|5-.Salir.                            |")
            print("---------------------------------------")
            opcion = int(input("Ingrese opcion (1-5) : "))
            if opcion == 1:
                comprar_entrada()
            elif opcion == 2:
                mostrar_ubicaciones_disponibles()
            elif opcion == 3:
                ver_listado_asistentes()
            elif opcion == 4:
                mostrar_ganancias_totales()
            elif opcion == 5:
                salir()
                break
            else:
                print("Opcion incorrecta")
    except ValueError:
           print("Error.")
           print("Error.")
