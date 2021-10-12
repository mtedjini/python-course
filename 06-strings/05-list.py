# Une chaîne est un tableau de caractères. Les mêmes opérations sont donc 
# possibles que sur une liste !

# Créez une fonction is_valid_time() qui prend en paramètre un temps au format
# "HH:mm" et qui retourne True si le format est valide et si l'heure existe.

################################################################################

################################################################################





































print('\033[92m✓ OK' if is_valid_time('23:59') and is_valid_time('00:00') and not is_valid_time('2:4') and not is_valid_time('25:00') and not is_valid_time('ab:cd') else '\033[91m❌KO')

