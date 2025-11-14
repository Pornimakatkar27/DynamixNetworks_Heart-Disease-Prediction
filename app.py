import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("heart_rf_pipeline.joblib")

st.set_page_config(page_title="Heart Disease Prediction App", layout="centered")
st.title("Heart Disease Prediction")

st.markdown("""
This app predicts whether a person is **likely to have heart disease** based on medical attributes.  
Fill in the details below and click **Predict**.
""")

# Input form
st.header("Patient Information")

age = st.number_input("Age", min_value=20, max_value=100, value=45)

sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x==0 else "Male")

cp = st.selectbox("Chest Pain Type (cp)", options=["No Pain","Non-anginal pain", "Atypical angina", "Typical angina"])
if cp =="Typical angina":
    cp=0
elif cp == "Atypical angina":
    cp=1
elif cp=="Non-anginal pain":
    cp=2
else:
    cp=3

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)

chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "Yes" if x==1 else "No")

restecg = st.selectbox("Resting ECG Results", options=["Normal ECG","ST-T wave abnormality","Left Ventricular Hypertrophy"])
if restecg =="Normal ECG":
    restecg=0
elif restecg =="ST-T wave abnormality":
    restecg=1
else:
    restecg=2

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)

exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x==1 else "No")

oldpeak = st.number_input("ST Depression (Oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

slope = st.selectbox("Slope of Peak Exercise ST Segment", options=["Upsloping","Flat","Downsloping"])
if slope=="Upsloping":
    slope=0
elif slope=="Flat":
    slope=1
else:
    slope=2
ca = st.selectbox("Number of Major Vessels (0–3)", options=["High Risk","Moderate","normal","low risk"])
if ca=="low risk":
    ca=3
elif ca=="normal":
    ca=2
elif ca=="Moderate":
    ca=1
else:
    ca=0
    
thal = st.selectbox("Thalassemia (thal)", options=["Normal","Fixed defected","Reversible defect"])
if thal=="Normal":
    thal=1
elif thal=="Fixed defected":
    thal=2
else:
    thal=3

# Collect input into a dataframe
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'chest pain': [cp],
    'trestbps': [trestbps],
    'cholesterol': [chol],
    'fbs': [fbs],
    'ECG': [restecg],
    'heart rate': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thalassemia': [thal]
})

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"The model predicts a HIGH chance of Heart Disease.")
        st.error(f"There is {probability*100:.2f}% chance of Heart Disease.")
    else:
        st.success(f"The model predicts a LOW chance of Heart Disease.")
        st.success(f"There is {probability*100:.2f}% chance of Heart Disease.")

st.markdown("---")
st.caption("Built with using Streamlit and Scikit-learn.")

