# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:04:10 2023

@author: youssef el aidoudi
"""
import random
import turtle

########################## FONCTIONS DE GÉNÉRATION DE LABYRINTHE ############################

def somme_liste(input):
    my_sum = 0
    for lig in input:
        my_sum += sum(lig)
    return my_sum

def generer_labyrinthe(taille_x, taille_y):
    # Crée une matrice pour représenter le labyrinthe avec tous les murs intacts
    Murs = [[[1, 1, 1, 1] for a in range(taille_x)] for b in range(taille_y)]
    x = 0
    y = 0
    somme_visite = 0
    noeud_courant = [x, y]
    # Matrice pour marquer les cellules visitées pendant la génération
    visite = [[0 for a in range(taille_x)] for b in range(taille_y)]
    visite[x][y] = 1
    visite_noeuds = [[x, y]]
    n = 0
    # Boucle principale pour générer le labyrinthe
    while somme_visite != (taille_x * taille_y):  # Vérifie si terminé
        options = [0, 0, 0, 0]
        # Vérifie si les murs peuvent être retirés dans les directions possibles
        if x != 0:
            if visite[y][x - 1] == 0:
                options[0] = 1  # Le mur peut être retiré à gauche
        if y != taille_y - 1:
            if visite[y + 1][x] == 0:
                options[1] = 1  # Le mur peut être retiré au-dessus
        if x != taille_x - 1:
            if visite[y][x + 1] == 0:
                options[2] = 1  # Le mur peut être retiré à droite
        if y != 0:
            if visite[y - 1][x] == 0:
                options[3] = 1  # Le mur peut être retiré en dessous

        if options == [0, 0, 0, 0]:
            # Si aucune direction possible, revient à la cellule précédente
            noeud_courant = visite_noeuds[n - 1]
            x = noeud_courant[0]
            y = noeud_courant[1]
            n = n - 1
        else:
            # S'il y a des directions possibles, choisit aléatoirement
            noeud_trouve = False
            while not noeud_trouve:
                random_int = random.randint(0, 3)
                if options[random_int] == 1:
                    if random_int == 0:
                        direction_opposee = [noeud_courant[0] - 1, noeud_courant[1]]  # Se déplace dans la cellule à gauche
                        Murs[noeud_courant[1]][noeud_courant[0]][0] = 0  # Retire le mur à gauche
                        Murs[direction_opposee[1]][direction_opposee[0]][2] = 0
                    elif random_int == 1:
                        direction_opposee = [noeud_courant[0], noeud_courant[1] + 1]  # Se déplace dans la cellule au-dessus
                        Murs[noeud_courant[1]][noeud_courant[0]][1] = 0  # Retire le mur au-dessus
                        Murs[direction_opposee[1]][direction_opposee[0]][3] = 0
                    elif random_int == 2:
                        direction_opposee = [noeud_courant[0] + 1, noeud_courant[1]]  # Se déplace dans la cellule à droite
                        Murs[noeud_courant[1]][noeud_courant[0]][2] = 0  # Retire le mur à droite
                        Murs[direction_opposee[1]][direction_opposee[0]][0] = 0
                    else:
                        direction_opposee = [noeud_courant[0], noeud_courant[1] - 1]  # Se déplace dans la cellule en dessous
                        Murs[noeud_courant[1]][noeud_courant[0]][3] = 0  # Retire le mur en dessous
                        Murs[direction_opposee[1]][direction_opposee[0]][1] = 0
                    n = n + 1
                    visite_noeuds.insert(n, direction_opposee)
                    noeud_courant = direction_opposee
                    visite[noeud_courant[1]][noeud_courant[0]] = 1
                    x = noeud_courant[0]
                    y = noeud_courant[1]
                    noeud_trouve = True
        somme_visite = somme_liste(visite)
    return Murs


def afficher_labyrinthe(taille_x, taille_y, Murs):
    # Définir les paramètres de départ pour dessiner le labyrinthe avec la bibliothèque Turtle
    startx = -380
    starty = -startx
    taille_case = (2 * (-startx)) / taille_x
    
    # Effacer l'écran de Turtle
    turtle.clear()
    
    # Configurer la vitesse du dessin
    turtle.speed(0)
    
    # Positionner la tortue au coin supérieur gauche du labyrinthe
    turtle.penup()
    turtle.goto(startx, starty)
    
    # Dessiner le contour du labyrinthe
    turtle.pendown()
    turtle.goto(-startx, starty)
    turtle.goto(-startx, -starty)
    
    # Orienter la tortue vers la droite
    turtle.setheading(0)
    
    # Parcourir les lignes du labyrinthe
    for y in range(taille_x):
        turtle.penup()
        # Positionner la tortue au début de la ligne
        turtle.goto(startx, -starty + taille_case * (y))
        # Parcourir les colonnes de la ligne
        for x in range(taille_y):
            # Dessiner un mur s'il est présent
            if Murs[y][x][3] == 1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(taille_case)
    
    # Orienter la tortue vers le haut
    turtle.left(90)
    
    # Parcourir les colonnes du labyrinthe
    for x in range(taille_x):
        turtle.penup()
        # Positionner la tortue au début de la colonne
        turtle.goto(startx + taille_case * (x), -starty)
        # Parcourir les lignes de la colonne
        for y in range(taille_y):
            # Dessiner un mur s'il est présent
            if Murs[y][x][0] == 1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(taille_case)







################################## FONCTIONS DIJKSTRA ##################################

def noeud_oppose(b, noeud_courant):
    # Fonction pour obtenir les coordonnées du noeud opposé à partir de la direction b
    if b == 0:
        # Si la direction est à gauche, déplace le noeud vers la gauche
        noeud_oppose = [noeud_courant[0] - 1, noeud_courant[1]]
    elif b == 1:
        # Si la direction est vers le haut, déplace le noeud vers le haut
        noeud_oppose = [noeud_courant[0], noeud_courant[1] + 1]
    elif b == 2:
        # Si la direction est à droite, déplace le noeud vers la droite
        noeud_oppose = [noeud_courant[0] + 1, noeud_courant[1]]
    else:
        # Si la direction est vers le bas, déplace le noeud vers le bas
        noeud_oppose = [noeud_courant[0], noeud_courant[1] - 1]
    
    return noeud_oppose


def recherche_Dijkstra(Murs, tailley, taillex):
    visite = [[0 for a in range(taillex)] for b in range(tailley)]
    visite[0][0] = 1  # Commence en bas à gauche avec 1
    noeuds_courants = [[0, 0]]
    nouveau = True
    while nouveau == True:
        nouveau = False
        for a in range(len(noeuds_courants)):  # recherche à tous les nœuds/cellules courants
            noeud_courant = noeuds_courants[0]
            for b in range(4):  # vérifie toutes les 4 directions possibles
                if Murs[noeud_courant[1]][noeud_courant[0]][b] == 0:  # vérifie le mur
                    noeud_autre_cote = noeud_oppose(b, noeud_courant)
                    if visite[noeud_autre_cote[1]][noeud_autre_cote[0]] == 0:  # vérifie s'il n'a pas été visité
                        visite[noeud_autre_cote[1]][noeud_autre_cote[0]] = visite[noeud_courant[1]][noeud_courant[0]] + 1
                        noeuds_courants.append(noeud_autre_cote)  # ajoute le nouveau nœud à la liste des nœuds courants
                        nouveau = True
            noeuds_courants.remove(noeud_courant)  # supprime le nœud précédemment à car il a été recherché
    return visite

def chemin_Dijkstra(visite, taillex, tailley, Murs):
    # Fonction pour récupérer les coordonnées du chemin le plus court trouvé par l'algorithme de Dijkstra
    
    # Initialisation des variables avec la distance totale et les coordonnées du point de départ
    distance = visite[taillex - 1][tailley - 1]
    coordonnees_chemin = [[taillex - 1, tailley - 1]]  # définit la fin en haut à droite
    
    # Parcourt le chemin à rebours en remontant depuis la fin jusqu'au début
    while coordonnees_chemin[0] != [0, 0]:
        # Vérifie si la case à gauche n'a pas de mur et que la distance est correcte
        if Murs[coordonnees_chemin[0][1]][coordonnees_chemin[0][0]][0] == 0:
            if visite[coordonnees_chemin[0][1]][coordonnees_chemin[0][0] - 1] == distance - 1:
                coordonnees_chemin.insert(0, [coordonnees_chemin[0][0] - 1, coordonnees_chemin[0][1]])
                distance = distance - 1
        
        # Vérifie si la case en haut n'a pas de mur et que la distance est correcte
        if Murs[coordonnees_chemin[0][1]][coordonnees_chemin[0][0]][1] == 0:
            if visite[coordonnees_chemin[0][1] + 1][coordonnees_chemin[0][0]] == distance - 1:
                coordonnees_chemin.insert(0, [coordonnees_chemin[0][0], coordonnees_chemin[0][1] + 1])
                distance = distance - 1
        
        # Vérifie si la case à droite n'a pas de mur et que la distance est correcte
        if Murs[coordonnees_chemin[0][1]][coordonnees_chemin[0][0]][2] == 0:
            if visite[coordonnees_chemin[0][1]][coordonnees_chemin[0][0] + 1] == distance - 1:
                coordonnees_chemin.insert(0, [coordonnees_chemin[0][0] + 1, coordonnees_chemin[0][1]])
                distance = distance - 1
        
        # Vérifie si la case en bas n'a pas de mur et que la distance est correcte
        if Murs[coordonnees_chemin[0][1]][coordonnees_chemin[0][0]][3] == 0:
            if visite[coordonnees_chemin[0][1] - 1][coordonnees_chemin[0][0]] == distance - 1:
                coordonnees_chemin.insert(0, [coordonnees_chemin[0][0], coordonnees_chemin[0][1] - 1])
                distance = distance - 1
    
    # Retourne les coordonnées du chemin
    return coordonnees_chemin


def afficher_chemin(coordonnees_chemin, startx, starty, taillegrille):
    # Fonction pour afficher le chemin trouvé en utilisant la bibliothèque Turtle
    
    # Configurer la vitesse de dessin de la tortue
    turtle.speed(0)
    
    # Lever le stylo de la tortue pour se déplacer sans dessiner
    turtle.penup()
    
    # Calculer les coordonnées de départ au centre de la première case
    x = startx + taillegrille / 2
    y = starty + taillegrille / 2
    
    # Positionner la tortue au point de départ
    turtle.goto(x, y)
    
    # Abaisser le stylo de la tortue pour commencer le dessin
    turtle.pendown()
    
    # Définir l'épaisseur du trait en fonction de la taille de la grille
    turtle.pensize(taillegrille / 2)
    
    # Définir la couleur du trait à rouge
    turtle.color("red")
    
    # Parcourir les coordonnées du chemin et dessiner le chemin
    for a in range(len(coordonnees_chemin) - 1):
        # Calculer les nouvelles coordonnées en fonction du déplacement entre les points successifs
        x = x + (coordonnees_chemin[a + 1][0] - coordonnees_chemin[a][0]) * taillegrille
        y = y + (coordonnees_chemin[a + 1][1] - coordonnees_chemin[a][1]) * taillegrille
        
        # Déplacer la tortue vers les nouvelles coordonnées pour dessiner la ligne du chemin
        turtle.goto(x, y)


#def point_a_xy(x, y, taillegrille, startx, starty, taillex, couleur):
#    turtle.penup()
 #   turtle.goto(startx + taillegrille / 2 + x * taillegrille, starty + taillegrille / 2 + y * taillegrille)
 #   turtle.pendown()
#    turtle.pencolor((0, 0.99 - couleur / (taillex * taillex), 0))
 #   turtle.pensize(taillegrille / 2)
   
taillex = 20
tailley = 20
startx = -380
starty = startx
taillegrille = (2 * (-starty)) / tailley
# Définition de la taille du labyrinthe, de la position de départ et de la taille de la cellule
# Détermination de la taille d'une cellule dans le labyrinthe
taille_case = (2 * (-starty)) / tailley

### Génération du labyrinthe
Murs = generer_labyrinthe(taillex, tailley)

# Affichage du labyrinthe généré
afficher_labyrinthe(taillex, tailley, Murs)

# Recherche du chemin le plus court dans le labyrinthe
visite = recherche_Dijkstra(Murs, tailley, taillex)

# Récupération des coordonnées du chemin le plus court
coordonnees_chemin = chemin_Dijkstra(visite, taillex, tailley, Murs)

# Affichage du chemin le plus court sur le labyrinthe
afficher_chemin(coordonnees_chemin, startx, starty, taille_case)

# Boucle principale de Turtle pour maintenir la fenêtre ouverte
turtle.mainloop()
