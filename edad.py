#Edad
#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos

#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):
print("Enter your birthday")
day = int(input("Write the number of the day you were born: "))
month = int(input("Write the number of the month you were born"))
year = int(input("Write the number of the year you were born"))

from time import localtime
t = localtime()
t.tm_mday
31
t.tm_mon
10
t.tm_year
2024

#INCOMPLETO