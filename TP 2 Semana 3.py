#                  >>>Trabajo Práctico Número 2<<<

#Ejercicio 1
"""
anios_compu = int(input("¿Cuántos años tiene su computadora?: "))
if(anios_compu < 3 ):
    print("Su computadora es nueva")
else:
    print("Su computadora es vieja")
"""

#Ejercicio 2
"""
anios_compu = int(input("¿Cuántos años tiene su computadora?: "))
if(anios_compu>0):
    if(anios_compu < 3 ):
        print("Su computadora es nueva")
    else:
        print("Su computadora es vieja")
else:
    print("Error, ingresó un número negativo")
"""
#Ejercicio 3
"""
nom_1 = input("Ingrese el nombre de la primera persona: ")
nom_1 = nom_1.lower()
nom_2 = input("Ingrese el nombre de la segunda persona: ")
nom_2 = nom_2.lower()

if(nom_1[0:1] == nom_2[0:1]):
    print("Coincidencia.")
else:
    print("No hay coincidencia.")
"""
#Ejercicio 4
"""
cand_a = "rojo"
cand_b = "verde"
cand_c = "azul"
voto = str(input("Eliga el candidato a votar. Ingrese [A], [B] o [C]: "))
voto = voto.lower()
if(voto == "a" or voto == "b" or voto == "c"):
    if(voto == "a"):
        print("Usted ha votado por el partido ",cand_a)
    if(voto == "b"):
        print(f"Usted ha votado por el partido {cand_b}")
    if(voto == "c"):
        print(f"Usted ha votado por el partido {cand_c}")
else:
    print("Opción errónea.")
"""

#Ejercicio 5
"""
letra = str(input("Ingrese una vocal: "))
letra = letra.lower()
if (len(letra)>1):
    print("No se puede procesar el dato.")
else:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("Es una voval.")
    else:
        print("No es una vocal.")
"""

#Ejercicio 6
"""
anio = int(input("Ingrese un año para saber si es bisiesto: "))
if(anio%4 == 0):
    print("Es un año bisiesto.")
else:
    print("No es un año bisiesto.")
"""

#Ejercicio 7
"""
num_1=int(input("Ingrese el primer número: "))
num_2=int(input("Ingrese el segundo número: "))
num_3=int(input("Ingrese el tercer número: "))
if(num_1 == num_2 and num_1 == num_3):
    print("Todos los números son iguales.")
else:
    if(num_1 > num_2):
        if(num_1 > num_3):
            print(f"El primer número ({num_1}) es mayor.")
        else:
            print(f"El tercer número ({num_3}) es mayor.")
    else:
        if(num_2 > num_3):
            print(f"El segundo número ({num_2}) es mayor.")
        else:
            print(f"El tercer número ({num_3}) es mayor.")
"""
#Ejercicio 8 
"""
usuario = str(input("Ingrese el nombre de usuario: "))
password = str(input("Ingrese la contraseña: "))

if(usuario == "Gwenevere" and password == "excalibur"):
    print("Usuario y contraseña correctos.")
    print("Ha ingresado corractamente.")
else:
    print("Acceso denegado.")
"""
#Ejercicio 9
"""
sex = str(input("Ingrese su sexo: "))
sex = sex.lower()
if(sex == "mujer" or sex == "hombre"):
    nom = str(input("Ingrese su nombre para saber su grupo correspondiente: "))
    nom = nom.lower()
    if(sex == "mujer"):
        if(nom[0:1] == "a" or nom[0:1] == "b" or nom[0:1] == "c" or nom[0:1] == "d" or nom[0:1] == "e" or 
        nom[0:1] == "f" or nom[0:1] == "g" or nom[0:1] == "h" or nom[0:1] == "i" or nom[0:1] == "j" or 
        nom[0:1] == "k" or nom[0:1] == "l" or nom[0:1] == "m"):
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
    if(sex == "hombre"):
        if(nom[0:1] == "n" or nom[0:1] == "ñ" or nom[0:1] == "o" or nom[0:1] == "p" or nom[0:1] == "q" or 
        nom[0:1] == "r" or nom[0:1] == "s" or nom[0:1] == "t" or nom[0:1] == "u" or nom[0:1] == "v" or 
        nom[0:1] == "w" or nom[0:1] == "x" or nom[0:1] == "y" or nom[0:1] == "z"):
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
else: 
    print("Error, lo ingresado no es un sexo.")
    """
#Ejercicio 10
"""
edad = int(input("Ingrese su edad: "))

if(edad<5):
    print("Entrada gratuita.")
if(edad>4 and edad<18):
    print("La entrada tiene el precio de $500.")
if(edad>18):
    print("La entrada tiene el precio de $1000.")
if(edad<0):
    print("No existe tal valor.")
    """

