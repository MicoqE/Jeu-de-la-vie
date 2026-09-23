import numpy as np

def init_grille(largeur, hauteur):
    return np.random.choice([True, False], size=(largeur, hauteur))
    
grille = init_grille(5, 5)

# Algorythme de comptage des voisins
"""
pour di dans [-1, 0, 1] :
    pour dj dans [-1, 0, 1] :
        si di == 0 et dj == 0 : ignorer (c'est la cellule elle-même)
        si i+di et j+dj sont dans les limites de la grille :
            compter ce voisin s'il est vivant
"""

def compter_voisins(grille, i, j):
    nb = 0 # Nombre de voisin vivant
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                pass
            elif 0 <= i+di < len(grille) and 0 <= j+dj < len(grille[i]):
                if grille[di+i][dj+j]:
                    nb += 1
    return nb

def etape_suivante(grille):
    grille_futur = np.full(grille.shape, None)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            voisin = compter_voisins(grille, i, j)
            if grille[i][j] == True:
                if voisin == 2 or voisin == 3:
                    grille_futur[i][j] = True
                else:
                    grille_futur[i][j] = False
            else:
                if voisin == 3:
                    grille_futur[i][j] = True
                else:
                    grille_futur[i][j] = False
    return grille_futur
            
print(grille)
print(etape_suivante(grille))