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















équipes = set()
for match in matchs:
    équipes.add(match["team"])
    équipes.add(match["opponent"])

# 2) Calculez les statistiques des équipes
équipes_statistiques = defaultdict(lambda : {"victoires": 0, "défaites": 
0, "matches_nuls": 0, "points": 0, "buts_marqués": 0, "buts_encaissés": 0, 
"différence_buts": 0})
for match in matchs:
    équipes_statistiques[match["team"]]["victoires"] += 1
    équipes_statistiques[match["opponent"]]["défaites"] += 1
    équipes_statistiques[match["team"]]["points"] += 3 if 
match["team_score"] > match["opponent_score"] else 1
    équipes_statistiques[match["opponent"]]["points"] += 3 if 
match["opponent_score"] > match["team_score"] else 1
    équipes_statistiques[match["team"]]["buts_marqués"] += 
match["team_score"]
    équipes_statistiques[match["opponent"]]["buts_encaissés"] += 
match["opponent_score"]
    équipes_statistiques[match["team"]]["différence_buts"] += 
match["team_score"] - match["opponent_score"]
    équipes_statistiques[match["opponent"]]["différence_buts"] += 
match["opponent_score"] - match["team_score"]
    if match["team_score"] == match["opponent_score"]:
        équipes_statistiques[match["team"]]["matches_nuls"] += 1
        équipes_statistiques[match["opponent"]]["matches_nuls"] += 1

# 3) Classez les équipes
équipes_classement = sorted(équipes_statistiques.items(), 
key=itemgetter("points", "victoires", "matches_nuls", "différence_buts"), 
reverse=True)

# 4) Identifiez les meilleures équipes
meilleure_attaque = max(équipes_statistiques, key=lambda équipe: 
équipe["buts_marqués"])
meilleure_defense = min(équipes_statistiques, key=lambda équipe: 
équipe["buts_encaissés"])

print("Classement des équipes:")
for équipe, statistiques in équipes_classement:
    print(f"{équipe}: {statistiques['points']} - 
{statistiques['victoires']} victoires - {statistiques['défaites']} 
défaites - {statistiques['matches_nuls']} matches nuls - 
{statistiques['buts_marqués']} buts marqués - 
{statistiques['buts_encaissés']} buts encaissés - 
{statistiques['différence_buts']} différence de buts")

print(f"\nMeilleure attaque : {meilleure_attaque} avec 
{équipes_statistiques[meilleure_attaque]['buts_marqués']} buts marqués")
print(f"Meilleure défense : {meilleure_defense} avec 
{équipes_statistiques[meilleure_defense]['buts_encaissés']} buts 
encaissés")
