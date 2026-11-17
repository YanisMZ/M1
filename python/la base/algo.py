
import random
import matplotlib.pyplot as plt

# Fonction à minimiser
def f(x):
    return (x - 1) ** 2 * (x - 8) ** 2


def pso():

    x1 = -4
    x2 = -6
    x3 = -7

    v1 = 0
    v2 = 0
    v3 = 0

    # Meilleures positions personnelles
    p1 = -3
    p2 = -5
    p3 = -10

    # Coefficients
    rho = 0.5
    b1 = 0.5
    b2 = 0.5

    # Meilleure position globale
    pg = p1

    i = 0
    N = 500

    while i < N:

        # Recherche de la meilleure position globale
        if f(p1) <= f(p2) and f(p1) <= f(p3):
            pg = p1
        elif f(p2) <= f(p1) and f(p2) <= f(p3):
            pg = p2
        else:
            pg = p3

        # Mise à jour des vitesses
        v1 = rho * v1 + b1 * (p1 - x1) + b2 * (pg - x1)
        v2 = rho * v2 + b1 * (p2 - x2) + b2 * (pg - x2)
        v3 = rho * v3 + b1 * (p3 - x3) + b2 * (pg - x3)

        # Mise à jour des positions
        x1 = x1 + v1
        x2 = x2 + v2
        x3 = x3 + v3

        # Mise à jour des meilleures positions personnelles
        if f(x1) < f(p1):
            p1 = x1

        if f(x2) < f(p2):
            p2 = x2

        if f(x3) < f(p3):
            p3 = x3

        i = i + 1

    # Affichage des résultats
    print("Meilleure position :", pg)
    print("Valeur de la fonction :", f(pg))
    print("Particule 1 :", x1)
    print("Particule 2 :", x2)
    print("Particule 3 :", x3)


# Exécution du PSO
pso()


# Tracé de la fonction après le PSO
x = []
y = []

i = -5
while i <= 10:
    x.append(i)
    y.append(f(i))
    i = i + 0.1

plt.plot(x, y, label="f(x) = (x-1)^2(x-8)^2")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Fonction à minimiser après le PSO")

plt.grid()
plt.legend()
plt.show()
