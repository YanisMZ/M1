import pandas as pd
from functools import reduce
from pathlib import Path

# Les deux CSV se trouvent dans le sous-dossier data.
# Path permet de lancer ce fichier depuis n'importe quel dossier.
dossier = Path(__file__).resolve().parent / 'data'


#Exercice 1
print("----------EXERCICE 1----------")

#Question 1
scores = pd.read_csv(dossier / 'scores.csv')
# Harmoniser les intitulés : 'math score' devient 'math_score'.
scores.columns = scores.columns.str.strip().str.lower().str.replace(' ', '_')
# Garder les données initiales sur 100 pour les exercices 4 et 6.
scores_origine = scores.copy()


#Question 2
def moyenne_ponderee(ligne):
    return (3 * ligne['math_score'] + 2 * ligne['reading_score']
            + ligne['writing_score']) / 6


#Question 3 : axis=1 applique la fonction à chaque ligne.
scores['weighted_average'] = scores.apply(moyenne_ponderee, axis=1)

#Question 4
print("Les 10 premières moyennes pondérées (coefficients 3, 2, 1) :")
print(scores[['math_score', 'reading_score', 'writing_score',
              'weighted_average']].head(10))


#Exercice 2
print("\n----------EXERCICE 2----------")

#Question 1
cols = ['math_score', 'reading_score', 'writing_score']


#Question 2
def rank(serie):
    moyenne = serie.mean()
    if moyenne > 90:
        niveau = 'high'
    elif moyenne > 60:
        niveau = 'medium'
    else:
        niveau = 'low'
    return [moyenne, niveau]


#Question 3 : expand répartit les deux valeurs dans deux colonnes.
scores[['mean', 'rank']] = scores[cols].apply(rank, axis=1,
                                            result_type='expand')

#Question 4
print("Notes, moyenne simple et rang :")
print(scores[cols + ['mean', 'rank']])


#Exercice 3
print("\n----------EXERCICE 3----------")


#Question 1
def rescale(colonne, low, high):
    return colonne * (high - low) / 100 + low


#Question 2
cols = ['math_score', 'reading_score', 'writing_score', 'mean']

#Question 3 : axis=0 applique la fonction à chaque colonne.
scores[cols] = scores[cols].apply(rescale, axis=0, args=(0, 20))

print("Notes et moyenne converties sur 20 :")
print(scores[cols].head(10))
# weighted_average reste sur 100 : elle n'est pas demandée dans cet exercice.
# rank conserve la catégorie calculée sur 100 à l'exercice 2.


#Exercice 4
print("\n----------EXERCICE 4----------")

# Les seuils du sujet sont sur 100, donc repartir des notes originales.
scores_risque = scores_origine.copy()


#Question 1
def evaluer_risque(ligne, seuil_math, seuil_reading, seuil_writing):
    score = 0
    if ligne['math_score'] < seuil_math:
        score += 1
    if ligne['reading_score'] < seuil_reading:
        score += 1
    if ligne['writing_score'] < seuil_writing:
        score += 1

    if ligne['test_preparation_course'] == 'completed':
        score -= 0.5

    if score <= 0.5:
        niveau = 'Faible risque'
    elif score <= 1.5:
        niveau = 'Risque modéré'
    elif score <= 2.5:
        niveau = 'Risque élevé'
    else:
        niveau = 'Risque critique'

    return pd.Series({'score_risque': score, 'niveau_risque': niveau})


#Question 2
scores_risque[['risque_std', 'niveau_std']] = scores_risque.apply(
    evaluer_risque, axis=1, args=(50, 50, 50)
)
scores_risque[['risque_exigeant', 'niveau_exigeant']] = scores_risque.apply(
    evaluer_risque, axis=1, args=(65, 65, 65)
)
scores_risque[['risque_bas', 'niveau_bas']] = scores_risque.apply(
    evaluer_risque, axis=1, args=(40, 40, 40)
)

#Question 3
for nom in ['std', 'exigeant', 'bas']:
    print(f"\nRésultats pour les seuils {nom} :")
    print(scores_risque[['risque_' + nom, 'niveau_' + nom]])
    print("Nombre d'élèves par niveau de risque :")
    print(scores_risque['niveau_' + nom].value_counts())


#Exercice 5
print("\n----------EXERCICE 5----------")

#Question 1
diabetes = pd.read_csv(dossier / 'diabetes.csv')
diabetes.columns = diabetes.columns.str.strip().str.lower().str.replace(' ', '_')

#Question 2 : catégories demandées dans le sujet.
diabetes['bmi_cat'] = diabetes['bmi'].apply(
    lambda imc: 'Normal' if imc < 25 else
    'Surpoids' if imc < 30 else 'Surpoids sévère'
)
print("Nombre de patients par catégorie d'IMC :")
print(diabetes['bmi_cat'].value_counts())

#Question 3 : 30 et 45 sont inclus dans le groupe du milieu.
diabetes['age_grp'] = diabetes['age'].apply(
    lambda age: '<30' if age < 30 else '30-45' if age <= 45 else '>45'
)
print("\nNombre de patients par groupe d'âge :")
print(diabetes['age_grp'].value_counts())

#Question 4 : normaliser chaque colonne avec son propre minimum et maximum.
cols = ['plasma_glucose', 'bmi', 'age']
diabetes_normalise = diabetes[cols].apply(
    lambda colonne: (colonne - colonne.min()) / (colonne.max() - colonne.min())
    if colonne.max() != colonne.min() else colonne * 0,
    axis=0
)
# Pour une colonne constante, on choisit 0 afin d'éviter la division par zéro.
print("\nLes 5 premières lignes normalisées entre 0 et 1 :")
print(diabetes_normalise.head())


#Exercice 6
print("\n----------EXERCICE 6----------")

#Question 1
scores = pd.read_csv(dossier / 'scores.csv')
scores.columns = scores.columns.str.strip().str.lower().str.replace(' ', '_')


def prevalence(serie):
    #Question 2 : une paire (catégorie, effectif) par valeur distincte.
    valeurs = serie.dropna()
    if len(valeurs) == 0:
        return None
    decompte = [(valeur, (valeurs == valeur).sum())
                for valeur in valeurs.unique()]

    #Question 3 : garder la paire dont l'effectif est le plus grand.
    # En cas d'égalité, conserver la première catégorie rencontrée.
    plus_frequent = reduce(lambda x, y: x if x[1] >= y[1] else y, decompte)

    #Question 4
    return plus_frequent[0]


#Question 5 : colonnes personnelles contenant des catégories de texte.
cols = list(scores.select_dtypes(include=['object', 'string']).columns)
print("Catégorie la plus fréquente pour chaque donnée personnelle :")
print(scores[cols].apply(prevalence, axis=0))
