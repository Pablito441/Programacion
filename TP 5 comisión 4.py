#      <<< Trabajo práctico Nro 5>>>
import TP_5_Funciones 
"""#Ejercicio 1

word = int(input("Ingrese su número de DNI: "))

rta = TP_5_Funciones.valido(word)
if rta == True:
    print("Número de DNI válido.")
else:
    print("El número de DNi escrito no es válido.")"""

#Ejercicio 2
"""
phrase = str(input("Ingrese una oración: "))
print("La longitud de su última palabra es de ", TP_5_Funciones.last_word(phrase))

"""
#Ejercicio 3
"""3.	Escribir un programa que permita al usuario obtener un identificador para cada 
uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada 
socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse 
más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de 
un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe 
dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer 
nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254

"""
"""print("Para crear su usuario como socio siga las siguientes instrucciones: ")
while True:
    firs_name = str(input("Ingrese uno o dos nombres: \nPara salir del programa no escriba nada: "))
    if firs_name == "":
        break
    last_name = str(input("Ingrese solamente un apellido: "))

    
    while True:
        dni = int(input("Ingrese su número de DNI: "))
        rta = TP_5_Funciones.valido(dni)
        if rta == True: 
            break
        else:
            print("El número de DNi escrito no es válido. Intentelo de nuevo.")


    if firs_name[firs_name.find(" ")]:
        one = firs_name[0:firs_name.find(" ")]
    cant = len(last_name)
    dni = str(dni)
    dni_digit = dni[0:2]
    print(f"Nombre: {firs_name} {last_name}.\nDNI: {dni}\nID -> {one}{cant}{dni_digit}")

print("Gracias por usar este programa.")
"""

#Ejercicio 4
"""number_one = int(input("Ingrese el primer número: "))
number_two = int(input("INgrese el segundo número: "))

TP_5_Funciones.multiple(number_one,number_two,0,0)"""

#Ejercicio 5

"""temperature_max = int(input("Ingrese la temperatura máxima del día: "))
temperature_min = int(input("Ingrese la temperatura minima del día: "))

medium_temperature = TP_5_Funciones.multiple(0,0,temperature_min,temperature_max)
print(f"The average temperature is {medium_temperature} degrees.")"""

#Ejercicio 6
"""
phrase = str(input("Enter a phrase: "))
print(TP_5_Funciones.text_space(phrase))

"""

#Ejercicio 7
"""array = []
while(True): 
    
        num = int(input("Enter a number or enter 0 to exit: "))
        if num == 0:
            break
        else:
            array.append(num)

TP_5_Funciones.minim_maxim_num(array)
"""
#Ejercicio 8 
"""
while(True):    
    radius = float(input("Enter the radius of your circumference: "))
    if radius <= 0:
        print("Error, that's not a circumference, try again.")
    else:
        break

TP_5_Funciones.calculate_area_perimeter(radius)

"""

#Ejercicio 9
"""
attempts = 3
while(True):
    user = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    income = TP_5_Funciones.login(user,password)

    if income == True: 
        print("You have successfully entered the system: ")
        break
    else:
        attempts -= 1
        print(f"The data entered is incorrect, you have {attempts} attempts left")

    if attempts == 0:
        print("Attempts timed out, unable to log in: ")
        break

"""

#Ejercicio 10
"""
shooping_cart = { 
    'product1': 20.0,
    'product2': 30.0,
    'product3': 100.0,
    'product4': 50.0
}

discount = {
    'product3': 50,
    'product2': 30
}

total_price = TP_5_Funciones.apply_discount(shooping_cart,discount)
print(f"the final purchase price is ${total_price}.")

"""
#Ejercicio 11
"""
numbers = [2,3,4,]
squared_results = TP_5_Funciones.apply_def_to_list(numbers)
print(squared_results)

"""

#Ejercicio 12
"""
phrase = str(input("Enter a phrase: "))

result = TP_5_Funciones.r_dictionary(phrase)
print(result)
"""
#Ejercicio 13
"""
vector = (3,4,5)
result_modul = TP_5_Funciones.module_vector_calculate(vector)
print(f"the vector modulus x={vector[0]}, y={vector[1]} y z={vector[2]} is {result_modul}. ")

"""

#Ejercicio 14
"""
number = int(input("Enter a number: "))
boleaan = TP_5_Funciones.boolean_prime(number)
if boleaan == True:
    print("The number is prime.")
else:
    print("The number isn't prime.")
"""
#EJercicio 15
"""
count = 0
while(True):
    number = int(input("Enter a number or 0 for finish: "))
    factorial = TP_5_Funciones.factorial_number(number)
    print(f"The factorial of thr number entered is {factorial}.")
    if number==0:
        break
    count += 1
print(" ")
print(f"a total of {count} numbers were entered.")

"""
#Ejercicio 16
"""
number = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

count = TP_5_Funciones.count_digits(number,digit)
print(f"In the number {number} the digit {digit} to repeated {count} times.")
"""
#Ejercicio 17

maximum = 0
while(True):
    prime = int(input("Enter a prime number or a not number prime for finish: "))
    condition = TP_5_Funciones.boolean_prime(prime)
    if condition == False:
        print("see u, thank u")
        break
    sum_of_digits = TP_5_Funciones.sum_digit(prime)

    digit = int(input("Enter a digit: "))
    count = TP_5_Funciones.count_digits(prime,digit)
    print(f"In the number {prime} the digit {digit} to repeated {count} times.")

    if maximum < prime:
        maximum = prime
maximum_prime = TP_5_Funciones.factorial_number(maximum)
print(f"The largest number entered is {maximum} and its factorial is {maximum_prime}.")

