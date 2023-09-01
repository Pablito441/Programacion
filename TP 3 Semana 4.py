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
#Ejercicio 5

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


    # 5- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad_inversion = int(input("Ingrese la cantidad que desea invertir: "))
interes = int(input("Ingrese el interés anual: "))
tiempo =  int(input("Ingrese la cantidad de años: "))
capital_acumulado = cantidad_inversion
for i in range(1, tiempo+1):
    nuevo_interes = (capital_acumulado*interes)/100
    print("EL INTERES ES:", nuevo_interes)
    capital_acumulado = capital_acumulado + nuevo_interes
    print(f"Año {i}:\nCapital invertido:{cantidad_inversion}\nCapital invertido mas intereses: {capital_acumulado}")



