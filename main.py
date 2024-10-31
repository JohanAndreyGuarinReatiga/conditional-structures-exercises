#Letra o número
#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.


caracter = input("Write a character, a number, a letter, or either of them: ")
if caracter.isalpha():
    if caracter.isupper():
        print("The character is a capital letter")
    else:
        print("The character is a lowercase letter")
elif caracter.isdigit():
     print("The caracter is a number")
else:
    print("Isnt either of the options")    
    
#Ingrese caracter: 9
#Es numero.
#Ingrese caracter: A
#Es letra mayúscula.
#Ingrese caracter: f
#Es letra minúscula.
#Ingrese caracter: #
#No es letra ni número.