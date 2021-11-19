# Il est pratiquement toujours nécessaire de vérifier que l'utilisateur a bien 
# entré une donnée dans le format attendu.

# En utilisant la boucle "while True" vue précédemment, demandez son âge à
# l'utilisateur. Si la donnée rentrée n'est pas valide (entier positif
# inférieur à 130), demandez à nouveau, jusqu'à ce qu'elle le soit.

# Pas de correction automatique pour cet exercice.

################################################################################
is_correct_age : bool = True
while is_correct_age :
    print("Quel est votre âge ?")
    age = input()
    if int(age) >= 0 and int(age) <= 130 :
        is_correct_age = False
    else :
        is_correct_age = True
################################################################################