

import numpy as np
import pandas as pd

SCORES_CSV = "scores.csv"
DIABETES_CSV = "diabetes.csv"

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def titre(texte):
    print("\n")
    print(texte)
    print("\n")



titre("Exercice 1 : moyenne pondérée")

scores = pd.read_csv(SCORES_CSV)
print(scores.columns.tolist())


def moyenne_ponderee(row):
    return (
        3 * row["math score"]
        + 2 * row["reading score"]
        + row["writing score"]
    ) / 6


scores["weighted_average"] = scores.apply(moyenne_ponderee, axis=1)

print(scores[[
    "math score",
    "reading score",
    "writing score",
    "weighted_average"
]].head(10))

titre("Exercice 2 : mean et rank")
cols = ["math score", "reading score", "writing score"]


def rank(serie):
    moyenne = serie.mean()
    if moyenne > 90:
        niveau = "high"
    elif moyenne > 60:
        niveau = "medium"
    else:
        niveau = "low"
    return [moyenne, niveau]


scores[["mean", "rank"]] = scores[cols].apply(
    rank, axis=1, result_type="expand"
)

scores["mean"] = scores["mean"].astype(float)

print(scores[cols + ["mean", "rank"]].head(10))
print("\nRépartition des rangs :")
print(scores["rank"].value_counts())


titre("Exercice 3 : rescale")


def rescale(colonne, low, high):
    return colonne * (high - low) / 100 + low

cols = ["math score", "reading score", "writing score", "mean"]

scores_20 = scores[cols].apply(rescale, args=(0, 20))

print(scores_20.head(10))
print("\nMin / Max après mise à l'échelle :")
print(scores_20.agg(["min", "max"]))


titre("Exercice 4 : risque académique")

df = scores.copy()

def risque(row, seuil_math, seuil_reading, seuil_writing):
    score = 0
    score += row["math score"] < seuil_math
    score += row["reading score"] < seuil_reading
    score += row["writing score"] < seuil_writing

    score = float(score)

    if row["test preparation course"] == "completed":
        score -= 0.5

    if score <= 0.5:
        niveau = "Faible risque"
    elif score <= 1.5:
        niveau = "Risque modéré"
    elif score <= 2.5:
        niveau = "Risque élevé"
    else:
        niveau = "Risque critique"

    return pd.Series({
        "score_risque": score,
        "niveau_risque": niveau
    })

configs = {
    "std": (50, 50, 50),
    "exigeant": (65, 65, 65),
    "bas": (40, 40, 40)
}

for nom, seuils in configs.items():
    df[[f"risque_{nom}", f"niveau_{nom}"]] = df.apply(
        risque, axis=1, args=seuils
    )
    df[f"risque_{nom}"] = df[f"risque_{nom}"].astype(float)


ordre = [
    "Faible risque",
    "Risque modéré",
    "Risque élevé",
    "Risque critique"
]

for nom, seuils in configs.items():
    print(f"\nSeuils {seuils} (niveau_{nom}")
    print(
        df[f"niveau_{nom}"]
        .value_counts()
        .reindex(ordre, fill_value=0)
    )

print(df[[
    "math score",
    "reading score",
    "writing score",
    "test preparation course",
    "risque_std",
    "niveau_std",
    "risque_exigeant",
    "niveau_exigeant",
    "risque_bas",
    "niveau_bas"
]].head(10))


titre("Exercice 5 : diabetes.csv")

diab = pd.read_csv(DIABETES_CSV)

print(diab.columns.tolist())
print("Valeurs manquantes :\n", diab.isna().sum())

diab["bmi_cat"] = diab["bmi"].apply(
    lambda x: np.nan if pd.isna(x)
    else "Normal" if x < 25
    else "Surpoids" if x < 30
    else "Surpoids sévère"
)
print("\nNombre de patients par catégorie d'IMC :")
print(diab["bmi_cat"].value_counts())

diab["age_grp"] = diab["age"].apply(
    lambda a: "<30" if a < 30
    else "30-45" if a < 45
    else ">45"
)
print("\nEffectif par groupe d'âge :")
print(diab["age_grp"].value_counts())

cols_norm = ["plasma glucose", "bmi", "age"]

diab_norm = diab[cols_norm].apply(
    lambda c: (c - c.min()) / (c.max() - c.min())
)
print("\n5 premières lignes des données normalisées :")
print(diab_norm.head())



