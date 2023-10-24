#                   <<<TRABAJO PRÁCTICO NÚMERO 6>>>

#Ejercicio 1 , 2, 3, 4 y 5
"""
list_of_numbers = []
new_list = []
addition = 0
while True:
    number = int(input("Enter a number or enter 0 for finish.\n-->  "))
    if number == 0: 
        break
    else:
        list_of_numbers.append(number)
#2
number_to_delete = int(input(" \nEnter a number to delete.\n-->  "))
if number_to_delete in list_of_numbers:
    list_of_numbers.remove(number_to_delete)
    print("The number was deleted successfully.\n ")
else:
    print("the number isn't found in the created list.\n ")
#3
for n in list_of_numbers:
    addition += n
print(f"the sum of all the numbers in the list is {addition}.\n ")
#4
number_max = int(input("Enter a number for create a new list."))
for n in list_of_numbers:
    if n<number_max:
        new_list.append(n)
for n in new_list:
    if n == new_list[len(new_list)-1]:
        print(n, end=". ")
    else:
        print(n, end=", ")
print(" ")
# 5
list_of_tuple = []

for n in list_of_numbers:
    count = list_of_numbers.count(n)
    tupla = (n,count)
    if tupla not in list_of_tuple:
        list_of_tuple.append(tupla)

for n in list_of_tuple:
    if n == list_of_tuple[len(list_of_tuple)-1]:
        print(n, end=". ")
    else:
        print(n, end=", ")

"""
#Ejercicio 6
"""
primary_level = []
secundary_level = []
while True:
    name = input("Enter the name of the primary students or 'x' for finish.\n-->  ")
    if name == "x":
        break
    else: 
        if name not in primary_level:
            primary_level.append(name)
        else: 
            print("that name was entered previously.")
        
while True:
    name = input("Enter the name of the high school students or 'x' for finish.\n-->  ")
    if name == "x":
        break
    else: 
        if name not in secundary_level:
            secundary_level.append(name)
        else: 
            print("that name was entered previously.")

print("Primary level students.")
for name in primary_level:
    print(name)
print(" ")
print("High school students.")
for name in secundary_level:
    print(name)
print(" ")
non_repeated_names = []
reapeted_name = []
for name in primary_level:
    if name in secundary_level:
        reapeted_name.append(name)
    else: 
        non_repeated_names.append(name)

if reapeted_name == None:
    print("names are not repeated between secondary and primary school students")
else:
    print("Repeated names among secondary and primary school students: ")
    for name in reapeted_name:
        print(name)
print(" ")

print("Primary school names not repeated in secondary school.")
for name in non_repeated_names:
    print(name)
"""
#Ejercicio 7

"""
occurrences = {}
num_strings = 0
while num_strings < 50:
    text = input("Enter a string (o 'x' for finish).\n-->  ")
    if text == 'x':
        break
    num_strings += 1

    for caracter in text:
        if caracter in occurrences:
            occurrences[caracter] += 1
        else:
            occurrences[caracter] = 1

print("Character occurrences in the entered strings:")
for caracter, cantidad in occurrences.items():
    print(f"'{caracter}': {cantidad}")
"""
#Ejercicio 8
"""
import random
goals = []
for row in range(10):
    row_list = []
    for col in range(10):
        if row == col:
            row_list.append(0)
        else: 
            row_list.append(random.randint(0, 5))
    goals.append(row_list)

for row in goals:
    for n in row: 
        print(n, end= " ")
    print()

for team in range(10): 
    wins = 0
    draws = 0
    losses = 0
    goals_scored = 0
    goals_received = 0
    for opponent in range(10): 
        if team != opponent:
            if goals[team][opponent] > goals[opponent][team]:
                wins += 1
            elif goals[team][opponent] == goals[opponent][team]:
                draws += 1
            else:
                losses += 1
            goals_scored += goals[team][opponent]
            goals_received += goals[opponent][team]
    print(f"<<<  Team {team+1}   >>>\nWon {wins} matches.\nLost {losses} matches.\nDrew {draws} matches.")
    if goals_scored > goals_received:
        print(f"{goals_scored} goals scored.\n{goals_received} goals received.\nThere is a difference of {goals_scored - goals_received} goals.")
    else: 
        print(f"{goals_scored} goals scored.\n{goals_received} goals received.\nThere is a difference of {goals_received - goals_scored} goals.")
    print(f"Accumulated a total of {goals_scored} points for team {team+1}\n ")


"""
# Ejercicio 9

