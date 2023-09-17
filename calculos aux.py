import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "computadora", "inteligencia", "datos", "aprendizaje"]

# Seleccionar una palabra al azar de la lista
palabra_secreta = random.choice(palabras)

# Inicializar variables
intentos_maximos = 6
intentos = 0
letras_adivinadas = []

# Mostrar un mensaje de bienvenida
print("¡Bienvenido al juego de adivinar la palabra!")

# Bucle principal del juego
while intentos < intentos_maximos:
    # Mostrar la palabra parcialmente adivinada
    palabra_actual = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_actual += letra
        else:
            palabra_actual += "_"
    
    print("Palabra actual: ", palabra_actual)
    
    # Pedir al usuario una letra
    letra_usuario = input("Adivina una letra: ").lower()
    
    # Verificar si la letra está en la palabra secreta
    if letra_usuario in palabra_secreta:
        letras_adivinadas.append(letra_usuario)
        print("¡Correcto! La letra '{}' está en la palabra.".format(letra_usuario))
    else:
        intentos += 1
        print("Incorrecto. Te quedan {} intentos.".format(intentos_maximos - intentos))
    
    # Verificar si el usuario ha adivinado la palabra completa
    if set(palabra_secreta) == set(letras_adivinadas):
        print("¡Felicidades! Has adivinado la palabra: {}".format(palabra_secreta))
        break

# Si se agotan los intentos, mostrar un mensaje de derrota
if intentos == intentos_maximos:
    print("¡Has agotado tus intentos! La palabra secreta era: {}".format(palabra_secreta))
