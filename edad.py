#Edad
#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos

#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.
#El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.

print("Type your birthday")
day = int(input("Write the number of the day you were born: "))
month = int(input("Write the number of the month you were born: "))
year = int(input("Write the number of the year you were born: "))

from time import localtime
t = localtime()
bYear = t.tm_year - year 

if (t.tm_mon < month) or (t.tm_mon == month and t.tm_mday < day):
    bYear -= 1 
    
print(f""" You are {bYear} years old""")