"""
Escribir una función que simule el siguiente experimento: Se tiene una rata en una
jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
La función debe devolver el tiempo que tarda la rata en salir de la jaula.
"""
#Function
def time_for_liberty(counter_time):

    while True:
        way = int(input("Choise the option to escape:\n[1]First way.\n[2]Second way.\n[3]Third way."))
        if way not in (1,2,3):
            print("Error, The option is incorrect.")
        else:
            break
    

    if way ==1:
        counter_time += 3
        print("3 minutes have passed, you are going back to the cage.\n ")
        return time_for_liberty(counter_time)
    elif way ==2:
        counter_time += 5
        print("5 minutes have passed, you are going back to the cage.\n ")
        return time_for_liberty(counter_time)
    else:
        counter_time += 7
        print("7 minutes have passed, you left the cage!!\n ")
        return counter_time
    
#Main
print("I trapped you in a cage!!!")
counter = 0
counter = time_for_liberty(counter)

print(f"{counter} minutes have passed for you to escape from the cage.")

#Ejercicio 2
"""
Escribir una consigna apropiada para la siguiente función. Asumir que n es un número
entero."""

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

# LLamaria a la función como "invert_number" : 
def invert_number(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))