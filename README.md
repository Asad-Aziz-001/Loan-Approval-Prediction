  # Loan-Approval-Prediction


# **Online Run this Project**

https://loan-approval-prediction-zfmdblquqg9n57cqeznhkp.streamlit.app/

# **🔍 Project Overview**

The Loan Approval Predictor is a machine learning-based system that takes input features about a loan applicant (like income, credit history, marital status, etc.) and predicts whether their loan will be approved or rejected.

# **🛠️ Project Workflow**

**1. Data Collection**

The dataset (usually from Kaggle) includes columns such as:

Gender, Married, Education, ApplicantIncome, LoanAmount, Credit_History, etc.

The target variable is usually Loan_Status (Yes/No or 1/0).

**2. Data Preprocessing**

Handling Missing Values: Fill or drop nulls in columns like LoanAmount, Gender, etc.

Encoding Categorical Variables: Convert strings (e.g., Male, Female) to numerical values using Label Encoding or One-Hot Encoding.

Feature Scaling (optional): Standardize numerical features to bring them to a common scale.

Data Splitting: Split dataset into training and testing sets, commonly in a 80/20 or 70/30 ratio.

# **3. Model Training**

ML Algorithms Used: Common ones include:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Support Vector Machine (SVM)

The models learn patterns from the training data to distinguish between loan approval and rejection cases.

# **4. Model Evaluation**

Metrics Used:

Accuracy: Overall correct predictions.

Precision & Recall: Focus on class-specific performance.

Confusion Matrix: True Positive, False Positive, etc.

Best performing model is selected based on test performance.

# **5. Model Saving**

The best model is saved using pickle or joblib, allowing future reuse without retraining.

# **6. Frontend Interface (Streamlit)**

The saved model is used in a Streamlit app:

Users input values (like income, education, credit history).

The app loads the model, processes the input, and shows a prediction ("Approved" or "Rejected").

# **✅ Final Output**

The final result for any new applicant is displayed as:

Loan Approved ✅

Loan Rejected ❌

