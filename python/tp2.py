import re
import pandas as pd

def exo1():

    text = "Let's consider the following temperatures using the Celsius scale: +23 C, 0 C, -20.0 C, -2.2 C, -5.65 C, 0.0001 C. To convert them to the Fahrenheit scale you have to multiply the number by 9/5 and add 32 to the result. Therefore, the corresponding temperatures in the Fahrenheit scale will be: +73.4 F, 32 F, -4.0 F, +28.04 F, 21.83 F, +32.00018 F."


    motif = r'[+-]?\d+(?:\.\d+)? C'


    resultat = re.findall(motif, text)
    
    print("Exercice 1")
    print(resultat)

    


def exo2():
  
    motif = r'^[a-z][a-z0-9-]{1,14}[a-z]$'

    noms = [
        "abc",
        "john123",
        "user_name",
        "user-name",
        "a1b",
        "ab",
        "abcdefghijklmnop",
        "abc_123",
        "123abc",
        "abc!",
        "ABCdef"
    ]

    print("\nEXERCICE 2")

    for nom in noms:
        if re.fullmatch(motif, nom):
            print(nom, "-> VALIDE")
        else:
            print(nom, "-> INVALIDE")

    print()



def exo3():

    movies = [
        '1984, 1984, Michael Radford',
        'The Good, the Bad and the Ugly, 1966, Sergio Leone',
        'Terminator 2: Judgment Day, 1991, James Cameron',
        "Harry Potter and the Philosopher's Stone, 2001, Chris Columbus",
        'Back to the Future, 1985, Robert Zemeckis',
        'No Country for Old Men, 2007, Joel Coen, Ethan Coen'
    ]


    motif = r',\s*\d{4},\s*'

    movies_without_year = []

    for movie in movies:

 
        parts = re.split(motif, movie)

     
        nouveau_movie = ", ".join(parts)

        movies_without_year.append(nouveau_movie)

    print("\nEXERCICE 3")

    for movie in movies_without_year:
        print(movie)

 
    movies_dict = {}

    for movie in movies_without_year:
        nom, realisateur = movie.split(", ", 1)
        movies_dict[nom] = realisateur

    print("\nDictionnaire :")

    for film, realisateur in movies_dict.items():
        print(film, "->", realisateur)

    resultat = " | ".join(movies_without_year)

    print("\nChaîne finale :")
    print(resultat)

    return movies_without_year




def filtrer_telephones(fichier_csv):

    df = pd.read_csv(fichier_csv)

 

    motif = r'^(?:\+33|0033)[\s./-]*03(?:[\s./-]*\d){8}$'
    
    def est_valide(numero):
        return bool(re.fullmatch(motif, str(numero).strip()))


    if "Téléphone" not in df.columns:
        print("Erreur : la colonne 'telephone' n'existe pas.")
        return df

    df["valide"] = df["Téléphone"].apply(est_valide)
    
    print(df[df["valide"]])

    return df






def main():
    exo1()

    exo2()

    exo3()
    print("\nEXERCICE 5")
    filtrer_telephones("contacts.csv")




if __name__ == '__main__':
    main()
