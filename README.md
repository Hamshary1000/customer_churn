# 🏦 Sid Bank - Customer Churn Prediction App

An end-to-end data science app built for **Sid Bank** to predict and analyze customer churn using machine learning and interactive dashboards. It enables business users to explore churn drivers and take informed, proactive retention actions.

---

## 📚 Table of Contents

1. [📌 Problem Overview](#-problem-overview)  
2. [🎯 Project Goals](#-project-goals)  
3. [📂 Dataset Description](#-dataset-description)  
4. [🖥️ App Pages](#-app-pages)  
   - [1️⃣ Overview Page](#1️⃣-overview-page)  
   - [2️⃣ Dashboard Page](#2️⃣-dashboard-page)  
     - [📊 Demographic Analysis](#-demographic-analysis)  
     - [📈 Overall Analysis](#-overall-analysis)  
     - [🔍 Insights](#-insights)  
     - [💡 Recommendations](#-recommendations)  
   - [3️⃣ Prediction Page](#3️⃣-prediction-page)  
     - [⚙️ Model Building Process](#️-model-building-process)  
     - [🧠 Techniques Used](#-techniques-used)  
     - [📈 Model Accuracy](#-model-accuracy)  
5. [🚀 How to Run the App Locally](#-how-to-run-the-app-locally)  
6. [🌍 Live Application](#-live-application)  
7. [📫 Contact](#-contact)

---

## 📌 Problem Overview

Customer churn is a pressing issue for banks like **Sid Bank**, where losing existing customers can significantly impact revenue and growth. Identifying potential churners before they leave allows the bank to take action and retain valuable customers.

---

## 🎯 Project Goals

- Predict customer churn using machine learning  
- Uncover key drivers behind churn using interactive dashboards  
- Guide Sid Bank's customer retention strategies  
- Empower business teams with real-time insights and tools

---

## 📂 Dataset Description

| Column Name         | Description |
|---------------------|-------------|
| `RowNumber`         | Row index of the customer |
| `CustomerId`        | Unique customer ID |
| `Surname`           | Customer’s last name |
| `CreditScore`       | Customer’s credit score |
| `Geography`         | Country of residence |
| `Gender`            | Male or Female |
| `Age`               | Age of the customer |
| `Tenure`            | Years with Sid Bank |
| `Balance`           | Account balance |
| `NumOfProducts`     | Number of bank products used |
| `HasCrCard`         | Has a credit card (1 = Yes, 0 = No) |
| `IsActiveMember`    | Active customer (1 = Yes, 0 = No) |
| `EstimatedSalary`   | Estimated yearly salary |
| `Exited`            | Target variable (1 = Churned, 0 = Not)

---

## 🖥️ App Pages

### 1️⃣ [Overview Page](https://customerchurn-predic.streamlit.app/Overview)

#### **Project Summary**

The **Customer Churn Prediction App** is a full-stack data science tool built to detect churn risk among Sid Bank's customers.

#### **Business Benefits**
- Identify and retain at-risk customers  
- Improve customer engagement  
- Enable data-driven decisions for marketing and support teams  

#### **Technologies Used**
- Python & Streamlit  
- Scikit-learn  
- Power BI for dashboard visualizations  
- ML Model: **Random Forest Classifier**

---

### 2️⃣ [Dashboard Page](https://customerchurn-predic.streamlit.app/Dashboard)

The dashboard provides analytical visualizations and is divided into two internal views:

#### 📊 [Demographic Analysis](https://customerchurn-predic.streamlit.app/Dashboard#Demographic-Analysis)

- Churn by **gender**, **country**, and **credit card ownership**
- Customer distribution by **tenure**, **products**, and **age**
![Demographic Page](https://drive.google.com/uc?id=1AbCDeFgHiJklMNopQrStUvWxYZ123456)


#### 📈 [Overall Analysis](https://customerchurn-predic.streamlit.app/Dashboard#Overall-Analysis)

- Summary of churned vs retained customers  
- Overall demographic trends and product usage  
- Visualization of churn percentages and customer behavior patterns
![Overall Page](https://drive.google.com/file/d/1H5DdMSq00sXdbnEzDZ84R0ybQrtHZef_/view?usp=sharing)


---

### 🔍 Insights

- **Total Customers**: 10,000  
- **Churn Rate**: 20% overall  
- **Countries Covered**: France, Germany, Spain  
- **Average Age**: 37  
- **Average Balance**: ~$97.2K  

**Key Observations:**

- **France** has the highest churn volume (1.7K), likely due to a large base  
- **Females** show a higher churn *rate*, while males have more churn *volume*  
- Customers with **10-year tenure** drop significantly (only 490 customers remain)  
- Most customers have only **1–2 products**, indicating low cross-sell  
- **71%** have credit cards, but credit card churn impact needs further study

---

### 💡 Recommendations

- **Target France** with retention programs and tailored offers  
- **Analyze tenure drop-off at 10 years**—consider loyalty rewards for long-term customers  
- **Encourage multi-product adoption** to increase stickiness and engagement  
- **Segment churn by credit card usage** to evaluate its effect on loyalty  
- **Investigate female churn drivers** and tailor gender-specific solutions  
- **Calculate churn rates** (not just raw counts) for more nuanced targeting  
- **Collect more behavioral and financial variables** for deeper insights

---

### 3️⃣ [Prediction Page](https://customerchurn-predic.streamlit.app/Prediction)

This page allows users to enter customer data and get a real-time churn prediction powered by a machine learning model.

---

#### ⚙️ Model Building Process

1. **Data Cleaning**: Handled missing values, duplicates, outliers  
2. **Feature Engineering**: Scaled numeric features, one-hot encoded categoricals  
3. **Train-Test Split**: 80/20  
4. **Pipeline**: End-to-end pipeline using Scikit-learn  
5. **Tuning**: Hyperparameter optimization via GridSearchCV

---

#### 🧠 Techniques Used

- Algorithm: **Random Forest Classifier**  
- Preprocessing: `StandardScaler`, `OneHotEncoder`, `Pipeline`  
- Model Selection: Compared with Logistic Regression, XGBoost  
- Evaluation: Accuracy, F1-score, Precision, Recall

---

#### 📈 Model Accuracy

| Metric    | Value |
|-----------|-------|
| Accuracy  | 85%   |
| Precision | 83%   |
| Recall    | 81%   |
| F1 Score  | 82%   |
