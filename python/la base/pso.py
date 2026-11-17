#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:13:43 2026

@author: yanis
"""

import random

# ------------------------------------------------------------------
# Données
# ------------------------------------------------------------------

# Figure 1 : 5 villes  (1=A, 2=B, 3=C, 4=D, 5=E)
# ATTENTION : les distances sont lues sur la figure, à vérifier avec l'énoncé
#            A  B  C  D  E
D5 = [[0, 2, 3, 3, 8],   # A
      [2, 0, 7, 8, 1],   # B
      [3, 7, 0, 4, 8],   # C
      [3, 8, 4, 0, 6],   # D
      [8, 1, 8, 6, 0]]   # E

# Matrice 9 x 9
D9 = [[0, 1, 2, 3, 4, 5, 6, 1, 7],
      [1, 0, 5, 4, 3, 6, 1, 9, 2],
      [2, 5, 0, 1, 6, 1, 9, 3, 7],
      [3, 4, 1, 0, 5, 9, 7, 2, 1],
      [4, 3, 6, 5, 0, 9, 1, 2, 1],
      [5, 6, 1, 9, 9, 0, 2, 1, 7],
      [6, 1, 9, 7, 1, 2, 0, 4, 5],
      [1, 9, 3, 2, 2, 1, 4, 0, 7],
      [7, 2, 7, 1, 1, 7, 5, 7, 0]]


# ------------------------------------------------------------------
# Fonction à minimiser : longueur du tour (retour à la ville de départ)
# ------------------------------------------------------------------
def longueur(X, D):
    total = 0
    i = 0
    while i < len(X) - 1:
        total = total + D[X[i] - 1][X[i + 1] - 1]
        i = i + 1
    # retour au sommet de départ
    total = total + D[X[len(X) - 1] - 1][X[0] - 1]
    return total


# ------------------------------------------------------------------
# Opérations sur les positions / vitesses
# ------------------------------------------------------------------

# Opération  (+)  vitesse (+) vitesse : concaténation
def somme_vitesses(V1, V2):
    res = []
    i = 0
    while i < len(V1):
        res.append(V1[i])
        i = i + 1
    i = 0
    while i < len(V2):
        res.append(V2[i])
        i = i + 1
    return res


# Opération  (+)  position (+) vitesse : on applique les échanges
# (a, b) = on échange les valeurs a et b dans la position
def position_plus_vitesse(X, V):
    res = []
    i = 0
    while i < len(X):
        res.append(X[i])
        i = i + 1

    k = 0
    while k < len(V):
        a = V[k][0]
        b = V[k][1]
        # on cherche où se trouvent a et b
        ia = 0
        ib = 0
        j = 0
        while j < len(res):
            if res[j] == a:
                ia = j
            if res[j] == b:
                ib = j
            j = j + 1
        # échange
        tmp = res[ia]
        res[ia] = res[ib]
        res[ib] = tmp
        k = k + 1
    return res


# Opération  (x)  réel k (x) vitesse V
def reel_fois_vitesse(k, V):
    res = []
    if k < 0:
        k = -k

    if k > 0 and k < 1:
        # on tronque : on garde floor(k * |V|) éléments
        nb = int(k * len(V))
        i = 0
        while i < nb:
            res.append(V[i])
            i = i + 1
    else:
        if k == int(k):
            # k entier : addition de vitesses (V + V + ... + V, k fois)
            i = 0
            while i < int(k):
                res = somme_vitesses(res, V)
                i = i + 1
        else:
            # k > 1 non entier : partie entière + partie décimale
            entier = int(k)
            decimal = k - entier
            res = reel_fois_vitesse(entier, V)
            res = somme_vitesses(res, reel_fois_vitesse(decimal, V))
    return res


# Opération  (-)  position (-) position : vitesse qui fait passer de X1 à X2
def position_moins_position(X1, X2):
    # copie de X1 pour ne pas la modifier
    copie = []
    i = 0
    while i < len(X1):
        copie.append(X1[i])
        i = i + 1

    V = []
    i = 0
    while i < len(copie):
        if copie[i] != X2[i]:
            a = copie[i]
            b = X2[i]
            V.append((a, b))
            # on échange les valeurs a et b dans la copie
            j = 0
            while j < len(copie):
                if copie[j] == a:
                    copie[j] = b
                elif copie[j] == b:
                    copie[j] = a
                j = j + 1
        i = i + 1
    return V


# ------------------------------------------------------------------
# Algorithme PSO
# ------------------------------------------------------------------
def pso(D, nb_particules, N):

    n = len(D)

    # Coefficients
    rho = 0.5
    b1 = 1.5
    b2 = 1.5

    # Positions initiales : on part du sommet 1, le reste est mélangé
    X = []
    V = []
    P = []
    i = 0
    while i < nb_particules:
        reste = []
        j = 2
        while j <= n:
            reste.append(j)
            j = j + 1
        random.shuffle(reste)
        pos = [1]
        j = 0
        while j < len(reste):
            pos.append(reste[j])
            j = j + 1

        X.append(pos)
        V.append([])          # vitesse nulle au départ
        P.append(pos)         # meilleure position personnelle
        i = i + 1

    # Meilleure position globale
    pg = P[0]
    i = 1
    while i < nb_particules:
        if longueur(P[i], D) < longueur(pg, D):
            pg = P[i]
        i = i + 1

    it = 0
    while it < N:

        i = 0
        while i < nb_particules:

            # V(k+1) = rho (x) Vk (+) b1 (x) (Pi (-) Xk) (+) b2 (x) (Pg (-) Xk)
            terme1 = reel_fois_vitesse(rho, V[i])
            terme2 = reel_fois_vitesse(b1, position_moins_position(X[i], P[i]))
            terme3 = reel_fois_vitesse(b2, position_moins_position(X[i], pg))
            V[i] = somme_vitesses(somme_vitesses(terme1, terme2), terme3)

            # X(k+1) = Xk (+) V(k+1)
            X[i] = position_plus_vitesse(X[i], V[i])

            # Mise à jour de la meilleure position personnelle
            if longueur(X[i], D) < longueur(P[i], D):
                P[i] = X[i]

            i = i + 1

        # Mise à jour de la meilleure position globale
        i = 0
        while i < nb_particules:
            if longueur(P[i], D) < longueur(pg, D):
                pg = P[i]
            i = i + 1

        it = it + 1

    return pg


# ------------------------------------------------------------------
# Tests des opérations (exemples du sujet)
# ------------------------------------------------------------------
print("=== Tests des opérations ===")
Vt = [(1, 2), (5, 4)]
Xt = [1, 2, 4, 3, 5]
print("X (+) V   =", position_plus_vitesse(Xt, Vt))      # [2, 1, 5, 3, 4]
print("V (+) V   =", somme_vitesses(Vt, Vt))             # [(1,2),(5,4),(1,2),(5,4)]
print("0.5 (x) V =", reel_fois_vitesse(0.5, Vt))         # [(1,2)]

X1 = [1, 2, 4, 3, 5]
X2 = [2, 4, 5, 3, 1]
R = position_moins_position(X1, X2)
print("R = X1 (-) X2 =", R)                              # [(1,2),(1,4),(1,5)]
print("X1 (+) R      =", position_plus_vitesse(X1, R), "(doit être égal à X2)")

# ------------------------------------------------------------------
# Exécution : figure 1 (5 villes)
# ------------------------------------------------------------------
print()
print("=== TSP 5 villes (départ sommet 1) ===")
meilleur = pso(D5, 5, 100)
print("Meilleur tour :", meilleur)
print("Longueur      :", longueur(meilleur, D5))

# ------------------------------------------------------------------
# Exécution : matrice 9 x 9
# ------------------------------------------------------------------
print()
print("=== TSP 9 villes (départ sommet 1) ===")
meilleur = pso(D9, 20, 300)
print("Meilleur tour :", meilleur)
print("Longueur      :", longueur(meilleur, D9))