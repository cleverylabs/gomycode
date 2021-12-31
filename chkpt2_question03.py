# Given number
given = int(input('Donner un nombre entier: '))

# Dictionary
dico = {}

# Si le nombre donné est 0
if given > 0:
    for nb in range(given, 0, -1):
        dico[str(nb)] = nb * nb

# afficher le resultat
print(dico)
