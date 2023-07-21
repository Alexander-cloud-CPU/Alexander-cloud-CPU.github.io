# break - ejemplo
x = " "
while True:
    if x != "chupacabra":
        x = input("Ingrese una palabra: ")
    else:
        break
print("Has dejado el bucle con éxito.")    


# continue - ejemplo

word_without_vowels = ""

user_word = input("ingres una palabra: ")
user_word = user_word.upper()


for letter in user_word:
    if letter == "A":
        continue
    if letter == "E":
        continue
    if letter == "I":
        continue
    if letter == "O":
        continue
    if letter == "U":
        continue
    else:
        word_without_vowels = word_without_vowels + letter
        
print( word_without_vowels)
