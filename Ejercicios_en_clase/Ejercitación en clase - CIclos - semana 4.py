# 1- Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
# integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
# La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
# deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
# método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
# mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares.
# Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
# Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
# Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
# correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
# mismo corrimiento.
# Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
# comenzar desde la letra “a”.
# Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
# español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
# vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
# Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.

#RESOLUCIÓN
"""
abcdario = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Determinar la cantidad lugares que se correrá la letra: "))
#defino mi abecedario, es decir, los únicos carácteres que se correran y pregunto por la cantidad de lugares que se correra para encriptar el mensaje
for i in range(5): #Defino la cantidad de mensajes que se encriptaran

    mensaje = input("Mensaje a encriptar: ") 
    encriptado = "" #inicializo la variable vacia en donde se acumulará las letras corridas del mensaje a encriptar

    for caracter in mensaje:    #Por cada caracter del mensaje

        if caracter.lower() in abcdario :   #Defino una condicion para asegurarme que ese carácter se encuentre en el abcdario

            indice_letra = int(abcdario.find(caracter.lower())) #Busco el índice de la letra del mensaje en el abcdario
            indice_letra = (indice_letra+corrimiento)%27    #al índice le sumo la cantidad de lugares a correr y %27 para que solo exista un rango de 27 lugares, en donde si se llega al último vuelve a comenzar por el lugar 1
            encriptado += abcdario [indice_letra] # En la variable encriptado que estaba vacia voy concatenando cada letra que anteriormente corrimos

        else:
            encriptado += caracter # en caso de que el carácter no se encuentre en el abcdario no se modificará 

    print(f"El mensaje incriptado para el oficial {i+1}: {encriptado}.") # muentro la palabra encriptada

"""

#2- Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
#0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""

# RESOLUCIÓN

#Primero defino cada variable por cero para usarlos como contador y defino num por 1 para que entre en el ciclo
num = 1
pares_total = 0
impares_total = 0   

while num != 0: 
    num = str(input("Ingrese un número: ")) #Ingreso de número en string para poder recorrer el número en el bucle for
    pares = 0
    impares = 0 #Inicializo las variables temporales para cada número que se escriba

    if int(num) == 0:  #Condicional en caso de que se escriba 0 no se ejecute el resto del código
        num = int(num)  #lo vuelvo a inicializar como entero para que pueda compararse en el bucle
    else:

        for caracter in num: 
            if int(caracter) % 2==0:  #si es par se guarda en las las dos variables acomuladoras, la primera solo acomula las cifras de cada número escrito y la otra el total de veces que se leyó a lo largo del código
                pares += 1
                pares_total += 1
            else: 
                impares += 1
                impares_total += 1

        print(f"El número [{num}] tiene {pares} números pares y [{impares}] números impares.") #Los pares e impares del número escrito

print(f"En el total de números ingresados se encontraron [{pares_total}] números pares y [{impares_total}] números impares.") #Los pares e impares de toda la lectura del código

