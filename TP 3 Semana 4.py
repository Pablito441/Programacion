#      <<< TTRABAJO PRÁCTICO NÚMERO 3 >>>

# Ejercicio 1
"""
palabra = str(input("Escriba una palabra: "))
for i in range(10):
    print(palabra)
"""
#Ejercicio 2
"""
edad = int(input("cuál es su edad?: "))
for i in range(1,edad+1):
    print("Cumpliste ", i, "año/s")
"""
#Ejercicio 3 efasdasd validar que sea entero y positivo
"""
ent_posi = int(input(" Ingrese un número: "))
for i in range(ent_posi):
    if i%2!=0:
        if i == ent_posi - 1:
            print(i) 
        else:
            print(i, end=", ") 
"""
#Ejercicio 4 asdasdasdasd
"""
num = int(input(" Ingrese un número: "))
for i in range(num,0,-1):
    if i == 1:
        print(i, ",0.") 
    else:
        print(i, end=", ")
"""
#Ejercicio 5asdasdasdasdwasda tengo que revisar el ejercicio
"""
inversion = int(input("¿Cuánto va a invertir?: "))
interes = int(input("¿Cuál es el porcentaje del interés anual?: "))
anios = int(input("¿Por cuántos años?: "))
aux = 0
for i in range(1, anios+1):
    print(f"Año {i}.")
    print(f"Capital invertido = {inversion}.")
    print(f"Capital + interés = {inversion+inversion*(interes/100)}.")
    aux = aux + inversion+inversion*(interes/100)
    print(f"Inversion total: {aux}")
"""

# Ejercicio 5  asdasdasdsasdasd tengo que revisar el ejercicio
""" 
cantidad_inversion = int(input("Ingrese la cantidad que desea invertir: "))
interes = int(input("Ingrese el interés anual: "))
tiempo =  int(input("Ingrese la cantidad de años: "))
capital_acumulado = cantidad_inversion
for i in range(1, tiempo+1):
    nuevo_interes = (capital_acumulado*interes)/100
    print("EL INTERES ES:", nuevo_interes)
    capital_acumulado = capital_acumulado + nuevo_interes
    print(f"Año {i}:\nCapital invertido:{cantidad_inversion}\nCapital invertido mas intereses: {capital_acumulado}")
"""
#Ejercicio 6
"""
num = int(input("Ingresar un número: "))
for i in range(num):
    for j in range(i+1):
        if j == i:
            print("*")
        else:
            print("*", end=" ")

"""
# Ejercicio 7
"""
for i in range(10):
    print("Tabla del ", i+1, ".")
    for j in range(10):
        print(f"[{i+1} x {j+1} ={(i+1)*(j+1)}]")
"""
# Ejercicio 8 

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
"""
num = str(input("Ingresar un número: "))

for i in range(len(num)):
    aux = len(num) - i -1
    for j in range(i+1):
        if j == i:
            print(num[aux])
        else:
            print(num[aux], end=(" "))
        aux = aux + 1
"""
#Ejercicio 9 
"""
password = "cotraseña"
passw = ""
while password != passw:
    passw = str(input("Enter the password: "))
    if passw == password: 
        print("you have accessed the system.")
    else:
        print("Incorrect password.")
        """

#Ejercicio 10
"""
num = int(input("Enter a number:  "))
aux = 0
for i in range(1,num):
    if num%i == 0:
        aux += 1

if aux == 2:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")"""

#Ejercicio 11
"""
phrase = str(input("enter a word: "))
for i in range(len(phrase)-1,-1,-1):
    print(phrase[i], end="  ")"""


#Ejercicio 12
"""
phrase = str(input("write a sentence: "))
letter = str(input("write a letter: "))
letter.lower()
phrase.lower()
aux = 0
for i in range(0,len(phrase)-1):
    if letter == phrase[i]:
        aux += 1

print(f"The letter `{letter}` appears {aux} times in the sentence")
"""
#Ejercicio 13
"""
word = ""
while word != "salir":
    word= str(input("enter a word: "))
    print(word)
"""
#Ejercicio 14
"""
num_1 = str(input("Enter the first number: "))
num_2 = str(input("Enter the second number: "))

print(f"for number {num_1}: ")
for i in range(len(num_1)):
    if int(num_1[i])%2==0:
        print(f"{num_1[i]} is even")
    else:
        print(f"{num_1[i]} is odd")

print(f"for number {num_2}: ")
for i in range(len(num_2)):
    if int(num_2[i])%2==0:
        print(f"{num_2[i]} is even")
    else:
        print(f"{num_2[i]} is odd")
        """

