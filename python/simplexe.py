import numpy as np


def simplex(A, b, c):
    """
    Résout :

        Max Z = c.x

    sous contraintes :

        A.x <= b
        x >= 0
    """

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    m, n = A.shape

    # -----------------------------------------
    # Construction du tableau initial
    # -----------------------------------------

    # Ajout des variables d'écart
    tableau = np.zeros((m + 1, n + m + 1))

    tableau[:m, :n] = A

    # Variables d'écart
    tableau[:m, n:n + m] = np.eye(m)

    # Second membre
    tableau[:m, -1] = b

    # Fonction objectif
    tableau[-1, :n] = -c

    # -----------------------------------------
    # Algorithme du simplexe
    # -----------------------------------------

    while True:

        # Chercher la colonne entrante
        colonne_pivot = np.argmin(
            tableau[-1, :-1]
        )

        # Si tous les coefficients sont >= 0,
        # on a atteint l'optimum
        if tableau[-1, colonne_pivot] >= 0:
            break

        # -------------------------------------
        # Test du rapport
        # -------------------------------------

        rapports = []

        for i in range(m):

            coefficient = tableau[i, colonne_pivot]

            if coefficient > 0:
                rapports.append(
                    tableau[i, -1] / coefficient
                )
            else:
                rapports.append(np.inf)

        ligne_pivot = np.argmin(rapports)

        # Vérification d'un problème non borné
        if rapports[ligne_pivot] == np.inf:
            raise ValueError(
                "Le problème est non borné."
            )

        # -------------------------------------
        # Pivot
        # -------------------------------------

        pivot = tableau[
            ligne_pivot,
            colonne_pivot
        ]

        # Normalisation de la ligne pivot
        tableau[ligne_pivot] /= pivot

        # Annuler la colonne pivot
        for i in range(m + 1):

            if i != ligne_pivot:

                facteur = tableau[
                    i,
                    colonne_pivot
                ]

                tableau[i] -= (
                    facteur *
                    tableau[ligne_pivot]
                )

    # -----------------------------------------
    # Récupération de la solution
    # -----------------------------------------

    solution = np.zeros(n)

    for j in range(n):

        colonne = tableau[:m, j]

        # Vérifier si la colonne est une colonne unité
        if np.count_nonzero(
            np.abs(colonne) > 1e-10
        ) == 1:

            ligne = np.where(
                np.abs(colonne) > 1e-10
            )[0][0]

            if abs(tableau[ligne, j] - 1) < 1e-10:
                solution[j] = tableau[ligne, -1]

    valeur_max = tableau[-1, -1]

    return solution, valeur_max, tableau


# =================================================
# EXEMPLE
# =================================================

# Max Z = 3x + 5y

c = [3, 5]

# 2x + y <= 10
# x + 3y <= 15

A = [
    [2, 1],
    [1, 3]
]

b = [10, 15]


solution, maximum, tableau = simplex(A, b, c)


print("Solution optimale :")

for i, valeur in enumerate(solution):
    print(f"x{i + 1} = {valeur}")

print("\nMaximum :")
print(maximum)

print("\nTableau final :")
print(tableau)