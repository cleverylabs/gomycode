# Given String
given_str = ''
while len(given_str) == 0:
    given_str = input('Donner un texte non-vide: ')

# Given number
given_int = int(input('Donner un nombre entier: '))
while given_int >= len(given_str):
    given_int = int(input('Donner un nombre entier: '))

# Chaine saisie
print('COMPLET: ' + str(given_str))
liste = list(given_str)
del(liste[given_int])

print('MODIFIE: ' + ''.join(liste))
