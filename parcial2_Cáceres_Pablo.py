import random

def generate_dna():
    dna = []
    i = 1
    while len(dna) < 6:
        line = input(f"Enter the DNA sequence for line {i}/6:\n--> ").upper() #permite escribir en minusculas para no hacer complicado el proceso
        if len(line) != 6:
            print("ERROR!! It must be 6 letters, please try again.") #l generador manual del adn, si no escribe los caracteres suficientes le sale mensaje de error
        elif any(letter not in "ATCG" for letter in line):
            print("ERROR!! You entered an incorrect letter, only A, T, C, or G are allowed.") #Si se ingresa una letra que no pertenezca ATCG debe volver a escribir la secuncia adn porqie no es válido
        else:
            dna.append(line)
            i += 1   #suma los string a la lista dna
    return dna

#generador random para hacer pruebas y no estar haciendolas a mano
def generate_random_dna(): 
    letters = 'ATCG'
    dna = []

    for _ in range(6):
        sequence = ''
        for _ in range(6):
            sequence += random.choice(letters)
        dna.append(sequence)

    return dna

def display_dna(dna):  #imprime la matriz dna 
    for sequence in dna:
        for letter in sequence:
            print(f"{letter}", end="  ")
        print()

def check_sequence(x, y, dx, dy, dna):
    letter = dna[x][y]
    for _ in range(3):
        x += dx
        y += dy 
        if x < 0 or x >= 6 or y < 0 or y >= 6 or dna[x][y] != letter: # verifica que la dirección no sé pase de los limites de la matriz, en caso de pasarse retorna false
            return False
    return True

def is_mutant(dna): 

    count = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)] # con la primer direccion se encarga de verificar de forma vertical, la segunda de forma horizontal, la tercera de diagonal principal y la cuarte de diagonal inversa
    for x in range(6):
        for y in range(6):
            for dx, dy in directions: #por cada letra de la matriz utiliza cada verificador de direccion, de esta forma podemos saber si una letra puede acabar en alguna de las secuancias
                if check_sequence(x, y, dx, dy, dna):
                    count += 1

    return count > 1 #Retorna True en caso de que se cumpla la condición y sino, False

# Main
print("Hello, welcome to the mutant detector.")
#dna = generate_random_dna()     #utilice el generador random para encontrar casos positivos o negativos para la prueba.
dna = generate_dna()
print("This is the DNA to analyze:")
display_dna(dna)
print()

if is_mutant(dna) == True: #resultados
    print(f"The human:\nDNA = {dna} \nIs a mutant, Magneto can recruit them.")
else:
    print(f"The human:\nDNA = {dna} \nIs not a mutant, ignore them Magneto.")

