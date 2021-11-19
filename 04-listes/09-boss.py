# Créez une fonction "compute_notes" prenant en paramètre une notese de notes
# et un index : compute_notes([16, 13, 9, 12], 2)

# L'index représente la séparation entre le premier et le second semestre.
# Dans l'exemple, 16 et 13 sont les notes du premier semestre.

# Si l'index ne permet pas de séparer correctement le tableau, la fonction
# retourne un tableau vide.

# Le but de cette fonction est de faire ne sorte qu'un étudiant n'ait pas un
# semestre ne contenant que des zéros.

# Si un des deux semestres ne contient pas d'autre note que des zéros, on 
# rajoute à ce semestre une unique note : la plus basse (sans compter les
# zéros !) de l'autre semestre. On renvoit ensuite le tableau des notes modifié.

# Si aucun des deux semestres n'est concerné, on retourne le tableau sans 
# modification.

# Si les deux semestres ne contiennent que des zéros, on retourne le tableau
# sans modification.

# Exemple : compute_notes([16, 13, 9, 0, 0], 3) -> [16, 13, 9, 0, 0, 9]

################################################################################
def compute_notes1(notes : list[int], index : int):
    if max(notes) == 0 :
        return notes
    else :
        premier_semestre = notes[ : index]
        deuxieme_semestre = notes[index : ]

        if max(premier_semestre) == 0:
            notes.insert(index-1, max(deuxieme_semestre))
            return notes
        elif max(deuxieme_semestre) == 0:
            notes.append(max(premier_semestre))
            return notes

def compute_notes(notes_list: list[int], semester_2_index : int) -> list[int] :
    if semester_2_index >= len(notes_list) or semester_2_index <=0:
        return []
    
    if max(notes_list) == 0:
        return notes_list
    
    semester1: list[int] = notes_list[: semester_2_index]
    semester2: list[int] = notes_list[semester_2_index :]

    if max(semester1) == 0:
        semester1.append(max(semester2))
    elif max(semester1) == 0:
        semester2.append(max(semester1))
    
    return semester1 + semester2
################################################################################

































print('\033[92m✓ OK' if compute_notes([10, 12, 8], 3) == [] and compute_notes([10, 8, 9, 15, 0], 4) == [10, 8, 9, 15, 0, 15] and compute_notes([0, 10, 8], 1) == [0, 10, 10, 8] and compute_notes([0, 0], 1) == [0, 0] and compute_notes([0, 0, 3], 2) == [0, 0, 3, 3] else '\033[91m❌KO')
