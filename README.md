# Jeu-de-la-vie
Implémentation en Python du Jeu de la Vie, le célèbre automate cellulaire mathématique conçu par John Horton Conway en 1970.

# Les règles
> si la cellule vis
    > si les parmis les cellules autours 2 ou 3 sont en vie alors la cellules vie.
    > mais si le nombre de cellules en vie autours de la cellules est inférieur à deux ou supérieur à 3 alors elle meurt
> mais si la cellule ne vie pas
    > si le nombre de cellule en vie autour est exactement 3 alors elle prend vie
    > sinon elle reste morte

# Structure de la grille
tableau de i par i

# Calcule de l'état à la base des règles
On vérifi l'était de chaque cellule autour de celle sur lequel le curseur sera et on sauvegard son état futur puis on fait de même avec la cellule suivante. à la fin on appliqueq l'état suivant de toute les cellules puis on recommence le processuce.