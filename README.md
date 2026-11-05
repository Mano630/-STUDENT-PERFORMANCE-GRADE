
#  Student Performance Prediction System

##  About the Project

The Student Performance Prediction System is a Machine Learning project that predicts students' final grades (A–F) based on their academic performance, study habits, and other relevant factors.

The project involves data preprocessing, exploratory data analysis (EDA), feature selection, model training, evaluation, and comparison of multiple classification algorithms.

The best-performing model is integrated into an interactive Streamlit web application for student grade prediction.

##  Dataset

The dataset used in this project originally contains 25,000 student records and 16 columns.

### Dataset Information

- Original Dataset: 25,000 rows × 16 columns
- Duplicate Records Removed: 10,000
- Final Dataset Shape: 15,000 rows × 16 columns
- Missing Values: 0
- Remaining Duplicate Records: 0

### Dataset Features

- Student ID
- Age
- Gender
- School Type
- Parent Education
- Study Hours
- Attendance Percentage
- Internet Access
- Travel Time
- Extra Activities
- Study Method
- Math Score
- Science Score
- English Score
- Overall Score
- Final Grade

### Dataset Download

Dataset File: `Student_Performance.csv`

Add the original dataset download link here.

##  Input Features

The input features used for student grade prediction include:

- Age
- Gender
- School Type
- Parent Education
- Study Hours
- Attendance Percentage
- Internet Access
- Travel Time
- Extra Activities
- Study Method
- Math Score
- Science Score
- English Score
- Overall Score

##  Target Variable

**Final Grade**

The target variable represents six student grade categories.

| Grade | Encoded Value |
|-------|---------------|
| A | 6 |
| B | 5 |
| C | 4 |
| D | 3 |
| E | 2 |
| F | 1 |

##  Machine Learning Algorithms

The following classification algorithms were implemented and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Gradient Boosting Classifier
5. AdaBoost Classifier
6. Support Vector Machine (SVC)
7. K-Nearest Neighbors (KNN)
8. Gaussian Naive Bayes
9. Multinomial Naive Bayes
10. LightGBM Classifier
11. XGBoost Classifier

### Best Performing Model

**Gradient Boosting Classifier**

##  Evaluation Metrics

The machine learning models were evaluated using:

- Accuracy Score
- Balanced Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score
- Average Precision
- Stratified K-Fold Cross-Validation

##  Model Performance

| Machine Learning Model | Test Accuracy |
|------------------------|---------------|
| Gradient Boosting | 99.60% |
| Decision Tree | 99.47% |
| XGBoost | 99.40% |
| Random Forest | 99.33% |
| LightGBM | 99.23% |

### Best Model Evaluation Results

- Test Accuracy: 99.60%
- Balanced Accuracy: 99.46%
- 5-Fold Cross-Validation Accuracy: 99.71% ± 0.10%
- 5-Fold Cross-Validation Macro F1: 99.71% ± 0.07%

**Note:** The `overall_score` feature should be checked for potential target leakage because it may be directly related to the final grade. This is important when assessing real-world model generalization.

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- LightGBM
- Streamlit
- Joblib
- Pyngrok
- Google Colab
- Git & GitHub

##  Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Categorical Feature Encoding
6. Data Preprocessing
7. Train-Test Split (80:20)
8. Machine Learning Model Training
9. Model Testing
10. Model Evaluation
11. Cross-Validation
12. Model Performance Comparison
13. Best Model Selection
14. Model Saving Using Joblib
15. Streamlit Application Development
16. Student Grade Prediction

##  Streamlit Web Application

An interactive Student Grade Predictor web application was developed using Streamlit.

### Application Features

- User-friendly interface
- Student academic information input
- Final grade prediction (A–F)
- Prediction confidence display
- Grade probability visualization
- Integration with the trained Gradient Boosting model

### Saved Model

`student_grade_model.joblib`

### Application File

`app.py`

##  How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### Step 2: Install Required Libraries

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost lightgbm streamlit joblib pyngrok
```

### Step 3: Open the Notebook

Open the project notebook using Google Colab or Jupyter Notebook.

### Step 4: Upload the Dataset

Upload the `Student_Performance.csv` dataset.

### Step 5: Execute the Notebook

Run all cells to perform:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Model training
- Model evaluation
- Best model selection

### Step 6: Run the Streamlit Application

If running locally, first update any Colab-specific file paths in the application.

```bash
streamlit run app.py
```

### Step 7: Predict Student Grades

Enter the required student information and generate the predicted final grade.

##  Future Improvements

- Hyperparameter tuning for further model optimization
- Additional feature engineering
- Investigation and prevention of target leakage
- Model explainability using SHAP
- Deployment on Streamlit Community Cloud
- Model monitoring and performance tracking
- Integration with an academic dashboard

##  Author

**Manodip Bouri**

**Skills:** Python | Machine Learning | Data Science | Scikit-learn | Streamlit | Data Analysis
