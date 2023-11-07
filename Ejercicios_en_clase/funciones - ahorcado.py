"""Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al
azar de una lista de palabras predefinidas y permitir que el jugador adivine la palabra letra por
letra. El jugador tiene un número limitado de intentos antes de perder el juego.
Requisitos:
     Define una lista de palabras que el programa pueda elegir al azar para que el jugador
adivine. Puedes usar palabras relacionadas con la programación, tecnología o
cualquier tema que te guste.
     El programa debe seleccionar una palabra al azar de la lista para cada partida.
     El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
lugar correspondiente.
     El jugador debe poder ingresar una letra adivinada en cada turno.
     El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el
tablero en consecuencia.
     El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el
juego.
     Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente"
o "Letra incorrecta, te quedan X intentos".
     El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin
intentos.
     Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de
derrota si se quedan sin intentos.
Consideraciones adicionales:
     Puedes utilizar funciones para organizar tu código de manera efectiva.
     Agrega comentarios para explicar el funcionamiento de tu código."""

#Respuesta: 

import random
import funcióndelahorcado 
# Lista de palabras para el juego.=
random_words = ["gato", "perro", "pato", "conejo", "vaca", "caballo", "jirafa", "leon", "tigre", "elefante"]
attempts = 0 
guessed_letters = []

#Escoje una palabra random de la lista de palabras.
secret_word = random.choice(random_words)

#Mensaje de bienvenida.
print("<<<Bienvenido al ahorcado>>>")
print(" ")

#bucle principal del juego
while attempts != 6:
    
    funcióndelahorcado.curret(secret_word,guessed_letters)

    #preguntar al usuario por la letra
    letter = str(input("Ingrese una letra: "))
    letter = letter.lower()

    #verificación de la letra
    if len(letter) > 1:
        print("Error, ingrese solo una letra. ")
        continue
    elif letter in secret_word:
        print("Genial! la letra pertenece a la palabra secreta :D")
        guessed_letters.append(letter)
    else:
        print("La letra no pertenece a la palabra secreta :(")
        attempts += 1
        print(f"te quedan {5-attempts} intentos")
    print(" ")

    #verificar si el usuario escribio la palabra completa
    if set(secret_word) == set(guessed_letters): 
        print(f"¡¡Felicidades!! adivinaste la palabra secreta: {secret_word}.")
        break

    #Por si se te acaban los intentos
    if attempts == 5: 
        print(f"oh nooo!! Se agotaron los intentos, la palabra secreta era: {secret_word}.")