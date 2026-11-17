
import random
import math


distances = [
    [0, 1, 7, 5, 2],
    [1, 0, 9, 3, 2],
    [7, 9, 0, 4, 3],
    [5, 3, 4, 0, 6],
    [2, 2, 3, 6, 0]
]


def f(x):
    cout = 0

    for i in range(len(x) - 1):
        cout += distances[x[i] - 1][x[i + 1] - 1]

    return cout


def recuit_simule():
    x1 = [1, 2, 3, 4, 5, 1]
    T = 1000
    xbest = x1[:]
    TB = 0.01
    NTF = 5

    while T > TB:
        i = 0

        while i < NTF:
            x2 = x1[:]

            a, b = random.sample(range(1, 5), 2)
            x2[a], x2[b] = x2[b], x2[a]

            delta = f(x2) - f(x1)

            if delta < 0:
                x1 = x2

                if f(x1) < f(xbest):
                    xbest = x1[:]

            else:
                if random.uniform(0, 1) < math.exp(-delta / T):
                    x1 = x2

            i += 1

        T = 0.99 * T

    return xbest


xbest = recuit_simule()

print("Meilleur parcours :", xbest)
print("Coût minimum :", f(xbest))
