#División¶
#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5

#La división no es exacta.
#Cociente: 2
#Resto: 4

#Dividendo: 100
#Divisor: 10

#La división es exacta.
#Cociente: 10
#Resto: 0

FirstNumber = int(input("Enter the numerator: "))
SecondNumber = int(input("Enter the divisor: "))

if SecondNumber != 0: 
    Result = int(FirstNumber / SecondNumber)
    if FirstNumber % SecondNumber == 0:
        print(f"""The result is {Result}  and the division is exact""")
    else: 
        print(f"Thats not an exact division and its result is {Result} ")
else: 
    print("You cant divide by zero")