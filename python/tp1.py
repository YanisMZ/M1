import math
import pandas as pd



def test():
    a = 0
    return a


def crypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in message:
        if char in alphabet:
            idx = (alphabet.index(char) + key) % len(alphabet)
            result += alphabet[idx]
        else:
            result += char

    return result


def decrypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in message:
        if char in alphabet:
            idx = (alphabet.index(char) - key) % len(alphabet)
            result += alphabet[idx]
        else:
            result += char

    return result


def exercise4():
    print("\n========== EXERCICE 4 ==========")

    texte = "python"

    resultat = crypt(texte, 10)

    print("Texte original :", texte)
    print("Texte chiffré  :", resultat)

    # Vérification du déchiffrement
    print("Texte déchiffré :", decrypt(resultat, 10))



def exercise5():
    print("\n========== EXERCICE 5 ==========")

    chaine = "StRing ObJEcTs haVe mANY inTEREsting PROPErties!"

   
    mots = chaine.split()

    print("Liste de mots :", mots)

    mots[0] = mots[0].lower()
    mots[1] = mots[1].upper()
    mots[2] = mots[2].lower()
    mots[3] = mots[3].upper()
    mots[4] = mots[4].lower()
    mots[5] = mots[5].upper()

    print("Liste modifiée :", mots)

    # Joindre les mots pour créer une nouvelle chaîne
    nouvelle_chaine = " ".join(mots)

    print("Nouvelle chaîne :", nouvelle_chaine)



def exercise6():
    print("\n========== EXERCICE 6 ==========")

    df = pd.read_csv("heroes.csv")

    print("Avant correction :")
    print(df[["name", "Gender", "Hair color"]].head())

  
    df["Hair color"] = df["Hair color"].str.lower()


    df["Gender"] = df["Gender"].replace("Fmale", "Female")

    print("\nAprès correction :")
    print(df[["name", "Gender", "Hair color"]].head())

    print("\nNombre de 'Fmale' restant :",
          (df["Gender"] == "Fmale").sum())




def main():

    print("\n========== EXERCICE 1 ==========")
    basket1 = [
        'banana', 'kiwifruits', 'grapefruits', 'apples',
        'apricots', 'nectarines', 'oranges', 'peaches',
        'pears', 'lemons'
    ]

    basket2 = [
        'apples', 'grapes', 'apricots', 'dragonfruits',
        'peaches', 'pears', 'limes', 'papaya'
    ]

    for fruit in basket1:
        if fruit in basket2:
            basket2.remove(fruit)

    print(basket2)

    # Tant que basket2 a strictement moins d'éléments que basket1
    while len(basket2) <= len(basket1):
        fruit = basket1.pop()
        basket2.append(fruit)

    print(basket2)
    print(basket1)


    print("\n========== EXERCICE 2 ==========")
    A = {1, 2, 3, 4, 5, 6, 7}
    B = {5, 7, 9, 11, 13, 15}
    C = {1, 2, 8, 10, 11, 12, 13, 14, 15, 16, 17}
    D = {1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    E = {9, 10, 11, 12, 13, 14, 15}

    resultat1 = D.intersection(E)
    resultat2 = B.intersection(C)
    resultat3 = A.union(resultat2)

    total = resultat3.difference(resultat1)

    print(total)

    print("\n========== EXERCICE 3 ==========")
    range_x = [
        0.0, 0.2, 0.4, 0.6, 0.8, 1.0,
        1.2, 1.4, 1.6, 1.8, 2.0
    ]

    range_y = [
        0.0, 0.2, 0.4, 0.6, 0.8, 1.0,
        1.2, 1.4, 1.6, 1.8, 2.0
    ]

    circ_parab = dict()

    for x in range_x:
        for y in range_y:
            z = math.sqrt(x**2 + y**2)
            circ_parab[(x, y)] = z

    print(circ_parab[(1.4, 1.8)])



if __name__ == '__main__':
    test()
    main()

    exercise4()
    exercise5()
    exercise6()
