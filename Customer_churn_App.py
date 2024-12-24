import streamlit as st 
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


# Page setting
st.set_page_config(page_title="Customer Churn App", layout="centered", page_icon="📊")
 
st.title("Customer Churn Prediction App")
st.image('original.png')

st.text("Fill-in the following values to predict the customer churn")

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

btn = st.button("Submit")


if btn == True :
    # loading model and scalers
    model =joblib.load('rf_model.pkl')
    scaler =joblib.load('X_scaled.pkl')
    target_scaler =joblib.load('y_scaled.pkl')
    # France : 0 
    # Germany : 1 
    # spain : 2 
    # Exited : 1 
    # Not Exited : 0 
    # Male= 1
    # Female =0 
    


    # encoding and scaling input
    Geograohy_mapping = {'France': 0, 'Germany': 1,'Spain':2}
    Gender_mapping = {'Female': 0, 'Male': 1}
    HasCrCard_mapping ={'Yes':1 ,'No':0}
    IsActiveMember_mapping ={'Yes':1 ,'No':0}

    Gender_encoded = Gender_mapping [Gender]
    Geography_encoded = Geograohy_mapping [Geography]
    HasCrCard_encoded = HasCrCard_mapping [HasCrCard]
    IsActiveMember_encoded = IsActiveMember_mapping [IsActiveMember]


    input_data=np.array([[CreditScore,Geography_encoded,Age,Tenure,Balance,NumOfProducts,HasCrCard_encoded,IsActiveMember_encoded,EstimatedSalary,Gender_encoded]])
    input_data_scaled = scaler.transform(input_data)
    prediction_scaled = model.predict(input_data_scaled)
       
    if prediction_scaled == 1 :
        st.success('Yes ')
    else :
        st.success('No')
        



    