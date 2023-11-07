#Ejercicio 1
"""
def digit_number(num):
    if num <10:
        return 1
    else:
        return 1 + digit_number(num/10)
#main
while True:
    num = int(input("Enter a positive integer.\n-->  "))
    if num <= 0: 
        print("Error, number incorrect, try again.")
    else:
        break

digits = digit_number(num)
print(f"The number {num} has {digits} digits.")

"""
#Ejercicio 2
"""
def power(n,b):
    if n == 1:
        return True
    if n < b or n % b != 0:
        return False 
    return power(n // b, b)
    

#main
while True:
    n = int(input("Enter a positive integer.\n-->  "))
    if n <= 0: 
        print("Error, number incorrect, try again.")
    else:
        break
while True:
    b = int(input("Enter a positive integer.\n-->  "))
    if b <= 0: 
        print("Error, number incorrect, try again.")
    else:
        break

result = power(n,b)
print(f"The number {n} is a power of {b}: {result}.")

"""
#Ejercicio 3

"""
#Funtion
def recursive_find_occurrences(a, b, start=0, positions=None):
    if positions is None:
        positions = []

    pos = a.find(b, start)

    if pos != -1:
        positions.append(pos)
        start = pos + 1
        return recursive_find_occurrences(a, b, start, positions)
    else:
        return positions

# Main
a = input("Enter a phrase.\n--> ")
b = input("Enter a string.\n--> ")
results = recursive_find_occurrences(a, b)
print(f"The positions of '{b}' in '{a}' are: {results}")

"""

#Ejercicio 4:
"""
def par(n):
    if n == 0:
        return True  # El cero se considera par
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False  # El cero se considera par
    else:
        return par(n - 1)

#main
while True:
    n = int(input("Enter a positive integer.\n-->  "))
    if n <= 0: 
        print("Error, number incorrect, try again.")
    else:
        break
if impar(n):
    print(f"{n} es impar.")
else:
    print(f"{n} es par.")

"""
#Ejercicio 5
"""
#function
def mayor_num(listt,i=0,bigger_number=None):
    if i == 0:
        bigger_number = listt[0]

    if i == len(listt):
        return bigger_number
    else:
        if listt[i] > bigger_number:
            return mayor_num(listt,i+1,listt[i])
        else:
            return mayor_num(listt,i+1,bigger_number)

#Main        
my_list = [3, 7, 1, 10, 5]
print(my_list)
bigger = mayor_num(my_list)
print("The largest number on the list is ", bigger)

"""
#Ejercicio 6

"""
def repetitions_list(my_list,repetitions,new_list=[],i=0):
    if i == len(my_list):
        return new_list
    else:
        for n in range(repetitions):
            new_list.append(my_list[i])
        return repetitions_list(my_list,repetitions,new_list,i+1)



my_list = [1,2,3,4]
repetitions = 2

print(f"The list: {my_list}. Repetitions: {repetitions}")

new_list = repetitions_list(my_list,repetitions)
print(new_list)

"""

#Ejercicio 7
"""
def calculate_k(n,p):
    if n == 1:
        return p
    else:
        return n * p + calculate_k(n-1,p)


while True:
    n = int(input("Enter a first number.\n-->  "))
    if n < 1:
        print("Enter a number greater than 0.Try again.")
    else:
        break

p = int(input("Enter a second number.\n-->  "))

k = calculate_k(n,p)
print(f"The result of K({n}, {p}) is: {k}.")

"""
#EJercicio 8
"""8.	El triángulo de Pascal es un arreglo triangular de números que se define 
de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. 
Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). 
Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor 
se calcula sumando los dos valores contiguos de la fila de arriba.Escribí la función recursiva 
pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k."""
"""#function
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# main
n = 5  
k = 2 
result = pascal(n, k)
print(f"The value in row {n} and column {k} of Pascal's Triangle is: {result}")
"""

#Ejercicio 9
"""9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres 
únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los 
caracteres dados (permitiendo caracteres repetidos).
"""
"""
# Function
def combinations(list, k, prefix=""):
    if k == 0:
        print(prefix)
        return
    for character in list:
        combinations(list, k - 1, prefix + character)

# Main
characters = ['A', 'B', 'C']
k = 2
combinations(characters, k)


"""

#Ejercicio 10

def paper_size_A(N):
    if N == 0:
        return (841, 1189)
    else:
        previous_width, previous_length = paper_size_A(N - 1)
        
        new_width = previous_length
        new_length = previous_width / 2
        
        return (new_width, new_length)

# Main
N = 6 
width, length = paper_size_A(N)
print(f"The measurements of paper A{N} are: Width = {int(width)} mm, Length = {int(length)} mm")

