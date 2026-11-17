
import math


def exercice1():
    print("\nEXERCICE 1")

    f = lambda x: x**2 if x >= 0 else 0
    print(f(3))
    print(f(-2))


    nombres = [1, 2, 3, 4, 5, 6, 7, 8]
    pairs = [n for n in nombres if n % 2 == 0]
    print(pairs)


    s1 = "bonjour"
    s2 = "bonsoir"
    communs = [c for c in s1 if c in s2]
    print(communs)


def exercice2():
    print("\nEXERCICE 2 ")


    func1 = lambda x, y: x if x >= y else y
    print(func1(5, 8))


    func2 = lambda s: {c: s.count(c) for c in set(s)}
    print(func2("bonjour"))


    func3 = lambda *nums: math.sqrt(sum([n**2 for n in nums]))
    print(func3(3, 4))
    print(func3(2, 3, 6))


def exercice3():
    print("\nEXERCICE 3")

    words = [
        'car', 'truck', 'interview', 'time', 'cell',
        'chicken', 'leader', 'government', 'transaction',
        'country', 'bag', 'call', 'area', 'service',
        'phone', 'advantage', 'job', 'shape', 'item',
        'atmosphere', 'height', 'creature', 'plane', 'unit'
    ]

 
    resultat = sorted(words, key=lambda mot: len(mot))
    print("Par longueur :", resultat)


    resultat = sorted(words, key=lambda mot: mot[-1])
    print("Par dernier caractere :", resultat)

 
    resultat = sorted(
        words,
        key=lambda mot: mot.count('a')
        + mot.count('b')
        + mot.count('c')
    )
    print("Par nombre de a, b et c :", resultat)


def exercice4():
    print("\nEXERCICE 4")

    taches = [
        {"nom": "Debug critique", "priorite": "haute",
         "temps_estime": 120},
        {"nom": "Documentation", "priorite": "basse",
         "temps_estime": 60},
        {"nom": "Réunion équipe", "priorite": "moyenne",
         "temps_estime": 30},
        {"nom": "Refactoring", "priorite": "moyenne",
         "temps_estime": 90},
        {"nom": "Urgence production", "priorite": "critique",
         "temps_estime": 45}
    ]


    priorite = lambda p: 3.0 if p == "critique" else 2.0 if p == "haute" else 1.0 if p == "moyenne" else 0.5


    for tache in taches:
        nom = tache["nom"]
        p = tache["priorite"]
        coefficient = priorite(p)

        print(
            f"{nom} - Priorité: {p} "
            f"-> Coefficient: {coefficient}"
        )


def main():
    exercice1()
    exercice2()
    exercice3()
    exercice4()


if __name__ == "__main__":
    main()

