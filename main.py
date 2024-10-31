#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.
#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

height = float(input("Enter you height in meters: "))
weight = int(input("Enter you weight in kilos: "))
age = int(input("Write your age: "))

imc = weight / (height**2)  #utilizar mejor los [math.pow(numero, potencia)] para elevar

if age < 45 and imc < 22.0:
    print("You have low risk")
if age < 45 and imc >= 22.0:
    print("You have Medium risk")
if age >= 45 and imc < 22.0:
    print("You have Medium risk")
if age >= 45 and imc >= 22.0: 
    print("You have High risk")