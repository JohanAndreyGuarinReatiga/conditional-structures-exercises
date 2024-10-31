#Triángulos
#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.
a = float(input("Escriba el lado a: "))
b = float(input("Escriba el lado b: "))
c = float(input("Escriba el lado c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("El triangulo es equilatero.")
    elif a == b or a == c or b == c:
        print("El triangulo es isoceles.")
    else:
        print("El triangulo es escaleno.")
else:
    print("No es un triangulo valido.")
