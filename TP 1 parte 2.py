#                           >>>TRABAJO PRÁCTICO N1 - SEGUNDA PARTE<<<

#Ejercicio 1
base = int(input("Ingrese la base del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
perimetro = (base+altura)*2
area = base * altura 
print("El perímetro del rectángulo es de ", perimetro)
print("El área del rectángulo es de ", area)

#Ejercicio 18
cena = float(input("¿Cuánto costó la cena?: "))
cena = cena + (cena*0.062) + (cena*0.10)
print(" El monto final de la cena es de ", cena)

#Ejercicio 19
dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))
print(dia/mes/anio)