# TP3 : Évaluation et réglage des modèles
# Fichiers nécessaires dans le même dossier : diabetes.csv et gm_2008_region.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, ElasticNet
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (classification_report, confusion_matrix, roc_curve,
                             roc_auc_score, precision_recall_curve, auc,
                             mean_squared_error)

# ======================================================================
# Exercice 1 : Métriques de classification
# ======================================================================
print("===== Exercice 1 =====")

# 1. Chargement des données
df = pd.read_csv("diabetes.csv")
X = df.drop("diabetes", axis=1)
y = df["diabetes"]

# 3. Ensembles d'entraînement et de test (40% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# 4. k-NN avec 6 voisins
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# 5. Matrice de confusion et rapport de classification
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))

# ======================================================================
# Exercice 2 : Régression logistique
# ======================================================================
print("===== Exercice 2 =====")

logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 6. Comparaison : regardez les colonnes precision / recall / f1-score
# des deux rapports. Le modèle avec les meilleures valeurs (surtout pour
# la classe 1 = diabète) est le plus performant.

# ======================================================================
# Exercice 3 : Courbe ROC
# ======================================================================
print("===== Exercice 3 =====")

# Probabilités d'appartenir à la classe 1
y_pred_prob = logreg.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

plt.plot([0, 1], [0, 1], "k--")
plt.plot(fpr, tpr, label="Régression logistique")
plt.xlabel("FPR (taux de faux positifs)")
plt.ylabel("TPR (taux de vrais positifs)")
plt.title("Courbe ROC")
plt.legend()
plt.show()

# ======================================================================
# Exercice 4 : Aire sous la courbe ROC (AUC)
# ======================================================================
print("===== Exercice 4 =====")

y_pred_prob = logreg.predict_proba(X_test)[:, 1]

# AUC sur l'ensemble de test
print("AUC :", roc_auc_score(y_test, y_pred_prob))

# AUC avec validation croisée 5 folds
cv_auc = cross_val_score(logreg, X, y, cv=5, scoring="roc_auc")
print("AUC par validation croisée :", cv_auc)

# ======================================================================
# Exercice 5 : Courbe précision-rappel
# ======================================================================
print("===== Exercice 5 =====")

precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)

plt.plot(recall, precision)
plt.xlabel("Rappel (recall)")
plt.ylabel("Précision")
plt.title("Courbe précision-rappel")
plt.show()

# Aire sous la courbe précision-rappel
print("Aire sous la courbe précision-rappel :", auc(recall, precision))

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# 5. Analyse : plus la courbe reste en haut à droite, meilleur est le modèle.
# Augmenter le rappel (détecter plus de diabétiques) fait baisser la précision
# (plus de fausses alertes) et inversement.

# ======================================================================
# Exercice 6 : GridSearchCV avec la régression logistique
# ======================================================================
print("===== Exercice 6 =====")

c_space = np.logspace(-5, 8, 15)
param_grid = {"C": c_space}

logreg = LogisticRegression(max_iter=1000)
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)
logreg_cv.fit(X, y)

print("Meilleur paramètre :", logreg_cv.best_params_)
print("Meilleur score :", logreg_cv.best_score_)

# ======================================================================
# Exercice 7 : RandomizedSearchCV avec un arbre de décision
# ======================================================================
print("===== Exercice 7 =====")

param_dist = {"max_depth": [3, None],
              "max_features": np.random.randint(1, 8, size=5),
              "min_samples_leaf": np.random.randint(1, 8, size=5),
              "criterion": ["gini", "entropy"]}

tree = DecisionTreeClassifier()
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)
tree_cv.fit(X, y)

print("Meilleurs hyperparamètres :", tree_cv.best_params_)
print("Meilleur score :", tree_cv.best_score_)

# ======================================================================
# Exercice 8 : GridSearchCV sur l'ensemble d'entraînement
# ======================================================================
print("===== Exercice 8 =====")

c_space = np.logspace(-5, 8, 15)
param_grid = {"C": c_space, "penalty": ["l1", "l2"]}

# solver="liblinear" accepte les pénalités l1 et l2
logreg = LogisticRegression(solver="liblinear")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

logreg_cv = GridSearchCV(logreg, param_grid, cv=5)
logreg_cv.fit(X_train, y_train)

print("Meilleurs paramètres :", logreg_cv.best_params_)
print("Meilleur score :", logreg_cv.best_score_)

# ======================================================================
# Exercice 9 : GridSearchCV pour un modèle Elastic Net (Gapminder)
# ======================================================================
print("===== Exercice 9 =====")

df_gm = pd.read_csv("gm_2008_region.csv")
y = df_gm["life"]
X = df_gm.drop(["life", "Region"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

l1_space = np.linspace(0, 1, 30)
param_grid = {"l1_ratio": l1_space}

elastic_net = ElasticNet()
gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)
gm_cv.fit(X_train, y_train)

y_pred = gm_cv.predict(X_test)

print("Meilleur l1_ratio :", gm_cv.best_params_)
print("Score R2 sur le test :", gm_cv.score(X_test, y_test))
print("Erreur quadratique moyenne :", mean_squared_error(y_test, y_pred))
