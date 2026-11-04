# Heart Disease Classification Using Machine Learning

## Problem Statement

The objective of this project is to predict the presence of heart disease using machine learning classification algorithms. Five different classification models are implemented, evaluated, and compared to identify the best-performing model.

---

## Dataset Description

**Dataset Name:** Heart Disease Dataset

**Number of Records:** 1025

**Number of Features:** 13

**Target Variable:** `target`

**Classification Type:** Binary Classification

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

---

## GitHub Repository Link

**Repository:**

<https://github.com/hemalathasadula999/Assignment_ML>

---

## Models Used

1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (KNN)
4. Naive Bayes Classifier
5. Support Vector Machine (SVM)

---

## Evaluation Metrics

The following metrics were used to evaluate all models:

- Accuracy
- AUC Score
- Precision
- Recall
- F1 Score
- Matthews Correlation Coefficient (MCC)

---

## Comparison Table

| Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|---------|---------|---------|---------|---------|---------|---------|
| Logistic Regression | 0.8146 | 0.9299 | 0.7638 | 0.9238 | 0.8362 | 0.6422 |
| Decision Tree | 0.9854 | 0.9857 | 1.0000 | 0.9714 | 0.9855 | 0.9712 |
| KNN | 0.6976 | 0.8335 | 0.7129 | 0.6857 | 0.6990 | 0.3956 |
| Naive Bayes | 0.8293 | 0.9043 | 0.8070 | 0.8762 | 0.8402 | 0.6602 |
| Support Vector Machine | 0.7171 | 0.7477 | 0.6975 | 0.7905 | 0.7411 | 0.4360 |

---

## Model Performance Observations

| Model | Observation |
|---------|-------------|
| Logistic Regression | Achieved good classification performance with high recall and strong AUC score. Suitable as a reliable baseline model. |
| Decision Tree | Achieved the best overall performance across all evaluation metrics. Produced the highest accuracy, precision, F1 score and MCC. |
| KNN | Produced moderate performance. Accuracy and MCC were lower compared to other models and performance depends on neighborhood selection. |
| Naive Bayes | Delivered strong overall performance with high recall, F1 score and MCC. It was the second-best performing model after Decision Tree. |
| Support Vector Machine | Produced acceptable classification results but performed lower than Logistic Regression, Decision Tree and Naive Bayes on this dataset. |

---

## Overall Winner for the Dataset

### 🏆 Decision Tree Classifier

The Decision Tree Classifier achieved the best overall performance on the Heart Disease Dataset.

### Performance Summary

- Accuracy = **98.54%**
- AUC Score = **98.57%**
- Precision = **100.00%**
- Recall = **97.14%**
- F1 Score = **98.55%**
- MCC = **97.12%**

Therefore, the **Decision Tree Classifier** is selected as the best-performing model for this dataset.

---

## Streamlit Application Features

- Upload Test Dataset (CSV)
- Model Selection Dropdown
- Display Accuracy, AUC, Precision, Recall, F1 Score and MCC
- Display Confusion Matrix
- Interactive User Interface

---

## Repository Contents

- app.py
- requirements.txt
- README.md
- heart.csv
- test_data.csv
- model_comparison.csv
- Assignment2_ML.ipynb
- logistic.pkl
- decision_tree.pkl
- knn.pkl
- naive_bayes.pkl
- svm.pkl

---

## Streamlit Application

Upload the provided **test_data.csv** file, select a machine learning model, and view:

- Accuracy
- AUC Score
- Precision
- Recall
- F1 Score
- MCC Score
- Confusion Matrix

through the interactive Streamlit web application.

---

## Conclusion

This project successfully implemented and compared five machine learning classification models for Heart Disease Prediction. Based on the evaluation metrics, the **Decision Tree Classifier** achieved the highest overall performance and emerged as the most suitable model for this dataset.
