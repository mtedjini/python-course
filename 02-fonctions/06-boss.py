# Créez une fonction add() prenant en paramètres deux nombres et retournant leur
# somme.

# En une seule ligne supplémentaire, stockez dans une variable "result"
# l'addition de 10, 4, 6 et 7

################################################################################
def add(x: float, y: float) -> float:
    return x+y

result: float = add(10,4) + add(6,7)
################################################################################

print("Result :", result)









































print('\033[92m✓ OK' if result == 27 else '\033[91m❌KO')
