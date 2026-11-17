
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets


# EXERCICE 1

votes = pd.read_csv("house-votes-84.csv")

print(votes.head())
votes.info()
print(votes.describe(include="all"))


# EXERCICE 2

variables = ["education", "missile", "satellite"]

for colonne in variables:
    plt.figure(figsize=(7, 4))
    sns.countplot(data=votes, x=colonne, hue="party", palette="Set2")
    plt.title("Répartition des votes : " + colonne)
    plt.xlabel("Réponse")
    plt.ylabel("Nombre de personnes")
    plt.tight_layout()
    plt.show()


# EXERCICE 3

donnees = votes.drop("party", axis=1)
classes = votes["party"]

donnees = pd.get_dummies(donnees)
donnees = donnees.fillna(0)

modele = KNeighborsClassifier(n_neighbors=6)
modele.fit(donnees, classes)


# EXERCICE 4

resultats = modele.predict(donnees)

print(resultats[:10])

nouveau_vote = pd.DataFrame(
    np.random.randint(0, 2, size=(1, donnees.shape[1])),
    columns=donnees.columns
)

prediction = modele.predict(nouveau_vote)

print("Prédiction :", prediction[0])


# EXERCICE 5

chiffres = datasets.load_digits()

print(chiffres.keys())
print(chiffres.DESCR)

print(chiffres.images.shape)
print(chiffres.data.shape)

plt.figure(figsize=(4, 4))
plt.imshow(chiffres.images[10], cmap="gray")
plt.axis("off")
plt.show()


# EXERCICE 6

images = chiffres.data
etiquettes = chiffres.target

X_train, X_test, y_train, y_test = train_test_split(
    images,
    etiquettes,
    test_size=0.2,
    random_state=42
)

classificateur = KNeighborsClassifier(n_neighbors=7)
classificateur.fit(X_train, y_train)

precision = classificateur.score(X_test, y_test)

print("Précision :", precision)


# EXERCICE 7

precision_train = []
precision_test = []

voisins = range(1, 10)

for k in voisins:
    classificateur = KNeighborsClassifier(n_neighbors=k)
    classificateur.fit(X_train, y_train)

    precision_train.append(classificateur.score(X_train, y_train))
    precision_test.append(classificateur.score(X_test, y_test))


plt.figure(figsize=(8, 5))

plt.plot(voisins, precision_train, marker="o", label="Apprentissage")
plt.plot(voisins, precision_test, marker="s", label="Test")

plt.xlabel("Nombre de voisins")
plt.ylabel("Précision")
plt.title("Résultats du KNN")
plt.xticks(list(voisins))
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

meilleur_k = list(voisins)[np.argmax(precision_test)]

print("Meilleur K :", meilleur_k)
print("Meilleure précision :", max(precision_test))
