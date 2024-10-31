a = 5
b =  7
p = 7

if a >= 6 and (a - b >= 2):
    print("A wins")
elif a >= 6 and (a - b >= 2):
    print("B wins")
    
    #sin terminar


# Solicitar los juegos ganados por A y B
gamesA = int(input("Juegos ganados por A: "))
gamesB = int(input("Juegos ganados por B: "))

# Verificar si la entrada es inválida

if gamesA > 7 or gamesB > 7 or (gamesA == 7 and gamesB < 5) or (gamesB == 7 and gamesA < 5) or abs(gamesA - games_B) > 2:
    print("Invalido")
# Verificar si A gana el set

elif gamesA == 6 and gamesB <= 4:
    print("Gano A")
elif gamesA == 7 and (gamesB == 5 or gamesB == 6):
    print("Gano A")
# Verificar si B gana el set

elif gamesB == 6 and gamesA <= 4:
    print("Gano B")
elif gamesB == 7 and (gamesA == 5 or gamesA == 6):
    print("Gano B")
    
# Si ninguno ha ganado, el set aún no termina

else:
    print("Aun no termina")
