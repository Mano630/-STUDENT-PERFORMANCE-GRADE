from pathlib import Path
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Grade Predictor", page_icon="🎓")

@st.cache_resource
def load_model():
    path = Path("/content/student_grade_model.joblib")
    if not path.exists():
        st.error("Model file missing.")
        st.stop()
    return joblib.load(path)

bundle = load_model()
model, feature_columns = bundle["model"], bundle["feature_columns"]

st.title("🎓 Student Grade Predictor")
st.write("Enter student details to predict their final grade.")

with st.form("inputs"):
    l, r = st.columns(2)
    with l:
        age = st.number_input("Age", 14, 19, 16)
        gender = st.selectbox("Gender", ["male", "female", "other"])
        school = st.selectbox("School type", ["public", "private"])
        education = st.selectbox("Parent education", ["no formal", "high school", "diploma", "graduate", "post graduate", "phd"])
        study_hours = st.number_input("Study hours", 0.0, 24.0, 3.0)
        attendance = st.slider("Attendance (%)", 0.0, 100.0, 80.0)
    with r:
        internet = st.selectbox("Internet access", ["yes", "no"])
        travel = st.selectbox("Travel time", ["<15 min", "15-30 min", "30-60 min", ">60 min"])
        activities = st.selectbox("Extra activities", ["yes", "no"])
        method = st.selectbox("Study method", ["notes", "textbook", "group study", "coaching", "mixed", "online videos"])

    st.subheader("Scores")
    c1, c2, c3, c4 = st.columns(4)
    math = c1.number_input("Math", 0.0, 100.0, 60.0)
    science = c2.number_input("Science", 0.0, 100.0, 60.0)
    english = c3.number_input("English", 0.0, 100.0, 60.0)
    overall = c4.number_input("Overall", 0.0, 100.0, 60.0)

    submitted = st.form_submit_button("Predict Grade")

if submitted:
    numerical = {
        "age": age, "study_hours": study_hours, "attendance_percentage": attendance,
        "parent_education": {"no formal": 0, "high school": 1, "diploma": 3, "graduate": 4, "post graduate": 5, "phd": 6}[education],
        "travel_time": {"<15 min": 4, "15-30 min": 3, "30-60 min": 2, ">60 min": 1}[travel],
        "math_score": math, "science_score": science, "english_score": english, "overall_score": overall
    }
    nominal = {"gender": gender, "internet_access": internet, "school_type": school, "study_method": method, "extra_activities": activities}
    indicators = {f"{col}_{val}": 1.0 for col, val in nominal.items()}

    encoded_row = {}
    for col in feature_columns:
        name = col.split("__", 1)[-1]
        if name in numerical:
            encoded_row[col] = numerical[name]
        else:
            encoded_row[col] = indicators.get(name, 0.0)

    X_input = pd.DataFrame([encoded_row], columns=feature_columns)
    pred = model.predict(X_input)[0]
    probs = model.predict_proba(X_input)[0]

    grade_map = {1: "F", 2: "E", 3: "D", 4: "C", 5: "B", 6: "A"}
    st.success(f"Predicted Grade: {grade_map.get(pred, str(pred))}")
    st.metric("Confidence", f"{probs.max():.1%}")

    fig, ax = plt.subplots(figsize=(6, 3.5))
    labels = [grade_map.get(c, str(c)) for c in model.classes_]
    bars = ax.bar(labels, probs, color=["#16856b" if c == pred else "#86b6d9" for c in model.classes_])
    ax.bar_label(bars, labels=[f"{p:.1%}" for p in probs], padding=2)
    ax.set(title="Grade Probability Distribution", ylim=(0, 1.15))
    st.pyplot(fig)
