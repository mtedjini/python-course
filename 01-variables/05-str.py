# Encore une fois, les types ne se mélangent pas.

# Votre but est de créer une variable "presentation" contenant la phrase
# "Patrick Sébastien est né en 1953" en utilisant les variables ci-dessous.

# Pour que python accepte, il faudra convertir 1953 en chaîne grâce à la
# fonction str().

# Exemple : str(2022) -> "2022"

################################################################################
first_name: str = "Patrick"
last_name: str = "Sébastien"
birth_year: int = 1953
################################################################################

print(presentation)




































print('\033[92m✓ OK' if presentation == "Patrick Sébastien est né en 1953" else '\033[91m❌KO')
