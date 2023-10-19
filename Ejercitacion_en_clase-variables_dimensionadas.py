#Ejercicios en Clase - Variables Dimensionadas 

#Ejercicio 1

"""
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
forma: (nombre, dni, destino). Por ejemplo:
*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+
Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.
"""
#Resolución

"""
print("<<<      Bienvenidos a Aerolineas Pableichon     >>>\n ")

destination_list = []
passengers_list = []
while(True):

    menu = int(input("Eliga una opción:\n[1] Agregar pasajeros\n[2] Agregar ciudades\n[3] Ciudad destino del pasajero\n[4] Pasajeros viajantes a una ciudad\n[5] Pais destino del pasajero\n[6] Pasajeros viajantes a un país\n[0] Salir del programa\n-->  "))
    print("")


    if menu == 1:
        print("<    Agregar pasajero    >")

        name = str(input("Ingrese el nombre del pasajero: "))
        while(True):
            dni = int(input("Ingrese el dni del pasajero: "))
            if len(str(dni)) != 7 and len(str(dni)) != 8:
                print("Error, el dni ingresado es incorrecto, intentelo de nuevo.")
            else:
                break
        destination_1 = str(input("Ingrese el destino del pasajero: "))

        passenger = (name,dni,destination_1)
        passengers_list.append(passenger)
        print(" ")

    elif menu ==2:
        print("<    Agregar ciudades    >")

        ciudad = str(input("Ingresar la ciudad a viajar: "))
        pais = str(input("Ingresar el país a viajar: "))

        destination_2 = (ciudad,pais)
        destination_list.append(destination_2)
        print(" ")

    elif menu ==3:
        print("<    Ciudad destino del pasajero    >")
        yes = 1
        dni = int(input("Ingrese el dni del pasajero: "))
        for tupla in passengers_list:
            if dni in tupla:
                print(f"Se encontro el pasajero,{tupla[0]}, su destino es {tupla[2]}.")
                yes += 1
                break
        if yes== 1:
            print("Este pasajero no se encuentra registrado")
        print(" ")
        
    elif menu ==4:
        print("<    Pasajeros viajantes a una ciudad    >")
        passengers = []
        city = str(input("Ingrese la ciudad destino: "))
        for tupla in passengers_list:
            if city in tupla:
                passengers.append(tupla[0])
        if not passengers:
            print("Ningún pasajero viaja a esa ciudad.")

        for i, element in enumerate(passengers):
            if i < len(passengers) - 1:
                print(element, end=", ")
            else:
                print(element, end=".")
        print(" ")

    elif menu ==5:
        print("<    Pais destino del pasajero    >")
        city = ""
        dni = int(input("Ingrese el dni del pasajero: "))
        print(" ")
        for tupla in passengers_list:
            if dni in tupla:
                city = tupla[2]
                for tupla in destination_list:
                    if city in tupla:
                        print(f"El pasajero viaja a {tupla[1]}")
                        break
                break
        if city == "":
            print("Este pasajero no se encuentra registrado")
        print(" ")

    elif menu ==6:

        print("<    Pasajeros viajantes a un país    >")
        passengers = set() 
        country = str(input("Ingrese el país destino: "))
        print(" ")

        for tupla in destination_list:
            if country in tupla:
                city = tupla[0]
                for tupla in passengers_list:
                    if city in tupla:
                        passengers.add(tupla[0]) 

        if not passengers:
            print("Ningún pasajero viaja a ese país.")
        else:
            print("Pasajeros:", ", ".join(passengers)) 
        print(" ")

    elif menu ==0:
        print("<    Gracias por utilizar el programa.    >")
        break

    else:
        print("Error, ha ingresado un número incorrecto,vuelva a intentarlo.")

"""

#Ejercicio 2
"""
Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual
contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
contenga cada domicilio una sola vez."""
#Respuesta

"""
def invoice_shop(shop):
    addresses = set()  
    for tupla in shop:
        addresses.add(tupla[3])  
    return list(addresses)  

shopping_moth = []
while(True):
    customer = input("Ingrese el nombre del cliente: ")
    while(True):
        day_moth = int(input("Ingrese el día del mes de la compra: "))
        if day_moth <1 or day_moth >31: 
            print("Error, ingresó un número incorrecto, intentelo de nuevo:")
        else:
            break
    while(True):
        amount = float(input("Ingrese el precio de la compra: "))
        if day_moth <0: 
            print("Error, ingresó un número incorrecto, intentelo de nuevo:")
        else:
            break
    address = input("Ingrese su dirección: ")

    sale = (customer,day_moth,amount,address)
    shopping_moth.append(sale)

    exit = int(input("[1]Si no quiere seguir agregando datos de compra."))
    if exit == 1: 
        break
invoice_address = invoice_shop(shopping_moth)
print("Domicilios para facturación:")
for address in invoice_address:
    print(address)

"""
#Ejercicio 3
"""
Crear un programa para gestionar datos de los socios de un club, permitiendo:
- Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar
son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar
con los datos de los socios fundadores ya cargados:
o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
- Informar cantidad de socios del club.
- Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad
ingresaron el 14/03/2018.
- Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
- Imprimir el listado de socios completo.

"""

