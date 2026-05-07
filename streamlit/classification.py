import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cache data loading
@st.cache
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# Train model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# -------- STREAMLIT UI --------

st.title("🌸 Iris Flower Classification App")
st.write("Predict the species of Iris flower using Random Forest")

st.sidebar.header("Input Features")

# User inputs
sepal_length = st.sidebar.slider(
    "Sepal Length (cm)", float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)", float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)", float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)", float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

# Create input dataframe
input_data = pd.DataFrame({
    'sepal length (cm)': [sepal_length],
    'sepal width (cm)': [sepal_width],
    'petal length (cm)': [petal_length],
    'petal width (cm)': [petal_width]
})

st.subheader("Input Data")
st.write(input_data)

# Prediction
prediction = model.predict(input_data)

#proability
prediction_probablity = model.predict_proba(input_data)

st.subheader("Prediction")
st.write("🌼 Predicted Species:", target_names[prediction[0]])

st.subheader("Prediction Probability")
st.write(pd.DataFrame(
    prediction_probablity,
    columns=target_names
))
