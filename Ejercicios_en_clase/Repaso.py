#Ejercicio 1
"""
phrase = str(input("Enter a pharse: "))

if len(phrase) == 4:
    phrase += "!"
else:
    phrase += "?"

print(phrase)
"""
#Ejercicio 2
"""
import random

# word list for the game
random_words = ["gato", "perro", "pato", "caca", "cine"]
attempts = 0 
guessed_letters = []

#Choice a ramdon word from the list
secret_word = random.choice(random_words)

#Welcome menssage
print("Welcome to the word guessing game.")

#main game loop
while attempts != 5:

    #show the partially guessed word
    curret_word = ""
    for each_letter in secret_word:
        if each_letter in guessed_letters:
            curret_word += each_letter
        else:
            curret_word += "_"
    print("Curret word: ", curret_word)

    #ask the user for a letter
    letter = str(input("Enter a letter: "))
    letter = letter.lower()

    #letter verification
    if len(letter) > 1:
        print("Enter one letter only. ")
        continue
    elif letter in secret_word:
        print("This letter is in the secret word.")
        guessed_letters.append(letter)
    else:
        print("This letter isn't in the secret word.")
        attempts += 1
        print(f"you have {5-attempts} attempts left")

    #check if the user has guessed the complete word
    if set(secret_word) == set(guessed_letters): 
        print(f"great, you guessed the secret word: {secret_word}.")
        break

    #If your attempts run out
    if attempts == 5: 
        print(f"You have exhausted your attempts! The secret word was: {secret_word}.")
"""
#Ejercicio 3
"""
text = input("Enter a sentence: ")

words_list = text.split()
word_counter = len(words_list)

print(f"the number of words in the entered text is {word_counter}.")
"""
#Ejercicio 4
"""
minimum_salary = 100000

while True:
    all_month = int(input("Did you attend all month? yes[1] - no[2]"))
    if all_month < 1 or all_month > 2:
        print("Wrong number, try again.")
    else: 
        break

while True:
    sunday_hours = int(input("How many overtime hours did you work on sundays?"))
    if sunday_hours < 3 or sunday_hours >10:
        print("The hours must be between 3 and 10 hours, try again.")
    else:
        break

if all_month == 1 and sunday_hours > 2 and sunday_hours < 6:
    additional_salary = minimum_salary * 0.03
    print(f"His total salary is {minimum_salary + additional_salary}")

elif all_month == 1 and sunday_hours > 5 and sunday_hours < 11:
    additional_salary = minimum_salary * 0.10
    print(f"His total salary is {minimum_salary + additional_salary}")

elif all_month == 2 and sunday_hours > 2 and sunday_hours < 11:
    additional_salary = minimum_salary * 0.02
    print(f"His total salary is {minimum_salary + additional_salary}")
"""
#Ejercicio 5
"""

number_one = int(input("Enter the firts number: "))
number_second = int(input("Enter the second number: "))

if number_one == number_second:
    print(f"[{number_one} x {number_second} = {number_second*number_one}]")
elif number_one > number_second:
    print(f"[{number_one} - {number_second} = {number_one - number_second}]")
else:
    print(f"[{number_one} + {number_second} = {number_second+number_one}]")
    """

#Ejercicio 6
"""
while True:
    age = int(input("Enter your age: "))
    if age < 45:
        print("entered an age impossible to retire, try again.")
    else:
        break

while True:
    antiquity_employment = int(input("How long have you been at work?: "))
    if antiquity_employment < 1: 
        print("Error, try again.")
    else: 
        break

if age >= 60 and antiquity_employment < 25:
    print("Retirement by age.")
elif age < 60 and antiquity_employment > 25:
    print("Retirement due to young seniority.")
elif age >= 60 and antiquity_employment > 25:
    print("Retirement due to adult seniority")
else:
    print("You can't retire")
    """
#Ejercicio 7

while True:
    years = int(input("How many years have you been in the company? "))
    if years <0: 
        print("Error, try again.")
    else: 
        break

if years == 0:
    print("Receive a profit of 5% of your monthly salary.")
elif years == 1: 
    print("Receive a profit of 7% of your monthly salary.")
elif years >= 2 and years <5: 
    print("Receive a profit of 10% of your monthly salary.")
elif years >= 5 and years <10:  
    print("Receive a profit of 15% of your monthly salary.")
elif years >10: 
    print("Receive a profit of 20% of your monthly salary.")