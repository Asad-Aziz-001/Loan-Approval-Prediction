import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# App config
st.set_page_config(page_title="Loan Approval Prediction", page_icon="💳", layout="centered")

# -------------------------------------------------------------------------
# 1. Load Model
# -------------------------------------------------------------------------
MODEL_CANDIDATES = ["loan_model.pkl", "loan_model .pkl"]
model = None
load_error = None

for fname in MODEL_CANDIDATES:
    try:
        if os.path.exists(fname):
            with open(fname, "rb") as f:
                if os.path.getsize(fname) > 0:
                    model = pickle.load(f)
                    break
                else:
                    load_error = f"File '{fname}' is empty (0 bytes)"
    except Exception as e:
        load_error = f"Error loading '{fname}': {str(e)}"

if model is None:
    st.error("❌ Model loading failed.\n\n"
             f"Error: {load_error or 'Unknown error'}\n\n"
             "Please ensure:\n"
             "1. `loan_model.pkl` is present\n"
             "2. It is not empty or corrupted\n"
             "3. It was saved with `pickle.dump()`")
    st.stop()

# -------------------------------------------------------------------------
# 2. Sidebar Instructions
# -------------------------------------------------------------------------
with st.sidebar:
    st.title("📘 Guide")
    st.markdown("""
    This app predicts the **likelihood of loan approval** based on:
    - Applicant details
    - Income & loan info
    - Credit history
    
    ✅ Make sure all fields are filled correctly.
    """)

# -------------------------------------------------------------------------
# 3. Title
# -------------------------------------------------------------------------
st.markdown("<h1 style='text-align: center;'>💳 Credit Risk Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Fill in the details to check if a loan is likely to be approved.</p>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------------------------------------------------
# 4. Form Layout
# -------------------------------------------------------------------------
with st.form("loan_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self-Employed", ["Yes", "No"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    with col2:
        applicant_income = st.number_input("Applicant Income", min_value=0)
        coapplicant_income = st.number_input("Co-applicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_term = st.selectbox("Loan Amount Term (months)",
                                 [360.0, 300.0, 240.0, 180.0, 120.0, 84.0, 60.0, 12.0])
        credit_history = st.selectbox("Credit History", [1.0, 0.0], format_func=lambda x: "Good (1)" if x == 1.0 else "Bad (0)")

    submitted = st.form_submit_button("🔍 Predict Loan Approval")

# -------------------------------------------------------------------------
# 5. Prediction Logic
# -------------------------------------------------------------------------
if submitted:
    try:
        encoded = np.array([[
            1 if gender == "Male" else 0,
            1 if married == "Yes" else 0,
            {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
            1 if education == "Graduate" else 0,
            1 if self_employed == "Yes" else 0,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]
        ]])

        cols = [
            "Gender", "Married", "Dependents", "Education", "Self_Employed",
            "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
            "Loan_Amount_Term", "Credit_History", "Property_Area"
        ]
        input_df = pd.DataFrame(encoded, columns=cols)

        prediction = model.predict(input_df)[0]

        st.markdown("---")
        if prediction in [1, "Y"]:
            st.success("🎉 Loan is **likely to be Approved!**")
        else:
            st.error("🚫 Loan is **likely to be Rejected.**")

    except Exception as e:
        st.error(f"⚠️ Something went wrong: {str(e)}")
