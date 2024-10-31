#Calculadora
#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.

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