# TP4 : Prétraitement des données
# Fichiers nécessaires dans le même dossier : gm_2008_region.csv et house-votes-84_raw.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.linear_model import Ridge, ElasticNet
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import scale, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# ======================================================================
# Exercice 1 : Exploration des caractéristiques catégorielles
# ======================================================================
print("===== Exercice 1 =====")

df = pd.read_csv("gm_2008_region.csv")

# Boxplot de l'espérance de vie par région
df.boxplot("life", "Region", rot=60)
plt.show()

# ======================================================================
# Exercice 2 : Création de variables catégorielles
# ======================================================================
print("===== Exercice 2 =====")

df_gm = pd.get_dummies(df)
print(df_gm.columns)

# On supprime la colonne Region_America (pour éviter la redondance)
df_gm = df_gm.drop("Region_America", axis=1)
print(df_gm.columns)

# ======================================================================
# Exercice 3 : Régression avec des caractéristiques catégorielles
# ======================================================================
print("===== Exercice 3 =====")

X = df_gm.drop("life", axis=1)
y = df_gm["life"]

ridge = Ridge(alpha=0.5)
ridge_cv = cross_val_score(ridge, X, y, cv=5)
print("Scores de la validation croisée :", ridge_cv)

# ======================================================================
# Exercice 4 : Suppression de données manquantes
# ======================================================================
print("===== Exercice 4 =====")

# Le fichier brut n'a pas d'en-tête
df_votes = pd.read_csv("house-votes-84_raw.csv", header=None)
print(df_votes.head())

# Convertir les "?" en NaN
df_votes = df_votes.replace("?", np.nan)

# Nombre total de NaN
print("Nombre de NaN :", df_votes.isnull().sum().sum())

# Suppression des lignes avec des valeurs manquantes
n_avant = df_votes.shape[0]
df_sans_nan = df_votes.dropna()
n_apres = df_sans_nan.shape[0]
print("Lignes perdues :", n_avant - n_apres)

# ======================================================================
# Exercice 5 : Imputation avec un pipeline
# ======================================================================
print("===== Exercice 5 =====")

# On repart des données brutes (avec NaN)
df_votes = pd.read_csv("house-votes-84_raw.csv", header=None)
df_votes = df_votes.replace("?", np.nan)

# Attributs = toutes les colonnes sauf la première, cible = première colonne
X = df_votes.iloc[:, 1:]
y = df_votes.iloc[:, 0]

# Remplacer les valeurs textuelles par 0 et 1
X = X.replace({"n": 0, "y": 1})

# Transformateur d'imputation (valeur la plus fréquente)
imp = SimpleImputer(missing_values=np.nan, strategy="most_frequent")

# Classificateur SVC
clf = SVC()

# Étapes du pipeline
steps = [("imputation", imp), ("SVM", clf)]
pipeline = Pipeline(steps)

# Ensembles d'entraînement et de test (30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(classification_report(y_test, y_pred))

# ======================================================================
# Exercice 6 : Standardiser les données
# ======================================================================
print("===== Exercice 6 =====")

df_gm2 = pd.read_csv("gm_2008_region.csv")

X = df_gm2.drop("Region", axis=1)
y = df_gm2["Region"]

X_scaled = scale(X)

print("Moyenne avant :", np.mean(X, axis=0))
print("Écart-type avant :", np.std(X, axis=0))
print("Moyenne après :", np.mean(X_scaled, axis=0))
print("Écart-type après :", np.std(X_scaled, axis=0))

# 6. Conclusion : après standardisation, chaque attribut a une moyenne
# proche de 0 et un écart-type égal à 1.

# ======================================================================
# Exercice 7 : Standardiser dans un pipeline
# ======================================================================
print("===== Exercice 7 =====")

steps = [("scaler", StandardScaler()),
         ("knn", KNeighborsClassifier())]
pipeline = Pipeline(steps)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modèle standardisé
knn_scaled = pipeline.fit(X_train, y_train)

# Modèle non standardisé (pour comparer)
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

print("Score avec standardisation :", knn_scaled.score(X_test, y_test))
print("Score sans standardisation :", knn_unscaled.score(X_test, y_test))

# ======================================================================
# Exercice 8 : Pipeline de classification (Iris)
# ======================================================================
print("===== Exercice 8 =====")

iris = datasets.load_iris()
X = iris.data
y = iris.target

steps = [("scaler", StandardScaler()),
         ("SVM", SVC())]
pipeline = Pipeline(steps)

parameters = {"SVM__C": [1, 10, 100],
              "SVM__gamma": [0.1, 0.01]}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# GridSearchCV avec 3 folds (valeur par défaut)
cv = GridSearchCV(pipeline, parameters)
cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)

print(classification_report(y_test, y_pred))
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Score :", cv.score(X_test, y_test))
print("Meilleurs paramètres :", cv.best_params_)

# ======================================================================
# Exercice 9 : Pipeline de régression (Gapminder)
# ======================================================================
print("===== Exercice 9 =====")

df_gap = pd.read_csv("gm_2008_region.csv")
y = df_gap["life"]
X = df_gap.drop(["life", "Region"], axis=1)

steps = [("imputation", SimpleImputer(strategy="mean")),
         ("scaler", StandardScaler()),
         ("elasticnet", ElasticNet())]
pipeline = Pipeline(steps)

parameters = {"elasticnet__l1_ratio": np.linspace(0, 1, 30)}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

gm_cv = GridSearchCV(pipeline, parameters, cv=3)
gm_cv.fit(X_train, y_train)

print("Score R2 sur le test :", gm_cv.score(X_test, y_test))
print("Meilleur l1_ratio :", gm_cv.best_params_)
