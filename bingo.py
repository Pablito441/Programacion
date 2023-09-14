import random
#Defino la lista y el tamaño de la lista
list_number = []
list_one = []
list_two = []
listaa = []
count = 0
# Se llena la lista con número del 1 al 50
list_number = random.sample(range(1, 25),10)
print (list_number)

for i in range(0,5):
    list_one.append( list_number[i])
for i in range(5,10):
    list_two.append(list_number[i])

list_one.sort()
print(list_one)
print(list_two)


while True:
    num = int(input("Ingrese su número: "))
    if num in listaa:
        print("Ya ingresaste ese numero, Ingrese un número nuevo: ")
        continue
    if num < 1 or num >24:
        print("Ingresó un número incorrecto, vuelva a escribirlo")
        continue
    else:
        listaa.append(num)
        count += 1
    if count == 5:
        break

list_one.sort()
list_two.sort()
listaa.sort()

if listaa == list_one:
    print("Ganaste el juego pa")
elif listaa == list_one:
    print("Ganaste el juego pa")
else: 
    print("Perdon, fracasaste")
print(listaa)




