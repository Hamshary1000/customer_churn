import streamlit as st
import numpy as np
import joblib

# Set page configuration
st.set_page_config(page_title="Customer Churn App", layout="wide", page_icon="📊")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📋 Overview", "📈 Dashboard", "🔍 Prediction"])

# ---------------------
# Tab 1: Overview
# ---------------------
with tab1:
    st.title("📊 Customer Churn Prediction App")
    st.image("original.png", use_column_width=True)
    
    st.markdown("""
    ### Project Summary:
    The **Customer Churn Prediction App** is an end-to-end data science solution that uses machine learning to identify customers who are likely to churn (leave a service).  
    
    This helps businesses:
    - Take proactive steps to retain at-risk customers.
    - Improve customer engagement strategies.
    - Make data-driven decisions.

    **Technologies Used:**
    - Python & Streamlit
    - Scikit-learn
    - Power BI for Dashboard Visualization
    - Machine Learning Model: Random Forest Classifier
    """)

# ---------------------
# Tab 2: Dashboard
# ---------------------
with tab2:
    st.title("📈 Churn Analytics Dashboard")
    st.markdown("This interactive dashboard provides insights into customer churn data.")
    st.markdown("[🔗 View Full Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmEwMDBmZDctYTU2Yy00OWUxLTk0ZDktMWEyZmUxMjU5MTNjIiwidCI6IjJiYjZlNWJjLWMxMDktNDdmYi05NDMzLWMxYzZmNGZhMzNmZiIsImMiOjl9)")
    
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiZmEwMDBmZDctYTU2Yy00OWUxLTk0ZDktMWEyZmUxMjU5MTNjIiwidCI6IjJiYjZlNWJjLWMxMDktNDdmYi05NDMzLWMxYzZmNGZhMzNmZiIsImMiOjl9",
        height=600,
        width=1000
    )

# ---------------------
# Tab 3: Prediction
# ---------------------
with tab3:
    st.title("🔍 Predict Customer Churn")
    st.markdown("Fill in the customer's details below:")

    # Input fields
    CreditScore = st.number_input('Credit Score')
    Geography = st.radio('Country', ['Germany', 'Spain', 'France'])
    Age = st.slider('Age', 18, 62)
    Tenure = st.number_input('Tenure')
    Balance = st.number_input('Balance')
    NumOfProducts = st.number_input('No. of Products')
    HasCrCard = st.selectbox('Credit Card', ['Yes', 'No'])
    IsActiveMember = st.selectbox('Active Member', ['Yes', 'No'])
    EstimatedSalary = st.number_input('Estimated Salary')
    Gender = st.selectbox('Gender', ['Male', 'Female'])

    if st.button("Submit"):
        try:
            # Load model and scalers
            model = joblib.load('rf_model.pkl')
            scaler = joblib.load('X_scaled.pkl')
            target_scaler = joblib.load('y_scaled.pkl')

            # Encode inputs
            geography_mapping = {'France': 0, 'Germany': 1, 'Spain': 2}
            gender_mapping = {'Female': 0, 'Male': 1}
            yes_no_mapping = {'Yes': 1, 'No': 0}

            input_data = np.array([[
                CreditScore,
                geography_mapping[Geography],
                Age,
                Tenure,
                Balance,
                NumOfProducts,
                yes_no_mapping[HasCrCard],
                yes_no_mapping[IsActiveMember],
                EstimatedSalary,
                gender_mapping[Gender]
            ]])

            # Scale and predict
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)

            if prediction[0] == 1:
                st.success("🚨 The customer is **likely to churn**.")
            else:
                st.success("✅ The customer is **not likely to churn**.")
        except Exception as e:
            st.error(f"⚠️ An error occurred during prediction: {e}")

        



    
