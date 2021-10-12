# Créez une fonction is_valid_password() qui prend en paramètre une chaîne de
# caractère et qui vérifie si le mot de passe est valide selon les critères
# suivants :

# Le mot de passe fait au moins 6 caractères
# Il contient au moins une lettre minuscule
# Il contient au moins une lettre majuscule
# Il contient au moins deux chiffres
# Il ne contient pas d'autre type de caractère (car notre base de données ne sait pas les gérer)

# La fonction doit renvoyer un booléen.

################################################################################

################################################################################

# Pour simplifier vos test, utilisez input() et "while True" afin de pouvoir
# tester plusieurs entrées d'affilée.















































print('\033[92m✓ OK' if is_valid_password('1E4a2E') and not is_valid_password('1E8a2') and not is_valid_password('1EDA2E') and not is_valid_password('1eda2e') and not is_valid_password('sedEfe') and not is_valid_password('sedEf!') and not is_valid_password('sedEf7') else '\033[91m❌KO')
