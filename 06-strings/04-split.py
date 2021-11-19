# Il est pratique de pouvoir séparer une chaîne en plusieurs sous-chaînes en
# fonction d'un séparateur.

# L'opération split() le permet et renvoit un tableau contenant les différentes
# chaînes.

# "one-two-three".split('-') -> ["one", "two", "three"]

# join() permet l'opération inverse :

# '-'.join(["one", "two", "three"]) -> "one-two-three"

# Transformez la liste des ingrédients en tableau, retirez le fromage, et
# reformatez la chaîne ainsi : "tomato ~ lettuce ~ pickles"

################################################################################
ingredients: str = "tomato, cheese, lettuce, pickles"

list_of_ingedients : list[str] = ingredients.split(',')
print(list_of_ingedients)
#list_of_ingedients.remove("cheese")
print(list_of_ingedients)

ingredients : str = ' ~'.join(list_of_ingedients)
print(ingredients)
################################################################################



























print('\033[92m✓ OK' if ingredients == "tomato ~ lettuce ~ pickles" else '\033[91m❌KO')
