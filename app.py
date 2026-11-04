import streamlit as st
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    roc_auc_score,
    confusion_matrix
)

st.title("Heart Disease Classification Using Machine Learning")

uploaded_file = st.file_uploader(
    "Upload test_data.csv",
    type=["csv"]
)

model_name = st.selectbox(
    "Select Model",
    [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Naive Bayes",
        "SVM"
    ]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    X = data.drop("target", axis=1)
    y = data["target"]

    model_files = {
        "Logistic Regression": "logistic.pkl",
        "Decision Tree": "decision_tree.pkl",
        "KNN": "knn.pkl",
        "Naive Bayes": "naive_bayes.pkl",
        "SVM": "svm.pkl"
    }

    model = joblib.load(model_files[model_name])

    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:, 1]

    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    mcc = matthews_corrcoef(y, y_pred)
    auc = roc_auc_score(y, y_prob)

    st.subheader("Evaluation Metrics")

    st.write("Accuracy:", round(accuracy, 4))
    st.write("AUC:", round(auc, 4))
    st.write("Precision:", round(precision, 4))
    st.write("Recall:", round(recall, 4))
    st.write("F1 Score:", round(f1, 4))
    st.write("MCC:", round(mcc, 4))

    st.subheader("Confusion Matrix")

    cm = confusion_matrix(y, y_pred)
    st.write(cm)