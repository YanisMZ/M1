#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:42:27 2026

@author: yanis
"""


from functools import reduce


def my_zyp(*args):
    longueurs = list(map(len, args))
    
    min_longueurs = min(longueurs)
   
    resultat = []
    for i in range(min_longueurs):
        mapping = map(lambda iterable : iterable[i],args)
        resultat.append(tuple(mapping))
    return resultat
    
def my_filter(*args):
    func1 = lambda x: x % 3 == 0 or x % 5 == 0

    a = filter(func1, *args)

    return list(a)
    
# 1. Fonction de filtrage
def filtrer_clients(clients, montant_min, ville):
    return list(filter(
        lambda client: client["montant"] > montant_min
        and client["ville"] == ville,
        clients
    ))


# 2. Fonction de tri
def trier_clients(clients):
    return sorted(
        clients,
        key=lambda client: (-client["purchases"], client["name"])
    )


# 3. Fonction de statistiques
def statistiques_achats(clients):
    achats = list(map(lambda client: client["purchases"], clients))

    return {
        "somme": sum(achats),
        "moyenne": sum(achats) / len(achats) if achats else 0,
        "maximum": max(achats) if achats else None,
        "minimum": min(achats) if achats else None
    }

   


def main():
    
    print(my_zyp([1, 2, 3], ['a', 'b', 'c', 'd'], 'Python'))
    
    nums = list(range(101))
    
    
    string = 'Ordinary Least Squares'
    spells = [
        'riddikulus', 'obliviate', 'sectumsempra',
        'avada kedavra', 'alohomora', 'lumos',
        'expelliarmus', 'expecto patronum'
    ]
    print("\nexercice 2")
    nums_filtered = list(filter(lambda x: x % 3 != 0 and x % 5 != 0, nums))
    print("1.", nums_filtered,"\n")



    string_filtered = ''.join(filter(lambda x: x.lower() not in 'aeiouy', string))
    print("2.", string_filtered,"\n")


   
    spells_filtered = list(filter(lambda x: x.count('a') > 2, spells))
    print("3.", spells_filtered,"\n")
    
    
    sets = [
    {1, 4, 8, 9},
    {2, 4, 6, 9, 10, 8},
    {9, 0, 1, 2, 4}
    ]
    
    resultat = reduce(lambda acc, x: acc & x, sets)
    
    print(resultat)
        
        
        
    string = "Python"
    
    resultat = reduce(lambda acc, x: x + acc, string)
    
    print(resultat)
    
    nums = [1, 2, 3]

    resultat = int(reduce(lambda acc, x: acc + str(x), nums, ""))
    
    print(resultat)
    
    
    
    client_liste = [
        {'nom': 'Jean', 'prenom': 'Pierre', 'ville': 'Paris', 'montant': 100},
        {'nom': 'Marie', 'prenom': 'Charlotte', 'ville': 'Lyon', 'montant': 
    200},
        {'nom': 'Pierre', 'prenom': 'Paul', 'ville': 'Marseille', 'montant': 
    150},
        {'nom': 'Charlotte', 'prenom': 'Sophie', 'ville': 'Lyon', 'montant': 
    250},
        {'nom': 'Paul', 'prenom': 'Jacques', 'ville': 'Paris', 'montant': 
    300},
    ]

    min_amount = 150
    ville = 'Paris'

    client_filtré = filtrer_clients(client_liste, min_amount, ville)
    
    print(client_filtré)
    
    



   


if __name__ == "__main__":
    main()

