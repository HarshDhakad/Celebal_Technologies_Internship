import streamlit as st
import pickle
import numpy as np

with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Prediction App")
st.write("Enter flower measurements to predict the species.")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 3.0, 0.2)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)[0]

species = ['Setosa', 'Versicolor', 'Virginica']
st.success(f"🌼 Predicted species: **{species[prediction]}**")
