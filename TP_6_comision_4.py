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

#Ejercicio 7


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




#Ejercicio 9



#Ejercicio 10


#Ejercicio 12

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
