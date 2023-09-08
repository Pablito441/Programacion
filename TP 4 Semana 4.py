"""
Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
"""

# Respuesta
"""
x = 0
while x < 30:
    if x == 15:
        print(f"The execution of the loop was broken when x was {x}.")
        x += 1
        break
    elif x in [4,6,10] :
        print(f"The value {x} of x was skipped.")
        x += 1
        continue
    else:
        print('The value of the loop is: ', x)
    x += 1
"""
#Ejercicio 1
"""
lines = []

print("Enter lines of text. Press Enter blank to finish.")
while True:
    line = input()
    line = line.upper()
    if line == "":
        break 
    lines.append(line)

print("Lines in capital letters:")
for line in lines:
    print(line)
"""
#Ejercicio 2
"""
bank_account = 0
bita = 0
while bita != 350:

    bitacora = str(input("Type D or R [D for deposit and R for withdrawal} plus the amount you want to deposit or withdraw: "))
    bitacora = bitacora.lower()
    bita = int(bitacora[bitacora.find(" ") + 1: len(bitacora)])

    if bita < 0:
        print("ERROR! the number has to be positive.")
    else:
        if bitacora[0] == "d":
            bank_account += bita
            print(f"Has a current balance ${bank_account}.")
        elif bitacora[0] == "r":
            bank_account -= bita
            print(f"Has a current balance ${bank_account}.")
"""
#Ejercicio 3
"""
num = 1
prime = 0
while num != 0:

    num = int(input("Enter a number higher than 1: "))
    if num == 0:
        continue
    elif num < 2:
        print("ERROR! the number has to be higher than 1.")
    else: 
        aux = 0
        for i in range(1,num+1):
            if num %i == 0:
                aux += 1

    if aux == 2:
        prime += num

print(f"the sum of the prime numbers is equal to {prime}.")
"""

#Ejercicio 4
"""
year_1 = int(input("Enter the first year: "))
year_2 = int(input("Enter the second year: "))
for i in range(year_1, year_2+1):
    if (i% 4 == 0 and i% 100 != 0) or (i% 400 == 0):
        print(i)
"""
#Ejercicio 5
"""
for i in range(1,21):
    if i% 2 != 0:
        continue
    print(i)
"""
#Ejercicio 6
"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 60

for num in numbers:
    if num == target :
        print(f"number {target} found!")
        break
else:
    print(f"The number {target} isn't on the list.")

"""
#Ejercicio 7

"""
import random
while True:  

    x = int(input("Menu:\n[1]Mysterious message.\n[2]Random number.\n[3]Recommendation.\n[0]Go out.\n"))
    if x == 0:
        break
    elif x == 1:
        print("fighting!!")
    elif x == 2:
        num_random = random.randint(1, 100)
        print(f"Your number random is {num_random}.")
    elif x == 3: 
        print("Enter the number 0")

"""