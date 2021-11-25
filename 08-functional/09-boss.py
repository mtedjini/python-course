# ÉTAPE 1
# Vous devez générer une liste "discount_products" qui contiendra uniquement
# les produits discount.
# Pour ces produits, vous devrez ajouter une clé "discount_cost" dont la valeur
# sera calculée en fonction du coût et de la réduction
# Exemple : -25% sur le tournevis, donc discount_cost = 3

# ÉTAPE 2
# Un client commande vos deux articles en promotion.
# Créez un dictionnaire "order" de type Order (type à créer) contenant les clés
# total_cost et total_discount_cost qui sont deux entiers.
# Calculez dans ce dictionnaire le total des articles, avec le prix original
# et le prix discount.

from typing import TypedDict

class Product(TypedDict, total=False):
    name: str
    cost: float
    discount: float
    discount_cost: float

products: list[Product] = [
  {
    "name": "Aspi Turbo Max",
    "cost": 150,
    "discount": 50
  },
  {
    "name": "Tournevis",
    "cost": 4,
    "discount": 25
  },
  {
    "name": "Marteau",
    "cost": 10
  }
]

################################################################################
import functools
#correction:
def add_discount_cost(product : Product) -> Product:
  if "discount" in product and "cost" in product:
    product["discount_cost"] = product["cost"] - (product["cost"] * (product["discount"] /100))
  return product

class Order(TypedDict):
  total_cost: float
  total_discount_cost : float

def add_product(order : Order, product : Product) -> Order:
  if "cost" in product and "discount_cost" in product:
    order["total_cost"] += product["cost"]
    order["total_discount_cost"] += product["discount_cost"]
  return order

#Etape 1:
discount_products : list[Product] = list(filter(lambda product: "discount" in product, products))
discount_products = list(map(add_discount_cost, products))


#Etape 2:
order : Order = {
  "total_cost" : 0,
  "total_discount_cost" : 0,
}

functools.reduce(add_product, discount_products, order)
print(order)
#test
# def get_discount_cost(product : Product) -> float:
#   if product["discount"] in product:
#     return product["cost"]*100-product["discount"])/100

# discount_products : list[Product] = map(get_discount_cost, products)

# class Order(TypedDict):
#   total_cost: float
#   total_discount_cost : float

# order : Order = 
################################################################################

# Lorsqu'on travaille avec des types aux propriétés optionnelles (voir
# total=False dans le type Product), il faut vérifier l'existence d'une
# propriété avant de s'en servir.

























print('\033[92m✓ OK' if len(discount_products) == 2 and discount_products[0]['discount_cost'] == 75.0 and discount_products[1]['discount_cost'] == 3.0 and order['total_cost'] == 154 and order['total_discount_cost'] == 78 else '\033[91m❌KO')
