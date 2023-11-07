

#       <<<   TRABAJO PRÁCTICO NÚMERO 7  >>>
# Funciones
def bubble_sort(a):
    num = len(a)
    for i in range(num):
        for j in range(0,num - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]

def bubble_sort_decendent(a):
    num = len(a)
    for i in range(num):
        for j in range(0,num - i - 1):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]
                

def insert_sort(a):
    for i in range(1, len(a)):
        current_value = a[i]
        position = i

        while position > 0 and len(a[position - 1]) > len(current_value):
            a[position] = a[position - 1]
            position -= 1


        a[position] = current_value
def selection_sort(a):
    ult = len(a)

    for i in range(ult):
        min = i
        for j in range(i+1,ult):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]
    
def selection_sort_book(books):
    n = len(books)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if books[j]["año_publicacion"] < books[min_idx]["año_publicacion"]:
                min_idx = j
        books[i], books[min_idx] = books[min_idx], books[i]

def count_sort(list):
    # Encuentra el valor máximo y mínimo en la lista
    maximum = max(list)
    minimum = min(list)

    # Calcula el rango de valores
    rangee = maximum - minimum + 1

    # Crea una lista de conteo para almacenar la frecuencia de cada valor
    counter = [0] * rangee

    # Llena la lista de conteo
    for num in list:
        counter[num - minimum] += 1

    # Reconstruye la lista ordenada
    index = 0
    for i in range(rangee):
        while counter[i] > 0:
            list[index] = i + minimum
            index += 1
            counter[i] -= 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide la lista en mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llama recursivamente a merge_sort en cada mitad
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


#Ejercicio 1
"""
list_of_number = []
while True:
    number = int(input("Enter a number.(0 for finish).\n-->  "))
    if number == 0:
        print("Thanks you for entered numbers")
        break
    else:
        list_of_number.append(number)

print(" ")
print(f"The created list:\n{list_of_number}\n ")

print("The order list: ")
bubble_sort(list_of_number)
print(list_of_number)

"""
#Ejercicio 2
"""
words = input("enter words separated by spaces: ")
list_of_words = words.split()
selection_sort(list_of_words)

print("words arranged alphabetically: ")
for word in list_of_words:
    print(word)

"""
#Ejercicio 3
"""
books_list = [
    {
        "titulo": "El Gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "año_publicacion": 1925,
        "editorial": "Charles Scribner's Sons"
    },
    {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicacion": 1967,
        "editorial": "Editorial Sudamericana"
    },
    {
        "titulo": "To Kill a Mockingbird",
        "autor": "Harper Lee",
        "año_publicacion": 1960,
        "editorial": "J.B. Lippincott & Co."
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "año_publicacion": 1949,
        "editorial": "Secker & Warburg"
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año_publicacion": 1605,
        "editorial": "Francisco de Robles"
    }
]
for book in books_list:
    print(book)

print(" \nLista de libros ordenada por el año de publicación: \n ")
selection_sort_book(books_list)

for book in books_list:
    print(book)

"""

#Ejercicio 4
"""
words = input("enter words separated by spaces: ")
list_of_words = words.split()
insert_sort(list_of_words)

print("words arranged alphabetically: ")
for word in list_of_words:
    print(word)

"""

#Ejercicio 5
"""
list_of_number = []
while True:
    number = int(input("Enter a number.(0 for finish).\n-->  "))
    if number == 0:
        print("Thanks you for entered numbers")
        break
    else:
        list_of_number.append(number)

print(" ")
print(f"The created list:\n{list_of_number}\n ")

print("The order list: ")
bubble_sort_decendent(list_of_number)
print(list_of_number)
"""
#Ejercicio 6 
"""
list_of_number = []
while True:
    number = int(input("Enter a number.(0 for finish).\n-->  "))
    if number == 0:
        print("Thanks you for entered numbers")
        break
    else:
        list_of_number.append(number)
print("Unordered list: ") 
print(list_of_number)
print()     
count_sort(list_of_number)

print("Order list: ")
print(list_of_number)
print()

"""

#Ejercicio 7
"""
my_list = [3,'pablo','apple', 1, 'kiwi', 2,4,1,'grape', 'orange','pepe']

print(f"Unorder list:\n{my_list}\n ")
# Separate numbers and strings into different lists
numbers = [x for x in my_list if isinstance(x, int)]
strings = [x for x in my_list if isinstance(x, str)]

# Sort the lists of numbers and strings separately
numbers.sort()
strings.sort()

# Combine the sorted lists
result = numbers + strings

print("List sorted with numbers first and strings afterwards:")
print(result)
"""
#Ejercicio 8
"""
list_of_number = []
while True:
    number = int(input("Enter a number.(0 for finish).\n-->  "))
    if number == 0:
        print("Thanks you for entered numbers")
        break
    else:
        list_of_number.append(number)
print("Unordered list: ") 
print(list_of_number)
print()     
list_of_number = merge_sort(list_of_number)

print("Order list: ")
print(list_of_number)
print()

"""