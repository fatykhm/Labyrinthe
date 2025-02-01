# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:18:02 2023

@author: youssef el aidoudi
"""

import random
import turtle

# Définition de la fonction qui calcule la somme des éléments d'une liste bidimensionnelle
def somme_liste(input):
    my_sum = 0
    for lig in input:
        my_sum += sum(lig)
    return my_sum

# Définition de la fonction qui génère le labyrinthe
def generer_labyrinthe(taillex, tailley):
    # Création d'une matrice représentant le labyrinthe avec tous les murs intacts
    Murs = [[[1, 1, 1, 1] for a in range(taillex)] for b in range(tailley)]
    x = 0
    y = 0
    somme_visite = 0
    noeud_courant = [x, y]
    
    # Matrice pour marquer les cellules visitées pendant la génération
    visite = [[0 for a in range(taillex)] for b in range(tailley)]
    visite[x][y] = 1
    visite_noeuds = [[x, y]]
    n = 0
    
    # Boucle principale pour générer le labyrinthe
    while somme_visite != (taillex * tailley):  # Vérifie si terminé
        options = [0, 0, 0, 0]
        
        # Vérifie si les murs peuvent être retirés dans les directions possibles
        if x != 0:
            if visite[y][x - 1] == 0:
                options[0] = 1  # Le mur peut être retiré à gauche
        if y != tailley - 1:
            if visite[y + 1][x] == 0:
                options[1] = 1  # Le mur peut être retiré au-dessus
        if x != taillex - 1:
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

# Définition de la fonction pour afficher le labyrinthe
# Fonction pour afficher le labyrinthe
def afficher_labyrinthe(taillex, tailley, Murs):
    # Définition des coordonnées de départ et de la taille des cases
    startx = -380
    starty = -startx
    taille_case = (2 * (-startx)) / taillex
    
    # Nettoie l'écran et initialise la tortue
    turtle.clear()
    turtle.speed(0)
    
    # Positionne la tortue pour dessiner les bords du labyrinthe
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.pendown()
    turtle.goto(-startx, starty)
    turtle.goto(-startx, -starty)
    turtle.setheading(0)
    
    # Boucle pour dessiner les murs horizontaux
    for y in range(taillex):
        turtle.penup()
        turtle.goto(startx, -starty + taille_case * (y))
        for x in range(tailley):
            if Murs[y][x][3] == 1:
                turtle.pendown()  # Dessine le mur s'il est présent
            else:
                turtle.penup()  # Lève le stylo s'il n'y a pas de mur
            turtle.forward(taille_case)
    
    # Change la direction de la tortue pour dessiner les murs verticaux
    turtle.left(90)
    
    # Boucle pour dessiner les murs verticaux
    for x in range(taillex):
        turtle.penup()
        turtle.goto(startx + taille_case * (x), -starty)
        for y in range(tailley):
            if Murs[y][x][0] == 1:
                turtle.pendown()  # Dessine le mur s'il est présent
            else:
                turtle.penup()  # Lève le stylo s'il n'y a pas de mur
            turtle.forward(taille_case)


# Définition de la fonction pour ajuster la direction
def ajuster_cap(direction, binaryvalue):
    binarynew = [0, 0, 0, 0]
    for a in range(4):
        binaryvalue.append(binaryvalue[a])
    binarynew[0] = binaryvalue[direction + 3]
    binarynew[1] = binaryvalue[direction]
    binarynew[2] = binaryvalue[direction + 1]
    binarynew[3] = binaryvalue[direction + 2]
    return binarynew

# Définition de la fonction pour suivre le mur
# Fonction pour suivre le mur dans le labyrinthe
def suivre_mur(Murs):
    # Initialisation de la tortue pour commencer au milieu de la première case
    turtle.penup()
    turtle.goto(startx + taillegrille / 2, starty + taillegrille / 2)
    turtle.pendown()
    
    # Configuration de la taille et de la couleur du stylo pour représenter le mur à suivre
    turtle.pensize(taillegrille / 4)
    turtle.color("black")
    
    # Orientation initiale de la tortue vers le haut
    turtle.setheading(90)
    
    # Initialisation des coordonnées et de la direction
    x = 0
    y = 0
    direction = 1
    
    # Boucle pour suivre le mur jusqu'à atteindre la sortie
    while x != (taillex - 1) or y != (0):
        direction_murs = ajuster_cap(direction, Murs[y][x])
        
        # Ajuste la direction de la tortue en fonction des murs autour
        if direction_murs[0] == 0:
            turtle.left(90)
            direction = direction - 1
        elif direction_murs[1] == 0:
            turtle.right(0)
        elif direction_murs[2] == 0:
            turtle.right(90)
            direction = direction + 1
        else:
            turtle.right(180)
            direction = direction + 2
        
        # Ajuste la direction si elle dépasse les limites
        if direction == -1:
            direction = 3
        if direction > 3:
            direction = direction - 4
        
        # Mise à jour des coordonnées en fonction de la direction
        if direction == 1:
            y = y + 1
        elif direction == 2:
            x = x + 1
        elif direction == 3:
            y = y - 1
        else:
            x = x - 1
        
        # Avance la tortue d'une case
        turtle.forward(taillegrille)


# Paramètres du labyrinthe
taillex = 25
tailley = taillex
startx = -380
starty = startx
taillegrille = (2 * (-starty)) / tailley

# Génération du labyrinthe
Murs = generer_labyrinthe(taillex, tailley)

# Affichage du labyrinthe
afficher_labyrinthe(taillex, tailley, Murs)

# Suivi du mur dans le labyrinthe
suivre_mur(Murs)

# Maintien de la fenêtre turtle ouverte
turtle.mainloop()
