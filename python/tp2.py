
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error


df = pd.read_csv("gm_2008_region.csv")


# EXERCICE 1

fertility = np.array(df["fertility"]).reshape(-1, 1)
life = np.array(df["life"]).reshape(-1, 1)


# EXERCICE 2

plt.figure(figsize=(10, 7))

correlations = df.select_dtypes(include="number").corr()

sns.heatmap(correlations, annot=True, cmap="RdYlGn", square=True)

plt.show()

print(df.info())
print(df.describe())
print(df.head())


# EXERCICE 3

plt.figure()

plt.scatter(fertility, life)

model = LinearRegression()
model.fit(fertility, life)

x_values = np.linspace(
    fertility.min(),
    fertility.max(),
    100
).reshape(-1, 1)

predictions = model.predict(x_values)

print("Score du modèle :", model.score(fertility, life))

plt.plot(x_values, predictions, color="red")
plt.xlabel("Fertility")
plt.ylabel("Life")
plt.show()


# EXERCICE 4

features = df.drop(columns=["life", "Region"])
target = df["life"]

x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.30,
    random_state=42
)

model_all = LinearRegression()
model_all.fit(x_train, y_train)

result = model_all.predict(x_test)

score = model_all.score(x_test, y_test)
error = np.sqrt(mean_squared_error(y_test, result))

print("Score R2 :", score)
print("RMSE :", error)


# EXERCICE 5

regression = LinearRegression()

scores = cross_val_score(
    regression,
    features,
    target,
    cv=5
)

print("Les scores :", scores)
print("Moyenne :", np.mean(scores))


# EXERCICE 6

start = time.perf_counter()

scores_3 = cross_val_score(
    regression,
    features,
    target,
    cv=3
)

time_3 = time.perf_counter() - start

start = time.perf_counter()

scores_10 = cross_val_score(
    regression,
    features,
    target,
    cv=10
)

time_10 = time.perf_counter() - start

print("Score moyen avec 3 folds :", scores_3.mean())
print("Temps avec 3 folds :", time_3)

print("Score moyen avec 10 folds :", scores_10.mean())
print("Temps avec 10 folds :", time_10)


# EXERCICE 7

lasso_model = Lasso(alpha=0.4)
lasso_model.fit(features, target)

coefficients = lasso_model.coef_

print("Coefficients :", coefficients)

plt.figure(figsize=(10, 5))

plt.bar(features.columns, coefficients)

plt.xticks(rotation=45)
plt.ylabel("Valeur des coefficients")
plt.xlabel("Caractéristiques")
plt.tight_layout()
plt.show()


# EXERCICE 8

alpha_list = np.logspace(-4, 4, 50)

ridge_model = Ridge(solver="svd")

average_scores = []
standard_deviations = []

for value in alpha_list:

    ridge_model.set_params(alpha=value)

    results = cross_val_score(
        ridge_model,
        features,
        target,
        cv=10
    )

    average_scores.append(results.mean())
    standard_deviations.append(results.std())


def afficher_resultats(alphas, moyennes, ecarts):

    plt.figure(figsize=(9, 5))

    plt.plot(alphas, moyennes, label="Score moyen")

    plt.fill_between(
        alphas,
        np.array(moyennes) - np.array(ecarts),
        np.array(moyennes) + np.array(ecarts),
        alpha=0.2
    )

    plt.xscale("log")
    plt.xlabel("Alpha")
    plt.ylabel("Score R2")
    plt.legend()
    plt.grid()
    plt.show()


afficher_resultats(
    alpha_list,
    average_scores,
    standard_deviations
)
