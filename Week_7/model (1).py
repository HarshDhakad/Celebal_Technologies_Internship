import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

model = RandomForestClassifier()
model.fit(X, y)

with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)
