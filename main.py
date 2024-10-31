#Ordenamiento
#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

print("Choose an option ")
print("1. Organize two numbers")
print("2. Organize three numbers")
print("3. Organize four numbrs")

option = int(input("Enter the number of the desired option: "))

if option == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter de second number: "))
    sortedNums = sorted([num1, num2])
    print("Numbers in order", " ".join(map(str, sortedNums)))
elif option == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter de second number: "))
    num3 = int(input("Enter the third number: "))
    sortedNums = sorted([num1, num2, num3])
    print("Numbers in order", " ".join(map(str, sortedNums)))
elif option == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter de second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    sortedNums = sorted([num1, num2, num3, num4])
    print("Numbers in order:", " ".join(map(str, sortedNums)))
else:
    print("No valid option. Choose between 1, 2 or 3.")
