import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
model = pickle.load(open("knn_pipeline.pkl", "rb"))

st.title("Wholesale Customer Channel Classification")

st.write("Enter annual spending in each category:")

# Input fields (ONLY 5 FEATURES)
fresh = st.number_input("Fresh", min_value=0.0)
milk = st.number_input("Milk", min_value=0.0)
grocery = st.number_input("Grocery", min_value=0.0)
frozen = st.number_input("Frozen", min_value=0.0)
delicassen = st.number_input("Delicassen", min_value=0.0)

if st.button("Predict Channel"):

    # Create DataFrame with EXACT same columns as training
    input_data = pd.DataFrame({
        "Fresh": [fresh],
        "Milk": [milk],
        "Grocery": [grocery],
        "Frozen": [frozen],
        "Delicassen": [delicassen]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Predicted Channel: HORECA (Hotel/Restaurant/Cafe)")
    else:
        st.success("Predicted Channel: Retail")