# 🏦 Sid Bank - Customer Churn Prediction App

An interactive machine learning app designed to help **Sid Bank** identify and prevent customer churn. It provides business users with actionable insights and a predictive tool to improve retention.

---

## 📚 Table of Contents

1. [📌 Problem Overview](#-problem-overview)  
2. [🎯 Project Goals](#-project-goals)  
3. [📂 Dataset Description](#-dataset-description)  
4. [🖥️ App Pages](#-app-pages)  
   - [1️⃣ Overview Page](#1️⃣-overview-page)  
   - [2️⃣ Dashboard Page](#2️⃣-dashboard-page)  
     - [📍 Sub-Page 1: Churn Summary](#-sub-page-1-churn-summary)  
     - [📍 Sub-Page 2: Feature Impact](#-sub-page-2-feature-impact)  
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

Churn prediction is crucial for **Sid Bank**, where retaining customers is more cost-effective than acquiring new ones. This app identifies at-risk customers and empowers the business to take proactive actions.

---

## 🎯 Project Goals

- Predict customer churn using machine learning.
- Provide interpretable insights via dashboards.
- Help Sid Bank take strategic actions to improve retention.

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

A summary page introducing:

- What churn is
- Why it's important for Sid Bank
- The app’s purpose and how to use it

---

### 2️⃣ [Dashboard Page](https://customerchurn-predic.streamlit.app/Dashboard)

This section provides **interactive visualizations** and is divided into two internal tabs:

#### 📍 [Sub-Page 1: Churn Summary](https://customerchurn-predic.streamlit.app/Dashboard#churn-summary)

- Overall churn rate
- Churn by geography, gender, tenure
- Bar charts, pie charts, and filters

#### 📍 [Sub-Page 2: Feature Impact](https://customerchurn-predic.streamlit.app/Dashboard#feature-impact)

- Relationship between churn and:
  - Credit score
  - Age
  - Number of products
  - Balance and active membership
- Correlation heatmap

#### 🔍 Insights

- **Low credit scores**, **short tenures**, and **multiple products** increase churn risk.
- **Inactive members** churn more frequently.
- **Geography matters**: Germany shows the highest churn rate.
- Customers aged **35–50** show the highest churn trends.

#### 💡 Recommendations

- Target **low-tenure** customers with loyalty benefits.
- Promote **product bundling** to reduce churn.
- Implement **personalized outreach** to inactive members.
- Focus retention efforts on **German customers**.
- Offer onboarding programs to improve early-year retention.

---

### 3️⃣ [Prediction Page](https://customerchurn-predic.streamlit.app/Prediction)

Allows you to enter customer details and get a real-time churn prediction.

#### ⚙️ Model Building Process

1. Data cleaned (nulls, outliers, duplicates removed)
2. Features encoded and scaled
3. Data split into training and test sets
4. Built ML pipeline with preprocessing + modeling
5. Hyperparameter tuning via GridSearchCV

#### 🧠 Techniques Used

- Algorithms tested: Logistic Regression, Random Forest, XGBoost
- Best model: **XGBoost**
- Feature engineering: One-hot encoding, standardization
- Evaluation metrics: Accuracy, Precision, Recall, F1

#### 📈 Model Accuracy

| Metric        | Value |
|---------------|-------|
| Accuracy      | 85%   |
| Precision     | 83%   |
| Recall        | 81%   |
| F1 Score      | 82%   |








