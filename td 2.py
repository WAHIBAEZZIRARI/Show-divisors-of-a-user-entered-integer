num = int(input("Entrez un entier : "))
diviseurs = []
for i in range(1, num + 1):
    if num % i == 0:
        diviseurs.append(i)

print("Diviseurs :", diviseurs)
print("Nombre de diviseurs :", len(diviseurs))
