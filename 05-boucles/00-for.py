# Une boucle for permet de parcourir un tableau pour exécuter une opération ou
# une vérification sur chaque valeur.

# Exemple : for number in [7, 45, 65]
# La variable number prendra successivement les valeurs 7, 45 et 65

# Utilisez une boucle for pour calculer la moyenne des notes ci-dessous.
# Stockez le résultat dans une variable "average"

################################################################################
notes: list[int] = [10, 15, 12, 8, 7]

somme: float = 0

for each_notes in notes :
    somme += each_notes

average: float = somme/len(notes)
################################################################################

# Note : si vous connaissez déjà python, vous savez peut-être qu'il existe des
# méthodes plus simples pour calculer une moyenne... Mais chaque chose en son
# temps.






































print('\033[92m✓ OK' if average == 10.4 else '\033[91m❌KO')
