#Palabra más larga
#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.
#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol
#Palabra 1: plancha
#Palabra 2: lapices
#Las dos palabras tienen el mismo largo

firstWord = input("Word 1: ")
secondWord = input("Word 2: ")

lenghtOne = len(firstWord)
lenghtTwo = len(secondWord)

if lenghtOne > lenghtTwo:
    difference = lenghtOne - lenghtTwo
    print(f"The word '{firstWord}' is {difference} letters longer than '{secondWord}'.")
elif lenghtTwo > lenghtOne:
    difference = lenghtTwo - lenghtOne
    print(f"The word '{secondWord}' is {difference} letters longer than '{firstWord}'.")
else:
    print("Both words have the same length.")

