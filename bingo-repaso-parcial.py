"""Crea un juego de Bingo donde el usuario pueda ingresar los números para generar su propio cartón de bingo. A
continuación, se detalla cómo se debe implementar el juego:
1. Solicita al usuario que ingrese 25 números únicos, uno a la vez, para completar su cartón de bingo. Los
números deben estar en el rango de 1 a 75.
2. Valida que los números ingresados sean únicos y estén dentro del rango permitido. Si el usuario ingresa un
número duplicado o fuera del rango, debe mostrar un mensaje de error y solicitar otro número.
3. Después de que el usuario haya completado su cartón, inicia el juego de Bingo.

4. Extrae bolas de bingo al azar y verifica si los números extraídos están en el cartón del usuario.
5. Continúa extrayendo bolas de bingo hasta que el jugador complete una línea horizontal, vertical o diagonal
en su cartón.
6. Muestra mensajes informativos al usuario a medida que se extraen bolas y cuando gana.
7. Pregunta al usuario si desea jugar de nuevo al finalizar el juego.
Recuerda proporcionar instrucciones claras y manejar las entradas del usuario de manera amigable. El objetivo es
crear un juego interactivo que permita al usuario disfrutar del Bingo personalizado."""
#Funciones

#Main
import random



def generar_carton():
    # numeros_unicos = random.sample(range(1, 76), 25)
    carton = [] 
    numeros_unicos = []
    while len(numeros_unicos) < 25:
        num = input(f"Ingrese un número para su cartón ({len(numeros_unicos)+1}/25): ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 75:
                if num not in numeros_unicos:
                    numeros_unicos.append(num)
                else:
                    print("Error: El número ya ha sido ingresado. Intente nuevamente.")
            else:
                print("Error: El número debe estar en el rango de 1 a 75. Intente nuevamente.")
        else:
            print("Error: Ingrese un número válido. Intente nuevamente.")
    
    for i in range(0, 25, 5):
        fila = numeros_unicos[i:i+5]
        carton.append(fila)

    return carton

def imprimir_carton(carton):
    print("Cartón de Bingo:")
    for fila in carton:
        for num in fila:
            print(f"{num:2}", end=" | ")
        print()

def jugar_bingo(carton):
    numeros_bingo = list(range(1, 76))
    random.shuffle(numeros_bingo)

    print("Comienza el juego de Bingo:")
    for numero in numeros_bingo:
        print(f"Número de Bingo: {numero}")
        for i in range(5):
            if numero in carton[i]:
                indice = carton[i].index(numero)
                carton[i][indice] = 0
        imprimir_carton(carton)
        if any(all(num == 0 for num in fila) for fila in carton):
            print("¡Bingo! Has ganado.")
            return
    print("Lo siento, no has ganado en este juego.")


#main
while True:
        print("Bienvenido al Juego de Bingo Personalizado")
        carton = generar_carton()
        imprimir_carton(carton)
        jugar_bingo(carton)
        respuesta = input("¿Desea jugar de nuevo? (s/n): ")
        if respuesta.lower() != 's':
            break







