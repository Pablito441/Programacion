#Ejercicio 1

phrase = str(input("Enter a pharse: "))

if len(phrase) == 4:
    phrase += "!"
else:
    phrase += "?"

print(phrase)