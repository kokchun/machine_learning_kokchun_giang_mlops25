import streamlit as st
import httpx
import pandas as pd 

URL = "http://127.0.0.1:8000"

st.markdown("# Predict iris flower")
st.markdown("App to predict an Iris flower, take some measurement on your flower")

with st.form("iris_data"):
    sepal_length = st.number_input(
        "Sepal length (cm)", min_value=3.8, max_value=8.4, value=6.0
    )
    sepal_width = st.number_input(
        "Sepal width (cm)", min_value=1.5, max_value=4.9, value=3.0
    )
    petal_length = st.number_input(
        "Petal length (cm)", min_value=0.5, max_value=7.4, value=4.0
    )
    petal_width = st.number_input(
        "Petal width (cm)", min_value=0.1, max_value=3.0, value=2.0
    )

    submitted = st.form_submit_button("PREDICT")

# st.markdown(submitted)


if submitted:
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    response = httpx.post(f"{URL}/api/predict", json=payload)
    prediction = response.json().get("predicted_flower")
    st.markdown(f"**Predicted flower:** {prediction}")


st.markdown("## Raw data")

data = httpx.get(f"{URL}/api/data").json()
df = pd.DataFrame(data)

st.dataframe(df)