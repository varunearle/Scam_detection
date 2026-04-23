# 🏦 AI-Based Scam Detection for Banking Messages

## 📌 Overview

This project presents an **AI-based system** that detects phishing and scam messages in banking communication using **Natural Language Processing (NLP)** and machine learning.
The system analyzes text messages and classifies them as **Safe, Suspicious, or High Risk**, helping users avoid financial fraud.

---

## 🚀 Features

* Detects scam messages in real-time
* Classifies messages into **3 risk levels**
* Provides **confidence score**
* Highlights **suspicious keywords**
* Simple **web interface (Streamlit)**

---

## 🧠 Tech Stack

* **Language:** Python
* **Libraries:** Scikit-learn, pandas
* **NLP:** CountVectorizer
* **Model:** Logistic Regression
* **Deployment:** Streamlit
* **Platform:** Google Colab

---

## ⚙️ How It Works

1. User inputs a message
2. Text is preprocessed using NLP
3. Converted into numerical features
4. Model predicts scam probability
5. Output: Safe / Suspicious / High Risk

---

## 📊 Sample Output

```
Input: Your account is blocked, click here now
Output: 🚨 HIGH RISK Scam (85%)
Keywords: click, blocked
```

---

## 📂 Project Structure

```
├── app.py
├── requirements.txt
├── README.md
├── dataset (optional)
```

## 🌐 Deployment

The project can be deployed using **Streamlit Cloud** for a live web application.

##depoly link 
https://scamdetection-mspwwsjg43t6r8pstsxhlh.streamlit.app/



## 🎯 Future Improvements

* Use **LSTM / Transformer models**
* Improve dataset size
* Mobile app integration
* Real-time SMS detection



## 👨‍💻 Authors

* **Earle Varun Sai (AP24110010555)**
* **Saideep Reddy Mallidi (AP24110010548)**