#Ejercicio 15
"""
num = int(input("enter a number: "))
if num>0:
    for i in range(1,num+1):
        if num%i == 0:
            print(i, end=", ")

else:
    print("Error. that number is invalid")

print("are numbers divisors of ", num,".")
"""
#Ejercicio 16
"""
amount_num=int(input("how many numbers are you going to enter?: "))

counter=0

if amount_num<0:
    print("¡ERROR! enter a valid amount")
else:
    for i in range(amount_num):
        num=float(input("Enter a number: "))
        if num<0:
            counter=counter+1
print(f"{counter} negative numbers entered")
"""
#Ejercicio 17
"""
vowels_1 = "aeiou"
phrase = str(input("Enter a phase: "))
phrase = phrase.lower()
vowels = ""

for caracter in phrase:
    if caracter in vowels_1 and caracter not in vowels:
        vowels += caracter

print(f"The vowels in the phrase are: {vowels}")
"""
#Ejercicio 18
"""
fibo=[0,1]

for i in range(2,10):
    next_num=fibo[i-1]+fibo[i-2]
    fibo.append(next_num)

for num in fibo:
    print(num, end = " ")
"""
#Ejercicio 19
"""
amount = float(input("Enter the amount you want to save: $"))

if amount<0:
    print("MISTAKE! Enter a valid amount.")
else:
    saving = 0

    while saving<amount:
        new_saving = float(input("Enter the amount you want to enter: $"))

        if new_saving < 0:
            print("MISTAKE! Enter a valid amount.")
        else:
            saving += new_saving
            remaining = amount - saving
            print(f"You have saved ${saving}, you have ${remaining} to reach your goal of ${amount}.")
    
    if saving == amount:
        print(f"You have reached your goal of saving ${amount}.")
    else:
        additional = saving - amount
        print(f"You have reached your goal of saving ${amount} and have earned an additional {additional}.")
"""
#Ejercicio 20
"""
num = 1
addition = 0
while num != 0:
    num = int(input("Enter a positive integer: "))
    if num<0:
        print("¡MISTAKE! Please enter only positive integers.")
    else:
        addition += num
print(f"The sum of all valid numbers entered is {addition}")
"""
#Ejercicio 21
"""
num = 1
highest = 0

while num != 0:
    num = int(input("Enter a positive integer:"))
    if num<0:
        print("¡MISTAKE! Please enter only positive integers.")
    else:
        if num > highest:
            highest = num
print(f"The highest number entered was {highest}")
"""

#Ejercicio 22
"""
num = 0
even = 0

while num != -1:
    num=int(input("Enter a positive integer (or -1 to exit): "))

    if num == -1:
        break
    elif num<0:
        print("MISTAKE! Please enter a valid (positive) number")
    else:
        num_str=str(num)
        addition = 0

        for digit_str in num_str:
            digit = int(digit_str)
            addition += digit
        
        print(f"The sum of the digits of {num} is {addition}")

        if num%2 == 0:
            even += 1

print(f"Total even numbers entered: {even }")
"""
#Ejercicio 23 y 24
"""
product = 1
total = 0

while product != 0:
    product = float(input("Enter producer value: "))
    if product < 0:
        print("MISTAKE! Enter only valid amounts")
    else:
        total += product

if total > 1000:
    discount = total * 0.1
    final_price = total - discount
    print(f"Your purchase total is ${total}")
    print(f"A 10% discount was applied to it, so the final price is {final_price}")
else:
    print(f"Your purchase total is ${total}")
"""
#Ejercicio 25

num = int(input("Enter a positive integer: "))

if num < 0:
    print("MISTAKE! The number must be positive")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1

    for i in range(1, num+1):
        factorial *= i
    
    print(f"The factorial of {num} is {factorial}")


