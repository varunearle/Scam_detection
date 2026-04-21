import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "text": [
        "Free entry win cash prize now",
        "Your account is blocked click this link",
        "Win iPhone click here",
        "Urgent update your KYC now",
        "Meeting at 5 pm",
        "Your bank OTP is 1234",
        "Your balance is 20000",
        "Salary credited successfully"
    ],
    "label": [1,1,1,1,0,0,0,0]
}

df = pd.DataFrame(data)

# Model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

# UI
st.title("🏦 Scam Detection for Banking Messages")

msg = st.text_input("Enter your message")

if st.button("Check"):
    msg_vec = vectorizer.transform([msg])
    prob = model.predict_proba(msg_vec)[0][1]

    if prob > 0.7:
        st.error(f"🚨 HIGH RISK Scam ({prob*100:.2f}%)")
    elif prob > 0.4:
        st.warning(f"⚠️ Suspicious ({prob*100:.2f}%)")
    else:
        st.success(f"✅ Safe ({(1-prob)*100:.2f}%)")
