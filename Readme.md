# 🤝 NeedyConnect – AI-Powered NGO Matchmaking System

NeedyConnect is an AI-powered web application that connects needy individuals with NGOs based on their needs, location, education level, age, and skills. The system uses a Machine Learning model to predict the most suitable NGO category and automatically matches registered individuals with NGOs providing relevant services.

---

## 📌 Features

- 👤 Register needy individuals
- 🏢 Register NGOs and community organizations
- 🤖 AI-based NGO category prediction
- 📍 Location-based NGO matching
- 🎯 Need and service matching
- 💡 Personalized recommendations based on age and skills
- 📋 Interactive Streamlit interface
- ⚡ Instant matching between NGOs and beneficiaries

---

## 🛠️ Technology Stack

- Python
- Streamlit
- Scikit-learn
- Random Forest Classifier
- NumPy
- Joblib
- CountVectorizer
- LabelEncoder

---

## 📂 Project Structure

```
NeedyConnect/
│
├── app.py                  # Streamlit Application
├── ai_model.py             # AI Model Training & Prediction
├── model.pkl               # Trained Random Forest Model
├── vectorizer.pkl          # CountVectorizer
├── edu_encoder.pkl         # Education Label Encoder
├── label_encoder.pkl       # NGO Category Label Encoder
├── requirements.txt
└── README.md
```

---

## 🚀 How It Works

### Step 1
NGOs register by providing:

- NGO Name
- Location
- Services Offered

### Step 2
Needy individuals register with:

- Name
- Age
- Education Level
- Needs
- Skills (Optional)
- Location

### Step 3
The AI model processes the information and predicts the most suitable NGO category such as:

- Education
- Employment
- Shelter

### Step 4
The application searches for NGOs that:

- Belong to the predicted category
- Are located in the same city

### Step 5
Matched NGOs are displayed along with personalized recommendations.

---

## 🧠 Machine Learning Model

The application uses a **Random Forest Classifier** trained on sample beneficiary data.

### Features Used

- Age
- Education Level
- Needs
- Skills

### Prediction Output

- Education NGO
- Employment NGO
- Shelter NGO

---

## 📋 Personalized Recommendations

Depending on the individual's age, the system provides recommendations such as:

### Children (≤18)

- Free education programs
- Child welfare schemes
- Nutrition support

### Adults (19–59)

- Skill development programs
- Employment assistance
- Job recommendations based on skills

### Senior Citizens (60+)

- Elderly care
- Healthcare support
- Social welfare schemes

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/NeedyConnect.git
```

### Move into Project Folder

```bash
cd NeedyConnect
```

### Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📊 Application Modules

### Home

Displays the welcome page.

### Register Needy Individual

Allows users to enter:

- Personal details
- Needs
- Skills
- Education
- Location

### Register NGO

Allows NGOs to register by providing:

- NGO Name
- City
- Services Offered

### View Matches

Displays:

- Matched NGOs
- Beneficiary details
- AI-generated recommendations

---

## 📈 Future Enhancements

- Database integration (MySQL/PostgreSQL)
- NGO login portal
- Beneficiary login portal
- Google Maps integration
- Real-time notifications
- Email and SMS alerts
- Government scheme recommendations
- AI chatbot support
- Multi-language support
- Cloud deployment

---
