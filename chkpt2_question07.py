import math

C = 50
H = 30

D = input('Saisir les valeur de D (X,Y,Z): ')

list_D = D.split(',')

racine_carre = []
for value in list_D:
    racine_carre.append(str(int(math.sqrt((2 * C * int(value) / H)))))

print(','.join(racine_carre))

