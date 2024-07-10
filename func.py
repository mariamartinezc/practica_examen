import os
comprados = []
matriz = [
    ["A","B","C","D"],
    [ 1, 1, 1, 1 ],
    [ 2, 2, 2, 2 ],
    [ 3, 3, 3, 3 ],
    [ 4, 4, 4, 4 ],
    [ 5, 5, 5, 5 ],
    [ 6, 6, 6, 6 ],
    [ 7, 7, 7, 7 ],
    [ 8, 8, 8, 8 ],
    [ 9, 9, 9, 9 ],
    [ 10, 10, 10, 10 ],
]

recaudaciondepartamento = {
    "A": [0, 0],
    "B": [0, 0],
    "C": [0, 0],
    "D": [0, 0]
}

def actualizarrecaudaciondepartamento(tipo, precio):
    recaudaciondepartamento[tipo][0] += 1
    recaudaciondepartamento[tipo][1] += precio

def comprar_departamento(matriz):
    try:
        print("-------------------------------------------------")
        print("|   Bienvenido a la compra de departamentos     |")
        print("-------------------------------------------------")
        print("|  Tipo.          Piso.          Precio:        |")
        print("|1.-A          Piso (1-10)       $3.800.        |")
        print("|2.-B          Piso (1-10)       $3.000         |")
        print("|3.-C          Piso (1-10)       $2.800         |")
        print("|4.-D          Piso (1-10)       $3.500         |")
        print("-------------------------------------------------")
        tipo = int(input("Ingrese el tipo de departamento que desea (1-4) : "))
        if tipo < 1 or tipo > 4 :
            print("El tipo de departamento ingresado no es valido")
            return
        else:
            if tipo == 1:
                precio = 3.800
                rangopiso = (1,10) 
                tipo = "A"
            elif tipo == 2:
                precio = 3.000
                rangopiso = (1,10) 
                tipo = "B"
            elif tipo == 3:
                precio = 2.800
                rangopiso = (1,10) 
                tipo = "C"
            elif tipo == 4:
                precio = 3.500
                rangopiso = (1,10) 
                tipo = "D"
            else:
                print("Error, ingrese un tipo valido")
                return
            print("-----------------------------------------")
            print("|              EDIFICIOS                |")
            print("-----------------------------------------")
            mostrar_departamentos_disponibles()
            print(f"Tipo de departamento seleccionada : {tipo}")
            print("Ejemplo A :(1-10), B :(1-10), C :(1-10), D :(1-10).")
            print("El departamento debe estar dentro de el rango del tipo")
            while True:
                try:
                    piso = int(input("Ingrese el piso que desea (1-10) : "))
                    if piso < rangopiso[0] or piso > rangopiso[1]:
                        print("Error, ingrese un piso valido")
                    else:
                        for fila in matriz:
                            if piso in fila:
                                if fila[fila.index(piso)] == "X":
                                    print("Error, el piso ya está vendido")
                                    continue
                                else:
                                    break
                        else:
                            print("Error, el piso no existe")
                            continue
                        break
                except ValueError:
                    print("Error.")
            print("-------------------------------------------------")
            print("|          Registro de cliente                  |")
            print("-------------------------------------------------")
            print("Ingrese RUT del cliente")
            rut = input("Ingrese RUT del comprador sin puntos ni guion :")
            if "." in rut or "-" in rut:
                print("El RUT no es válido")
                return
            else:
                registro = {
                    "RUT": rut,
                    "Tipo": tipo,
                    "Piso": piso,
                    "Precio": precio
                }
                for fila in matriz:
                    if piso in fila:
                        fila[fila.index(piso)] = "X"
                        break
                actualizarrecaudaciondepartamento(tipo, precio)
                comprados.append(registro)
                print("Registro y Compra exitosa")
                print("-------------------------------------------------")
                print(f"RUT: {registro['RUT']}, Tipo: {registro['Tipo']}, Piso: {registro['Piso']}, Precio: {registro['Precio']}\n")
                return matriz
    except ValueError:
        print("El valor ingresado no es valido")
        #opcion2
def  mostrar_departamentos_disponibles():
   for filalugares in departamentos:
        print(filalugares) 
#opcion3
def ver_listado_compradores(): 
      #rut ordenado
    comprados.sort(key=lambda x: x['RUT'])
    with open("planilla_listar.csv", "w") as plantilla:
        for registro in comprados:
            plantilla.write(f"RUT: {registro['RUT']}, Tipo: {registro['Tipo']}, Piso: {registro['Piso']}, Precio: {registro['Precio']}\n")
    print("Archivo 'planilla_listar.csv' creado con exito.")          
#Mostrar ganancias totales
def mostrar_ganancias_totales():
    print("\nGANANCIAS DEPARTAMENTOS A ")
    print(f"Total de Total de departamentos A vendidas: {recaudaciondepartamento['A'][0]}")
    print(f"Total de dinero recaudado: ${recaudaciondepartamento['A'][1]:,}")
    print(" GANANCIAS DEPARTAMENTOS B  ")
    print(f"Total de Total de departamentos B vendidas: {recaudaciondepartamento['B'][0]}")
    print(f"Total de dinero recaudado: ${recaudaciondepartamento['B'][1]:,}")
    print(f"GANANCIAS DEPARTAMENTOS C ")
    print(f"Total de Total de departamentos C vendidas: {recaudaciondepartamento['C'][0]}")
    print(f"Total de dinero recaudado: ${recaudaciondepartamento['C'][1]:,}\n")
    print(f"GANANCIAS DEPARTAMENTOS D ")
    print(f"Total de departamentos D vendidas: {recaudaciondepartamento['D'][0]}")
    print(f"Total de dinero recaudado: ${recaudaciondepartamento['D'][1]:,}\n")
    print("ESTADÍSTICAS GENERALES")
    print(f"Total de entradas del concierto vendidas: {recaudaciondepartamento['A'][0] + recaudaciondepartamento['B'][0] + recaudaciondepartamento['C'][0] + recaudaciondepartamento['D'][0]}")
    print(f"Total de dinero recaudado con el concierto: ${recaudaciondepartamento['A'][1] + recaudaciondepartamento['B'][1] + recaudaciondepartamento['C'][1] + + recaudaciondepartamento['D'][1]:,}\n")
#funcion salir
def salir():
    print("Diseñador codigo")
    print("Maria Martinez")
    print("RUT: 19.003.574-3")
    print("Fecha: dd/mm/aa")
    print("Saliendo del programa")
#bucle menu
def menu():
    try:
        while True:
            print("----------------------------------------")
            print("|            Casa Feliz                |")
            print("----------------MENU--------------------")
            print("|1.-Comprar departamento.              |")
            print("|2.-Mostrar departamentos disponibles.|")
            print("|3.-Ver listado de compradores.        |")
            print("|4.-Mostrar ganancias totales.         |")
            print("|5-.Salir.                             |")
            print("----------------------------------------")
            opcion = int(input("Ingrese opcion del menu (1-5) : "))
            if opcion == 1:
                comprar_departamento()
            elif opcion == 2:
                mostrar_departamentos_disponibles()
            elif opcion == 3:
                ver_listado_compradores()
            elif opcion == 4:
                mostrar_ganancias_totales()
            elif opcion == 5:
                salir()
                break
            else:
                print("Opcion incorrecta")
    except ValueError:
           print("Error.")