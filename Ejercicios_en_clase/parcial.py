"""
Realizar un programa que cumpla con las siguientes condiciones:

Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
Generar un menú de opciones, que serán:
Juego de números.
Juego de palabras.
Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
El mayor número par.
El promedio de los números impares.
Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
No olvides realizar las debidas validaciones!

"""
#Pedí al usuario que ingrese su nombre
name = str(input("Ingrese su nombre: "))

#Verificación para que el usuario solo pueda ingresar número 1 o 2, sino le salta error
while True:
    menu = int(input(f"{name}, Eliga una opción\nJuego de números[1]\nJuego de palabras[2]\n >>> "))

    if menu < 1 or menu > 2:
        print("Error, el numero ingresado es incorrecto, intentelo de nuevo.")
    else: 
        break

#Inicialización de todas las variables a usar
counter = 0
odd_numbers = 0
number = 1
greatest_even = 0
vowels_a = 0
vowels_e = 0
vowels_i = 0
vowels_o = 0
vowels_u = 0
#Con un condicional separo los dos opciones del juego, en la opción 1 es el juego de números pares
if menu == 1: 
    print("<<<Juego de Números>>>")
#Con un bucle while pido ingresar la cantidad de número que el quiera, o el número 0 para salir y dejar de ingresar números
    while number != 0:
        number = int(input(f"{name}, ingrese un número o número '0' para salir\n>>> "))
#Considere que los números negativos tambien pueden ser pares e impares entonces por eso no hice la validación para los números negativos.

#Con una condicional separo cada sentencia, para los número pares e impares
        if greatest_even < number and number %2==0:
            greatest_even = number
        elif number % 2 != 0: 
            odd_numbers += number
            counter += 1
#Con una condicional si no se ingresaron números pares o impares pongo un mensaje de respuesta sino sigo con el código normal
    if greatest_even == 0:
        print(f"{name}, no se ingresaron número pares.")
    else:
        print(f"{name}, el mayor número par de todos los números ingresados es {greatest_even}.")

    if odd_numbers == 0: 
        print(f"{name}, no se ingresaron números impares.")
    else:
        average = float(odd_numbers/counter)
        print(f"{name}, el promedio de los números impares es {average}")

#es la parte dos del programa, cuando eliga la opcion 2
elif menu == 2:
#pido la frase al usuario
    print("<<<Juego de Palabras>>>")
    phrase = str(input(f"{name}, escriba una frase: "))
#un bucle por para recorrer la frase ingresada y sumar las vocales en cada variable
    for letter in phrase:
            if letter == 'a':
                vowels_a += 1
            elif letter == 'e':
                vowels_e += 1
            elif letter == 'i':
                vowels_i += 1
            elif letter == 'o':
                vowels_o += 1
            elif letter == 'u':
                vowels_u += 1
    
    print(f"{name}, de la frase ingresada ingresaste esta cantidad de vocales:\na = {vowels_a} \ne = {vowels_e}\ni = {vowels_i}\no = {vowels_o}\nu = {vowels_u}")









