import joblib
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def train_and_save_model():
    data = [
        {"age": 10, "education": "none", "needs": "education, food", "skills": "", "ngo_category": "Education"},
        {"age": 35, "education": "highschool", "needs": "employment, skill development", "skills": "carpentry", "ngo_category": "Employment"},
        {"age": 70, "education": "none", "needs": "health care, shelter", "skills": "", "ngo_category": "Shelter"},
        {"age": 25, "education": "college", "needs": "skill development", "skills": "computer", "ngo_category": "Employment"},
        {"age": 15, "education": "middle school", "needs": "education, food", "skills": "", "ngo_category": "Education"},
        {"age": 60, "education": "none", "needs": "health care", "skills": "", "ngo_category": "Shelter"},
    ]

    needs_corpus = [d['needs'] + " " + d['skills'] for d in data]
    ages = [d['age'] for d in data]
    education_levels = [d['education'] for d in data]
    labels = [d['ngo_category'] for d in data]

    vectorizer = CountVectorizer()
    X_text = vectorizer.fit_transform(needs_corpus)

    edu_encoder = LabelEncoder()
    edu_encoded = edu_encoder.fit_transform(education_levels)

    X = np.hstack([
        np.array(ages).reshape(-1,1),
        edu_encoded.reshape(-1,1),
        X_text.toarray()
    ])

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)

    clf = RandomForestClassifier()
    clf.fit(X, y)

    joblib.dump(clf, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(edu_encoder, 'edu_encoder.pkl')
    joblib.dump(label_encoder, 'label_encoder.pkl')

def predict_ngo_category(age, education, needs, skills):
    clf = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    edu_encoder = joblib.load('edu_encoder.pkl')
    label_encoder = joblib.load('label_encoder.pkl')

    text = f"{needs} {skills}"
    text_vec = vectorizer.transform([text]).toarray()

    try:
        edu_enc = edu_encoder.transform([education])[0]
    except ValueError:
        edu_enc = 0

    X_new = np.hstack([
        np.array(age).reshape(-1,1),
        np.array(edu_enc).reshape(-1,1),
        text_vec
    ])

    pred = clf.predict(X_new)
    category = label_encoder.inverse_transform(pred)[0]
    return category

if __name__ == '__main__':
    train_and_save_model()
    print("Model trained and saved.")