
def curret(secret,guessed):  
    #Mostrar parcialmente las letras adivinadas
    curret_word = ""
    for each_letter in secret:
        if each_letter in guessed:
            curret_word += each_letter
        else:
            curret_word += "_"
    print("Palabra actual: ", curret_word)