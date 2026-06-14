# 🏦 AI Bank Complaint Analyzer

An NLP-powered web application that automatically classifies customer bank complaints into predefined banking categories using Machine Learning.

## 🚀 Live Demo

https://ai-bank-complaint-analyzer.onrender.com

---

## 📌 Project Overviewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

Banks receive thousands of customer complaints daily. Manually sorting these complaints into relevant departments is time-consuming and inefficient.

This project uses Natural Language Processing (NLP) and Machine Learning to automatically classify complaint text into the appropriate banking category.

---

## ✨ Features

- 🔍 Analyze customer complaint text
- 🤖 Machine Learning based classification
- 📊 Analytics Dashboard
- 📜 Prediction History Tracking
- 🥧 Interactive Complaint Distribution Pie Chart
- 📈 Total Prediction Statistics
- 🌐 Deployed on Render
- 💻 Responsive and modern UI

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Backend
- FastAPI
- Jinja2

### Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Classification Model

### Deployment
- GitHub
- Render

---

## 📂 Project Structure

```text
AI_bank_complaint_analyzer/
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── app.py
├── banking_model.pkl
├── tfidf_vectorizer.pkl
├── complaints.csv
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Workflow

1. Complaint text is entered by the user.
2. Text is transformed using TF-IDF Vectorization.
3. Trained ML model predicts the complaint category.
4. Confidence score is generated.
5. Prediction is displayed on the dashboard.
6. Analytics data is stored and visualized.

---

## 📊 Complaint Categories

The model can classify complaints into categories such as:

- Credit Card Issues
- Card & Fraud Issues
- Mortgages & Loans
- Payments & Fund Transfer
- Account & Banking Services
- Credit Reporting

---

## 📷 Dashboard Features

### Analytics Dashboard
- Total Predictions
- Prediction History
- Complaint Distribution Chart
- Percentage-based Category Analysis

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/shashwat-singh-dev/Ai_bank_complaint_analyzer.git
```

Move into project directory:

```bash
cd Ai_bank_complaint_analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🎯 Future Improvements

- Non-bank complaint detection
- Better confidence calibration
- Advanced NLP preprocessing
- More complaint categories
- User authentication
- Export analytics reports

---

## 👨‍💻 Author

**Shashwat Singh**

B.Tech Student | Machine Learning Enthusiast | Aspiring Data Professional

GitHub:
https://github.com/shashwat-singh-dev

LinkedIn:
[https://www.linkedin.com/in/shashwatpy/]

---

## ⭐ If you found this project useful, consider giving it a star.