#Respuesta 
from datetime import datetime

#Funciones
def verificar_fecha(fecha):
    try:
        fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False


#Codigo principal 

dicctionary = {
    1 : {"name": "Amanada Núñez", "income": "17/03/2009", "cuota": True},
    2 : {"name": "Bárbara Molina", "income": "17/03/2009", "cuota": True},
    3 : {"name": "Lautaro Campos", "income": "17/03/2009", "cuota": True}
}
while(True):
    print("<<<      CLUB AMBALA S.A.      >>>")
    menu = int(input("[1]Agregar un Socio.\n[2]Registro de cuotas.\n[3]Modificar fecha de ingreso.\n[4]Dar de baja a un Socio.\n[5]Listado de socios.\n[0]Salir del programa.\n \nEliga una opción -->  "))

    #Salir de programa
    if menu == 0: 
        print("Muchas gracias por usar nuestro gestor de datos, Club Ambala S.A.")
        break

    #Agregar a un socio
    elif menu == 1:
        print("[    Agregar un socio    ]")
        print("Siga los siguientes pasos para obtener una incorporación exitosa:")
        while(True):
            number = int(input("Ingrese el número de socio: "))
            if number in dicctionary.keys():
                print("El número de socio ya existe, ingrese otro.")
            else: 
                print(" ")
                break
        name = input("Ingrese el nombre del nuevo socio.\n-->  ")
        while(True):
            date_addmission = input("Ingrese la fecha de ingreso (dd/mm/aaaa).\n-->  ")
            if verificar_fecha(date_addmission):
                print(" ")
                break
            else:
                print("Se ingresó una fecha incorrecta, intentelo de nuevo.")
        while(True):
            quota_verification = int(input("[1]Si las cuotas del socio están al día.\n[2]Si las cuotas del socio no están al día.\n-->  "))
            if quota_verification not in [1, 2]:
                print("Error, esos números no son válidos, intentelo de nuevo.")
            else:
                print(" ")
                break
        if quota_verification == 1: 
            quota_up_to_day = True
        else: 
            quota_up_to_day = False

        dicctionary[number] = {"name": name, "income":date_addmission, "cuota": quota_up_to_day}

        print("Socio incorporado correctamente")

    #Registro de cuotas
    elif menu == 2:
        print("[    Registro de cuotas    ]")
        while(True):
            socio_nro = int(input("Ingrese el número de socio para verificar si ha pagado las cuotas: "))
            if socio_nro in dicctionary.keys():
                if dicctionary[socio_nro]["cuota"] == True:
                    print("Tiene todas las cuotas pagadas\n ")
                    break
                else:
                    print("No tiene todas las cuotas pagadas\n ")
                    break
            else:
                print("Número de socio no válido.Intentelo de nuevo.")

    #Modificación de fecha de ingreso
    elif menu == 3:
        print("[    Modificación de fecha de ingreso    ]")

        while True:
            verification = 1
            date = input("Ingrese la fecha de ingreso de un/os socios que va a modificar(dd/mm/aaaa).\n-->  ")
            if verificar_fecha(date):
                for key,values in dicctionary.items():
                    if date in values["income"]:
                        verification =2
                        break
                if verification == 2:
                    break
                else:
                    print("La fecha ingresada no corresponde a ningun socio.Intentelo de nuevo.\n ")
                    break
            else:
                print("Se ingresó una valor no válido para una fecha, intentelo de nuevo.\n ")


        date1 = input("Ingrese la nueva fecha de ingreso.\n-->  ")
        for key,values in dicctionary.items():
            if date in values["income"]:
                dicctionary[key]["income"] = date1
                print("La fecha se modificó correctamente.\n ")


    #Dar de baja a un socio
    elif menu == 4:
        print("[    Dar de baja a un socio    ]")

        while True:
            verification = 1
            delete_socio_name = input("Ingrese el nombre del socio que quiere dar de baja.\n-->  ")
            for key,values in dicctionary.items():
                if delete_socio_name in values["name"]:
                    verification = 2
                    break
            if verification == 2: 
                break
            else: 
                print("Error, el nombre ingresado no corresponde a ningún socio, intentelo de nuevo.")
        for key,values in dicctionary.items():
            if delete_socio_name in values["name"]:
                del dicctionary[key]
                print(f"{delete_socio_name} se eliminó correctamente del listado de socios.\n-->  ")
                break
    #Listado de Socios
    elif menu == 5:
        print("[    Listado de socios.   ]")
        print(" ")
        for key,values in dicctionary.items():
            print(f"[   Socio Número: {key} ]")
            print(f"Nombre: {values["name"]}\nFecha de ingreso: {values["income"]}\nCouta al día: {values["cuota"]}")
            print(" ")
            