import random

rows = 4
columns = 4
board = [['||||' for _ in range(columns)] for _ in range(rows)]
revealed_board = [['  ' for _ in range(columns)] for _ in range(rows)]

def initialize_board():
    numbers = list(range(1, (rows * columns) // 2 + 1)) * 2
    random.shuffle(numbers)
    index = 0
    for i in range(rows):
        for j in range(columns):
            board[i][j] = '||||'
            revealed_board[i][j] = str(numbers[index])
            index += 1

def print_board(board_to_print):
    for i in range(rows):
        print(' '.join(board_to_print[i]))

def compare_elements(row1, column1, row2, column2):
    element1 = revealed_board[row1 - 1][column1 - 1]
    element2 = revealed_board[row2 - 1][column2 - 1]
    
    if element1 == element2:
        print("¡Coincidencia!")
        board[row1 - 1][column1 - 1] = '    '
        board[row2 - 1][column2 - 1] = '    '
        print_board(board)
    else:
        print("No coinciden.")

initialize_board()

print("Tablero inicial:")
print_board(board)

while True:
    row1 = int(input("Ingrese la fila de la primera carta: "))
    column1 = int(input("Ingrese la columna de la primera carta: "))
    print("Elemento seleccionado: " + revealed_board[row1 - 1][column1 - 1])
    
    row2 = int(input("Ingrese la fila de la segunda carta: "))
    column2 = int(input("Ingrese la columna de la segunda carta: "))
    print("Elemento seleccionado: " + revealed_board[row2 - 1][column2 - 1])
    
    compare_elements(row1, column1, row2, column2)
    
    # Verificar si todas las parejas han sido encontradas
    found_pairs = sum(row.count('    ') for row in board)
    if found_pairs == rows * columns:
        print("¡Felicidades! ¡Has encontrado todas las parejas!")
        break



#Ejercicio 10
"""
import random
list_matriz = []
while True:
    num = int(input("Enter a number:"))
    if num < 2: 
        print("Error, try again.")
    else:
        break

for f in range(num):
    row = []
    for c in range(num):
        row.append(random.randint(1,9))
    list_matriz.append(row)

for row in list_matriz:
    for n in row: 
        print(n, end= " ")
    print()

print(" \nMain diagonal")
for f in range(num):
    for c in range(num):
        if f == c:
            print(list_matriz[f][c], end= " ")
        else: 
            print("*", end= " ")
    print()

print(" \nReverse diagonal")
for f in range(num):
    for c in range(num):
        if f + c == num - 1:
            print(list_matriz[f][c], end= " ")
        else: 
            print("*", end= " ")
    print()

"""
#Ejercicio 11
"""
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Ingresa una divisa: ")

if divisa in divisas:
    simbolo = divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}")
else:
    print("Divisa no encontrada en el diccionario")

    """
#Ejercicio 12
"""
name = input("Enter your name.\n-->  ")
while True:
    age = int(input("Enter your age.\n-->  "))
    if age < 0 or age>100:
        print("Error, the age is wrong,try again.")
    else:
        break
address = input("Enter your address.\n-->  ")
cell_phone = int(input("Enter your cell phone number.\n-->  "))

profile = {'name':name,'age':age,'address':address,'cell_phone':cell_phone }
print(f"{profile['name']} tiene {profile['age']} años, vive en {profile['address']} y su número de teléfono es {profile['cell_phone']}.")

"""
#Ejercicio 13
"""
dictionary = {'manzana':900,'banana':1000,'naranja':700,'mandarina':650,'uva':1200}

fruit = input("What fruit would you like?\n-->  ").lower()

if fruit in dictionary:
    while True:
        kilograms = float(input("Enter a kilograms of fruit you want:\n-->  "))
        if kilograms < 0:
            print("Error,the number is incorrect.Try again.")
        else:
            break
    print(f"{kilograms} kg of {fruit} is ${kilograms*dictionary[fruit]}.")
else: 
    print("The fruit isn't in the price dictionary.")

"""