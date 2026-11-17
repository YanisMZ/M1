import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Charger le dataset
df = pd.read_csv("breast-cancer-wisconsin-data.csv")

# Afficher les premières lignes
print(df.head())


