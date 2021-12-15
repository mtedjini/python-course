# Le but de cet exercice est de créer une classe Pokemon et trois classes
# Bulbasaur, Charmander & Squirtle

# 1) LA CLASSE PARENTE

# Le type Attack mentionné ci-après possède les attributs suivants :
# - name (str)
# - damage (int)

# La classe Pokémon respecte les contraintes suivantes :
# - attribut _name (str, le seul attribut passé en paramètre)
# - attribut _type (str, aucune valeur pour le moment)
# - attribut _life_points (int, aucune valeur pour le moment)
# - attribut _attack (dictionnaire de type Attack, aucune valeur pour le moment)
# - méthode get_name(self) qui renvoit le nom
# - méthode get_type(self) qui renvoit le type
# - méthode is_ok(self) qui renvoit true si les points de vie sont positifs
# - méthode take_damage(self, damage: int) qui retire des points de vie (mais
# sans aller en dessous de 0)
# - méthode fight(self, opponent: 'Pokemon') qui prend en paramètre un autre
# Pokemon # et appelle sa fonction take_damage en fonction de la puissance de
# l'attaque (le type 'Pokemon' est bien entre quotes, c'est un cas particulier
# d'auto-référence)

# 2) LES TROIS POKEMONS

# Trois classes vont hériter de Pokemon. Attention, on parle bien de classes
# et pas encore d'instances de classes ! Celles-ci seront créées plus tard.

# La classe Bulbasaur hérite de la classe Pokemon avec les valeurs suivantes :
# _name: passé à __init__ (chaque individu peut avoir un nom différent)
# _type: grass
# _life_points: 40
# _attack: {"name": "Leech Seed", "damage": 20}
# Surchargez la méthode take_damage : ce pokémon est résistant, retirez 5 à la
# valeur de chaque attaque qui lui est infligée.

# La classe Charmander hérite de la classe Pokemon avec les valeurs suivantes :
# _name: passé à __init__ (chaque individu peut avoir un nom différent)
# _type: fire
# _life_points: 50
# _attack: {"name": "Ember", "damage": 30}
# Surchargez la méthode fight : si la cible est de type "grass", on ajoute +10
# aux dégats.

# La classe Squirtle hérite de la classe Pokémon avec les valeurs suivantes :
# _name: passé à __init__ (chaque individu peut avoir un nom différent)
# _type: water
# _life_points: 40
# _attack: {"name": "Bubble", "damage": 15}
# Surchargez la méthode fight : si la cible est de type "fire", les dégats
# sont doublés.

# 3) INSTANCES

# Vous pouvez désormais créer des instances de Pokemon ainsi :
# bulby = Bulbasaur("Bulby")

# Pokemon est une "classe abstraite" : on ne doit pas l'instancier directement,
# elle sert juste de plan aux trois autres.

# 4 ) LE COMBAT

# Écrivez une méthode fight(pokemon_1: Pokemon, pokemon_2: Pokemon) qui simule
# un combat entre deux Pokemon et renvoit le Pokemon gagnant.

# Le pokemon passé en premier à la fonction est le premier à attaquer.
# Les deux pokemons s'attaquent à tour de rôle jusqu'à ce que l'un d'eux soit
# KO.

# Ajoutez des prints() pour suivre toute l'intensité de la bataille.

# Bonne chance !

################################################################################
from os import name
from typing import TypedDict

class Attack(TypedDict):
  name : str
  damage : int

class Pokemon:
    array = []
    def __init__(self, name : str):
        self._name = name
        self._type = ""
        self._life_points = 0
        self._attack : Attack
    
    def get_name(self):
      return self._name

    def get_type(self):
      return self._type

    def is_ok(self):
      return (self._life_points > 0)

    def take_damage(self, damage : int):
      self._life_points = max(self._life_points - damage, 0)
      print(self._name + " recoit " + str(damage) + " de dommage, il lui reste " + str(self._life_points) + " de point de vie")
    
    def fight(self, opponent: 'Pokemon'):
      print(self._name + " utilise " + self._attack["name"])
      opponent.take_damage(self._attack["damage"])


class Bulbasaur(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self._type = "grass"
        self._life_points = 40
        self._attack = {"name": "Leech Seed", "damage": 20}

    def take_damage(self, damage: int):
        return super().take_damage(damage-5)

class Charmander(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self._type = "fire"
        self._life_points = 50
        self._attack = {"name": "Ember", "damage": 30}

    def fight(self, opponent: 'Pokemon'):
        if opponent._type == "grass":
          self._attack["damage"] += 10
          super().fight(opponent)
          self._attack["damage"] -= 10
        else :
          return super().fight(opponent)

class Squirtle(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self._type = "water"
        self._life_points = 40
        self._attack = {"name": "Bubble", "damage": 15}

    def fight(self, opponent: 'Pokemon'):
        if opponent._type == "fire":
          self._attack["damage"] = self._attack["damage"] * 2
          super().fight(opponent)
          self._attack["damage"] = self._attack["damage"] // 2
        else :
          return super().fight(opponent)

bulby = Bulbasaur("Bulby")
chary = Charmander("Chary")
squity = Squirtle("Squity")

# 4 ) LE COMBAT

# Écrivez une méthode fight(pokemon_1: Pokemon, pokemon_2: Pokemon) qui simule
# un combat entre deux Pokemon et renvoit le Pokemon gagnant.

# Le pokemon passé en premier à la fonction est le premier à attaquer.
# Les deux pokemons s'attaquent à tour de rôle jusqu'à ce que l'un d'eux soit
# KO.

# Ajoutez des prints() pour suivre toute l'intensité de la bataille.

def fight(pokemon_1: Pokemon, pokemon_2: Pokemon):
  print("Pokemon 1 : " + pokemon_1.get_name() + " " + str(pokemon_1._life_points) + " de point de vie")
  print("Pokemon 2 : " + pokemon_2.get_name() + " " + str(pokemon_2._life_points) + " de point de vie")
  while pokemon_1.is_ok() and pokemon_2.is_ok():
      pokemon_1.fight(pokemon_2)
      if pokemon_2.is_ok() == False:
        print("Winner : " + pokemon_1.get_name())
        return pokemon_1
      pokemon_2.fight(pokemon_1)
      if pokemon_1.is_ok() == False:
        print("Winner : " + pokemon_2.get_name())
        return pokemon_2
################################################################################
























print('\033[92m✓ OK' if isinstance(fight(Squirtle("Squity"), Charmander("Chary")), Squirtle)
  and isinstance(fight(Charmander("Chary"), Squirtle("Squity")), Charmander)
  and isinstance(fight(Squirtle("Squity"), Bulbasaur("Bulby")), Bulbasaur)
  and isinstance(fight(Bulbasaur("Bulby"), Squirtle("")), Bulbasaur)
  and isinstance(fight(Charmander("Chary"), Bulbasaur("Bulby")), Charmander)
  and isinstance(fight(Bulbasaur("Bulby"), Charmander("Chary")), Charmander) else '\033[91m❌KO')
