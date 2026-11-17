import math
import pandas as pd


def retrive_character_indices(chaine):
    character_indices = {}

    for indice, caractere in enumerate(chaine):
        if caractere in character_indices:
            character_indices[caractere].append(indice)
        else:
            character_indices[caractere] = [indice]

    return character_indices


def create_word_list(texte):
    return texte.split()


def exo2():
    spam = """Dear User,
    Our Administration Team needs to inform you that you are reaching the storage limit of your Mailbox account.
    You have to verify your account within the next 24 hours.
    Otherwise, it will not be possible to use the service.
    Please, click on the link below to verify your account and continue using our service.
    Your Administration Team."""

    spam = spam.lower()
    word_list = create_word_list(spam)

    unique_words = set(word_list)

    word_counter = {
        word: word_list.count(word)
        for word in unique_words
    }
    for word, count in word_counter.items():
        if count > 1:
            print(word, count)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def exo3():
    cands = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]
    primes = [n for n in cands if is_prime(n)]
    print("Nombres premiers :", primes)


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def exo4():
    list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    list2 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
    coprimes = []

    for a in list1:
        for b in list2:
            if pgcd(a, b) == 1:
                coprimes.append((a, b))
    print("Paires de nombres coprimes :")
    print(coprimes)


def main():
    
    print("===exo1=== \n")
    print(retrive_character_indices("ukulele"))
    
    print("\n ===exo2=== \n")
    exo2()

    
    
    print("\n ===exo3=== \n")
    exo3()
    print("\n ===exo4=== \n")
    exo4()


if __name__ == '__main__':
    main()
