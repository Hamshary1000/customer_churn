# Customer Churn Prediction App

## Overview
The Customer Churn Prediction App is an end-to-end data science project that predicts customer churn (likelihood of discontinuing a service) using a robust machine learning pipeline. This app is designed to help businesses take proactive steps to retain customers by identifying high-risk groups and providing actionable insights.

---

## Project Workflow

1. **Importing Libraries**: Essential libraries like Pandas, NumPy, Matplotlib, Scikit-learn, and Streamlit are utilized.
2. **Loading the Dataset**: The customer churn dataset is loaded and inspected for completeness.
3. **Data Exploration**:
   - **Univariate Analysis**: Analysis of individual features to understand distributions and anomalies.
   - **Bivariate Analysis**: Examining relationships between features and the target variable.
   - **Multivariate Analysis**: Exploring interactions among multiple features.
4. **Data Cleaning**:
   - Handling missing values.
   - Removing duplicates.
   - Addressing outliers.
5. **Feature Engineering**:
   - **Scaling**: Standardization or normalization of numerical features.
   - **Encoding**: Transforming categorical variables using techniques like one-hot encoding.
6. **Data Splitting**: Splitting the dataset into training and testing sets.
7. **Pipeline Building**: Creating a machine learning pipeline to automate preprocessing and modeling.
8. **Hyperparameter Tuning**: Using Grid Search to find the best model parameters.
9. **Model Evaluation**: Evaluating the model using metrics such as accuracy, precision, recall, and F1-score.
10. **Deployment**: Developing a Streamlit app for user interaction and deploying the model.

---

## Features
1. **End-to-End Workflow**: Covers all stages of a data science project.
2. **Interactive App**: A user-friendly interface built with Streamlit for exploring predictions.
3. **Data Insights**: Provides detailed insights into customer behavior and churn drivers.

---

## Technology Stack
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit
- **Machine Learning Techniques**: Hyperparameter tuning, pipeline automation
- **Deployment**: Streamlit

---

## Dataset
The dataset includes the following columns:

- **RowNumber**: Index of the customer in the dataset
- **CustomerId**: Unique identifier for the customer
- **Surname**: Customer's surname
- **CreditScore**: Customer's credit score
- **Geography**: Country of residence
- **Gender**: Customer's gender
- **Age**: Customer's age
- **Tenure**: Number of years the customer has been with the company
- **Balance**: Customer's account balance
- **NumOfProducts**: Number of products the customer has subscribed to
- **HasCrCard**: Whether the customer owns a credit card (1: Yes, 0: No)
- **IsActiveMember**: Whether the customer is an active member (1: Yes, 0: No)
- **EstimatedSalary**: Estimated salary of the customer
- **Exited**: Target variable indicating whether the customer churned (1: Yes, 0: No)

---

## Key Insights from the Project
1. **High-Risk Groups**: Customers with low credit scores, short tenures, and multiple products are more likely to churn.
2. **Impact of Geography**: Customers from certain regions exhibit higher churn rates.
3. **Model Performance**: Achieved an accuracy of 85% with hyperparameter-tuned models.

---




