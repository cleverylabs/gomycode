# Given number
given = int(input('Donner un nombre entier: '))
factorial = 1

# Si le nombre donné est 0
if given > 0:
    for nb in range(given, 1, -1):
        factorial = factorial * nb

# afficher le resultat
print(factorial)
