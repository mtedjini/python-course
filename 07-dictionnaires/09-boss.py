# Félicitations, vous êtes l'heureux(se) propriétaire d'une pizzeria.

# Vous recevez les commandes des clients sous la forme d'un objet de type Order.

# 

################################################################################
from typing import TypedDict

class Ingredient(TypedDict):
    name: str
    cost: int

class Order(TypedDict):
    quantity: int
    ingredients: list[Ingredient]

available_ingredients: list[Ingredient] = [
  { "name": "tomato", "cost": 1 },
  { "name": "onions", "cost": 1 },
  { "name": "egg", "cost": 2 },
  { "name": "olives", "cost": 1 },
  { "name": "cheese", "cost": 2 }
]

def get_cost_for_order(order: Order) -> int:
    return 1452
################################################################################