# Ejercicio 11 asdasdwdasdwasdwa
"""
aux = str(input("¿Desea una pizza vegetariana?: [si] o [no]: "))
aux = aux.lower()
if(aux == "si" or aux == "no"):
    if(aux == "si"):
        ingrediente= int(input("Ingredientes para agregar: Pimiento[1] , Tofu[2], Pimiento y Tofu[3]: "))
        if(ingrediente == 1):
            print("Pizza vegetariana muzzarella con tomate y pimiento.")
        if(ingrediente == 2):
            print("Pizza vegetariana muzzarella con tomate y tofu.")
        if(ingrediente == 3):
            print("Pizza vegetariana muzzarella con tomate, pimiento y tofu.")
    if(aux == "no"):
        ingrediente= int(input("Ingredientes para agregar: Peperoni[1] , Jamón[2] o Salmón[3]: "))
        if(ingrediente == 1):
            print("Pizza vegetariana muzzarella con tomate y peperoni.")
        if(ingrediente == 2):
            print("Pizza vegetariana muzzarella con tomate y jamón.")
        if(ingrediente == 3):
            print("Pizza vegetariana muzzarella con tomate y salmón.")
else:
    print("Error, valor incorrecto.")
    """

#Ejercicio 12
"""
anio_actual = int(input("Ingrese el año actual: "))
anio_random = int(input("Ingrese un año cualquiera: "))
if(anio_random==anio_actual):
    print("Son los mismo años.")
else:
    if(anio_random>anio_actual):
        print(f"Nos faltan {anio_random-anio_actual} años para llegar al año {anio_random}.")
    else:
        print(f"Pasaron {anio_actual-anio_random} años desde el año {anio_random}.")
        """

#Ejercicio 13 asdasdwdasdwasdwa
"""
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

if(num_1>num_2):
    if(num_1%num_2==0):
        print(f"{num_1} es múltiplo del {num_2}.")
    else:
        print(f"{num_1} no es múltiplo del {num_2}.")
else:
    if(num_2%num_1==0):
        print(f"{num_2} es múltiplo del {num_1}.")
    else:
        print(f"{num_2} no es múltiplo del {num_1}.")

"""
#Ejercicio 14 asdasdasdasdasdasd
"""print("En una ecuación de primer grado: ")
a = float(input("Ingrese el coeficiente a: "))
b= float(input("Ingrese el coeficiente b: "))
if(a==0 or b==0):
    print("La ecuación no tiene solución: ")
else:
    ecuacion = (a * (-b/a)) + b
    print("El resultado de la ecuacion es ", ecuacion, ".")
"""
# Ejercicio 15
"""
aux = str(input("Si desea calcular el área de un triángulo [T] o si quiere calcular el área de un círculo [O]: "))
aux = aux.lower()
if(aux=="t"):
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    print(f"El área del triangulo es {(base*altura)/2}.")
if(aux=="o"):
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"El área del círculo es de {3.14159*(radio**2)}.")"""

# Ejercicio 16 
"""
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
aux = str(input("Seleccione la operación: Suma[S], Resta[R], Multipliación[M], División[D]: "))
aux = aux.lower()
if(aux == "s"):
    print(f"{num_1} + {num_2} = {num_1+num_2}")
if(aux == "r"):
    print(f"{num_1} - {num_2} = {num_1-num_2}")
if(aux == "m"):
    print(f"{num_1} x {num_2} = {num_1*num_2}")
if(aux == "d"):
    print(f"{num_1} / {num_2} = {num_1/num_2}")
"""
#Ejercicio 17
"""
day_week = str(input("Ingrese un día de la semana: "))
day_week = day_week.lower()
if day_week == "lunes" or day_week == "martes" or day_week == "miercoles" or day_week == "jueves" or day_week == "viernes" or day_week == "sabado" or day_week == "domingo":
    if day_week == "lunes":
        print("Odio los lunes.")
    else:
        if day_week == "viernes":
            print("Por fin loco, puedo descansar un poco, vamos que es viernes!!")
        else:
            if day_week == "sabado" or day_week == "domingo":
                print("La vida está para disfrutar y vivir.")
            else:
                print("Un día como cualquiera.")
else:
    print("Ingreso un día inexistente.")
"""
#Ejercicio 18
"""
all_hrs = int(input("what is the total hours worked in the month?: "))
hourly_wage = int(input("what is your hourly wage?: "))

if all_hrs>48:
    print(f"you worked {all_hrs-48} hours overtime.")
    extra_hours = all_hrs-48


print(f"your total salary is ${(48*hourly_wage)+(extra_hours*((hourly_wage*0.10) + hourly_wage ))}.")
"""
#Ejercicio 19
"""
pencil = int(input("how many pencils do you want to buy?: "))
if pencil>1000:
    print(f"has a discount of 7% of the total.")
    print(f"you have to pay {pencil*60-(pencil*60*0.07)}.")
else: 
    print(f"you have to pay {pencil*60}.")
"""
#exercise 20

note_1 = int(input(" first note: "))
note_2 = int(input(" second note: "))
note_3 = int(input(" third note: "))
note_4 = int(input(" quarter note: "))

average = (note_1+note_2+note_3+note_4)/4

if average>= 6:
    print("you passed.")
else: 
    print("you failed.")

