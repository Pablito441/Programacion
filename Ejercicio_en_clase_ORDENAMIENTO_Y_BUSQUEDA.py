#               Ejercicio en clases de métodos de ordenamiento y busqueda
#Funciones
def bubble_sort(a):
    num = len(a)
    for i in range(num):
        for j in range(0,num - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]

def selection_sort(a):
    ult = len(a)

    for i in range(ult):
        min = i
        for j in range(i+1,ult):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]

def insert_sort(a):
    for i in range(1, len(a)):
        current_value = a[i]
        position = i

        while position > 0 and a[position - 1] > current_value:
            a[position] = a[position - 1]
            position -= 1


        a[position] = current_value

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

def busqueda_lineal(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i  
    return -1  

def busqueda_binaria(list, target):
    izquierda, derecha = 0, len(list) - 1
    
    while izquierda <= derecha:
        mid = (izquierda + derecha) // 2
        if list[mid] == target:
            return mid  
        elif list[mid] < target:
            izquierda = mid + 1
        else:
            derecha = mid - 1
    
    return -1  

#Programa principal
list = [3,2,8,1,2,9,7]
element_to_search = 9
print("unordered list")
print(list)
print("")
menu = int(input("[1]buble sort\n[2]selection sort\n[3]insert sort\n[4]merge sort\nChoose the option.\n-->  "))
if menu ==1:
    bubble_sort(list)
elif menu == 2:
    selection_sort(list)
elif menu == 3:
    insert_sort(list)
elif menu == 4:
    list = merge_sort(list)

print("order list")
print(list)

menu2= int(input("[1]linear search\n[2]binary search\nChoose the option.\n-->  "))

if menu2 == 1:
    result_lineal = busqueda_lineal(list, element_to_search)
    if result_lineal != -1:
        print(f"{element_to_search} is found in the index {result_lineal} (búsqueda lineal).")
    else:
        print(f"{element_to_search} not found in the list (búsqueda lineal).")

if menu2 == 2:
    result_binaria = busqueda_binaria(list, element_to_search)
    if result_binaria != -1:
        print(f"{element_to_search} is found in the index {result_binaria} (búsqueda binaria).")
    else:
        print(f"{element_to_search} not found in the list (búsqueda binaria).")