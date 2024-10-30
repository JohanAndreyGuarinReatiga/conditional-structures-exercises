#Calculadora
#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.

#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5

#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1

#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20

#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5

#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

FirstNumber = float(input("Enter the first operand: "))
Operator = input("Write an operator +  -  *  / : ")
SecondNumber = float(input("Enter the second operand: "))

if Operator == "+":
    Result = FirstNumber + SecondNumber
elif Operator == "-":
    Result = FirstNumber - SecondNumber
elif Operator == "*":
    Result = FirstNumber * SecondNumber
elif Operator == "/":
    if SecondNumber != 0:
        Result = FirstNumber / SecondNumber
    else:
        Result = "Oops, you cant divde by zero"
else:
    Result = "Oops, you have to write an operator"

print("The result is:", Result)