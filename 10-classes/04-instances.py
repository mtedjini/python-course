# À partir d'une classe, on peut créer autant d'instances que l'on souhaite,
# chacune est un objet séparé. Ces objets peuvent être manipulés comme des
# variables (à vrai dire, ce sont des variables !).

# Reprenez votre classe User.

# En dehors de la classe, créez une fonction get_oldest(). Cette fonction doit
# prendre deux instances de la classe User en paramètre, et renvoyer le
# fullname (prénom + nom) de l'utilisateur le plus vieux
# (on ignore le cas où les âges sont égaux).

################################################################################
class User:
    array = []
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.followers = 0
    
    def get_full_name(self):
        return self.firstname + " " + self.lastname
    
    def is_adult(self):
        return (self.age>=18)
    
    def add_followers(self, followers):
        if User.is_adult(self):
            self.followers += followers
            return self.followers

def get_oldest(user_one : User, user_two : User):
    if user_one.age > user_two.age:
        return user_one.get_full_name()
    elif user_one.age == user_two.age:
        return None
    else:
        return user_two.get_full_name()

################################################################################

# N'oubliez pas le typage. Une classe est également un type, ce qui est bien
# pratique.
















test_adult = User("bob", "doe", 18)
test_child = User("child", "doe", 10)
print('\033[92m✓ OK' if get_oldest(test_adult, test_child) == "bob doe" else '\033[91m❌KO')