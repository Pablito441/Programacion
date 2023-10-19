import math
#Ejercicio 1 y ejercicio 3

def valido(w):
    if len(str(w)) == 7 or len(str(w)) == 8:
        return True
    else: 
        return False

#Ejercicio 2

def last_word(p):
    p = p.strip()

    words = p.split()
    
    if words:
        last_wordd = words[-1]
        return len(last_wordd)
    else:
        return 0
    
#Ejercicio 4 y ejercicio 5

def multiple(n1,n2,temp_1, temp_2):
    if temp_1 == temp_2 == 0:
        if(n1 % n2 == 0):
            return print(f"{n1} es multiplo de {n2}")
        elif(n2 % n1 == 0): 
            return print(f"{n2} es multiplo de {n1}")
        else:
            return print("No son múltiplos entre sí.")
    if n1 == n2 == 0:
        return (temp_1+temp_2)/2
    
#Ejercicio 6

def text_space(text):
    for letter in text:
        print(letter, end=" ")
    
#Ejercicio 7

def minim_maxim_num(list):

    if len(list) == 0:
        print("the list is empty.")
    else:
        maximum = minimum = list[0]
        for number in list:
            if number > maximum:
                maximum = number
            elif number < minimum:
                minimum = number
        print(f"the minimum number is {minimum} and the maximum number is {maximum}.")

#Ejercicio 8

def calculate_area_perimeter(radius):

    area = (radius**2) * math.pi
    perimeter = 2 * math.pi * radius
    print(f"the area of the circumference is {area} and the perimeter is {perimeter}.")

#Ejercicio 9

def login(usern, passw):
    if usern == "usuario1" and passw == "asdasd":
        return True
    else:
        return False
    
#Ejercicio 10

def apply_discount(cart,discount):
    total_price = 0
    for product, price in cart.items():
        if product in discount:
            discount_product = price - price * (discount[product]/100)
            total_price += discount_product
        else:
            total_price += price
    return total_price

#Ejercicio 11

def squaree(number):
    return number**2

def apply_def_to_list(listt):
    results_list = []
    for number in listt:
        result = squaree(number)
        results_list.append(result)
    return results_list

#Ejercicio 12

def r_dictionary(p):
    dictionary = {}
    works = p.split()

    for work in works:
        dictionary[work] = len(work)

    return dictionary

#Ejercicio 13

def module_vector_calculate(v):
    module = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    return module

#Ejercicio 14 y 17

def boolean_prime(n):
    count = 0
    if n <= 1: 
        return False
    
    for number in range(1,n+1):
        if n%number == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

#Ejercicio 15

def factorial_number(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

#Ejercicio 16

def count_digits(n,d):
    count = 0
    for i in str(n):
        if i == str(d):
            count += 1
    return count

#Ejercicio 17 

def sum_digit(number):
    sum = 0
    for n in str(number):
        sum += int(n)
    return sum





