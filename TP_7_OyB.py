

#       <<<   TRABAJO PRÁCTICO NÚMERO 7  >>>
# Funciones
def bubble_sort(a):
    num = len(a)
    for i in range(num):
        for j in range(0,num - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]

def insert_sort(a):
    for i in range(1, len(a)):
        current_value = a[i]
        position = i

        while position > 0 and a[position - 1] > current_value:
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

words = input("enter words separated by spaces: ")
list_of_words = words.split()
selection_sort(list_of_words)

print("words arranged alphabetically: ")
for word in list_of_words:
    print(word)

#Ejercicio 3

lista_libros = [
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

