# -STUDENT-PERFORMANCE-GRADE
# 🎓 Student Performance Prediction System

A machine learning project that analyzes student-related data and predicts final academic grades using classification algorithms. The project includes data preprocessing, exploratory data analysis (EDA), model training, performance evaluation, and an interactive Streamlit application for grade prediction.

## 📌 Project Overview

The **Student Performance Prediction System** aims to use student demographic, academic, and study-related information to predict final grade categories.

The project explores multiple classification algorithms, compares their performance using evaluation metrics, and implements a Gradient Boosting classifier for an interactive prediction interface.

## 🎯 Objectives

- Analyze student performance data using exploratory data analysis.
- Identify patterns and relationships between student characteristics and academic outcomes.
- Clean and preprocess the dataset for machine learning.
- Encode categorical variables using appropriate encoding techniques.
- Train and compare multiple classification models.
- Evaluate models using accuracy, precision, recall, F1-score, and balanced accuracy.
- Develop an interactive application using Streamlit.
- Save the trained model for reuse without retraining.

## 📂 Dataset Description

The dataset contains **25,001 rows and 16 columns**, as reported in the notebook.

The features cover student demographics, study habits, attendance, educational background, and academic scores.

| Feature | Description |
|---|---|
| `student_id` | Unique student identifier |
| `age` | Student's age |
| `gender` | Gender category |
| `school_type` | Type of school |
| `parent_education` | Parent's educational background |
| `study_hours` | Time spent studying |
| `attendance_percentage` | Student attendance percentage |
| `internet_access` | Availability of internet access |
| `travel_time` | Time required to travel to school |
| `extra_activities` | Participation in extracurricular activities |
| `study_method` | Preferred study method |
| `math_score` | Mathematics score |
| `science_score` | Science score |
| `english_score` | English score |
| `overall_score` | Overall academic score |
| `final_grade` | Target variable representing the final grade |

**Note:** Place the dataset file in the appropriate project directory before running the notebook. The notebook currently references `Student_Performance.csv`.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Additional Models:** XGBoost, LightGBM
- **Model Persistence:** Joblib
- **Interactive Application:** Streamlit
- **Development Environment:** Google Colab / Jupyter Notebook
- **Version Control:** Git and GitHub

## ⚙️ Project Workflow

### 1. Data Loading and Inspection
- Load the dataset using Pandas.
- Examine the dataset's dimensions, columns, and data types.
- Inspect unique values and identify duplicate records.

### 2. Data Cleaning
- Check for missing values.
- Identify and remove duplicate rows.
- Inspect categorical and numerical features.

### 3. Exploratory Data Analysis (EDA)
- Analyze the distribution of final grades.
- Explore relationships between study methods and academic outcomes.
- Examine categorical feature distributions.
- Investigate patterns across academic and demographic variables.

### 4. Data Preprocessing
- Map ordinal categories such as parent education and travel time to numerical values.
- Apply One-Hot Encoding to nominal categorical variables.
- Handle missing numerical values using median imputation where required.
- Separate the input features from the target variable.
- Split the data into training and testing sets.

### 5. Model Training and Comparison

The notebook explores several classification algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- LightGBM
- XGBoost

The models are compared to understand their predictive performance.

### 6. Model Evaluation

The evaluation process includes:

- Accuracy
- Balanced accuracy
- Precision
- Recall
- Macro F1-score
- Weighted F1-score
- Confusion matrix
- Classification report

These metrics help assess overall predictive performance and performance across individual grade categories.

### 7. Model Saving

The selected Gradient Boosting model is saved using Joblib, along with its expected feature-column information, for reuse in the prediction application.

### 8. Streamlit Application

The interactive application allows users to enter student information, including academic scores, attendance, study hours, and study-related characteristics.

After submitting the inputs, the application processes the information and displays the predicted final grade.

## 📊 Model Performance

The notebook reports the following results for the Gradient Boosting classifier:

| Evaluation Metric | Result |
|---|---:|
| 5-fold cross-validation accuracy | 99.71% ± 0.10% |
| Cross-validation balanced accuracy | 99.69% ± 0.10% |
| Cross-validation macro F1-score | 99.71% ± 0.07% |
| Test accuracy | 99.60% |
| Test balanced accuracy | 99.46% |

The held-out test set contains 3,000 observations, based on the reported 80:20 train-test split.

**Important evaluation note:** These results should be interpreted carefully. The input features include `math_score`, `science_score`, `english_score`, and `overall_score`, while the target is `final_grade`. If the final grade is calculated directly or indirectly from these scores, target leakage may explain the unusually high accuracy. A more reliable assessment should verify the grade-generation rule and evaluate the model using only features available before the final grade is determined.

## 🚀 Getting Started

### Prerequisites

Install Python and the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

Install these additional packages if you intend to run the corresponding models:

```bash
pip install xgboost lightgbm
```

### Step 1: Clone the Repository

```bash
git clone https://github.com/Mano630/Student-Performance-Prediction.git
cd Student-Performance-Prediction
```

Replace the repository URL with your actual GitHub repository URL if the repository has a different name.

### Step 2: Prepare the Dataset

Place `Student_Performance.csv` in the directory expected by the notebook.

### Step 3: Run the Notebook

Open the notebook in Google Colab or Jupyter Notebook and execute the cells in sequence.

The notebook performs data analysis, preprocessing, model training, evaluation, and model export.

### Step 4: Run the Streamlit Application

After generating the model artifact and preparing `app.py`, run:

```bash
streamlit run app.py
```

Make sure the application loads `student_grade_model.joblib` from the correct local directory. If necessary, update the model path in `app.py`.

## 📁 Suggested Repository Structure

```text
Student-Performance-Prediction/
│
├── Student_Performance.csv
├── Student_Performance_Prediction.ipynb
├── app.py
├── student_grade_model.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

The dataset and model artifact should be committed only if you have permission to redistribute them. Large files can be managed using Git LFS or suitable external storage.

## 🔮 Future Improvements

- Investigate target leakage and improve the validity of the prediction task.
- Perform hyperparameter tuning using cross-validation.
- Compare models using class-wise precision, recall, and F1-score.
- Use features available before the final academic outcome is known.
- Add feature-importance analysis and explainable machine learning.
- Improve the Streamlit interface with prediction probabilities and visual summaries.
- Package preprocessing and prediction into a reproducible pipeline.
- Deploy the application to a suitable hosting platform.
