# ML_Assignment_2_2026AK05656
# Heart Disease Classification Using Machine Learning

## Problem Statement

The objective of this project is to predict the presence of heart disease using machine learning classification algorithms. Five different classification models are implemented, evaluated, and compared to identify the best-performing model.

## Dataset Description

Dataset Name: Heart Disease Dataset

Number of Records: 1025

Number of Features: 13

Target Variable: target

Classification Type: Binary Classification

### Features

- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

### Target

- 0 = No Heart Disease
- 1 = Heart Disease

## GitHub Repository Link

Add your GitHub repository link here.

## Models Used

1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (KNN)
4. Naive Bayes Classifier
5. Support Vector Machine (SVM)

## Evaluation Metrics

The following metrics were used to evaluate all models:

- Accuracy
- AUC Score
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)

## Comparison Table

| Model | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---------|---------|---------|---------|---------|---------|---------|
| Logistic Regression | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv |
| Decision Tree | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv |
| KNN | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv |
| Naive Bayes | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv |
| SVM | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv | Refer model_comparison.csv |

## Model Performance Observations

| Model | Observation |
|---------|---------|
| Logistic Regression | Provides good baseline performance and is easy to interpret. |
| Decision Tree | Easy to visualize and interpret decision boundaries. |
| KNN | Performs well for similar neighboring samples but depends on K value. |
| Naive Bayes | Fast training and prediction with reasonable results. |
| Support Vector Machine | Provides strong classification performance and handles complex decision boundaries effectively. |

## Overall Winner

The best-performing model is determined based on the highest accuracy obtained during evaluation.

## Streamlit Application Features

- Upload Test Dataset (CSV)
- Model Selection Dropdown
- Display Evaluation Metrics
- Display Confusion Matrix
- Interactive User Interface

## Repository Contents

- app.py
- requirements.txt
- Assignment2_ML.ipynb
- heart.csv
- test_data.csv
- model_comparison.csv
- logistic.pkl
- decision_tree.pkl
- knn.pkl
- naive_bayes.pkl
- svm.pkl
