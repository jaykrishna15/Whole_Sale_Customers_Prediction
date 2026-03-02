import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
with open("knn_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Wholesale Customer Prediction", page_icon="🛒")

st.title("🛒 Wholesale Customer Channel Classification")
st.markdown("Enter the **annual spending** in each product category below:")

st.divider()

col1, col2 = st.columns(2)

with col1:
    fresh = st.number_input("🥦 Fresh", min_value=0.0, step=100.0, format="%.2f")
    milk = st.number_input("🥛 Milk", min_value=0.0, step=100.0, format="%.2f")
    grocery = st.number_input("🛍️ Grocery", min_value=0.0, step=100.0, format="%.2f")

with col2:
    frozen = st.number_input("🧊 Frozen", min_value=0.0, step=100.0, format="%.2f")
    delicassen = st.number_input("🧀 Delicassen", min_value=0.0, step=100.0, format="%.2f")

st.divider()

if st.button("🔍 Predict Channel", use_container_width=True):

    input_data = pd.DataFrame({
        "Fresh": [fresh],
        "Milk": [milk],
        "Grocery": [grocery],
        "Frozen": [frozen],
        "Delicassen": [delicassen]
    })

    try:
        prediction = model.predict(input_data)[0]

        st.divider()
        if prediction == 1:
            st.success("✅ Predicted Channel: **HORECA** (Hotel / Restaurant / Cafe)")
            st.info("This customer likely belongs to the **Hotel, Restaurant, or Cafe** segment.")
        else:
            st.success("✅ Predicted Channel: **Retail**")
            st.info("This customer likely belongs to the **Retail** segment.")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
