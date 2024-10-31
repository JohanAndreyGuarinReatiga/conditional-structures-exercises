#Ordenamiento
#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

print("Selecciona una opción:")
print("1. Ordenar dos números")
print("2. Ordenar tres números")
print("3. Ordenar cuatro números")

option = int(input("Enter the number of the desired option: "))

if option == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter de second number: "))
    sorted_nums = sorted([num1, num2])
    print("Números ordenados:", " ".join(map(str, sorted_nums)))
elif option == 2:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    sorted_nums = sorted([num1, num2, num3])
    print("Números ordenados:", " ".join(map(str, sorted_nums)))
elif option == 3:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    num4 = int(input("Ingrese el cuarto número: "))
    sorted_nums = sorted([num1, num2, num3, num4])
    print("Números ordenados:", " ".join(map(str, sorted_nums)))
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")
