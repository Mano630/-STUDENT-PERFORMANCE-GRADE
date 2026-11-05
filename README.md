
Student Performance Prediction System
About the Project
The Student Performance Prediction System is a machine learning classification project that predicts a student's final grade (A–F) using academic performance, study habits, and background factors. The project compares several classification algorithms, evaluates their performance, and uses a Gradient Boosting Classifier in a Streamlit application for interactive predictions.
Dataset
The notebook loads the dataset from Student_Performance.csv.
- Original dataset: 25,000 rows × 16 columns
- Duplicate rows identified and removed: 10,000
- Dataset after cleaning: 15,000 rows × 16 columns
- Missing values: 0 across all columns after cleaning
Dataset Features
- Student ID (student_id)
- Age (age)
- Gender (gender)
- School Type (school_type)
- Parent Education (parent_education)
- Study Hours (study_hours)
- Attendance Percentage (attendance_percentage)
- Internet Access (internet_access)
- Travel Time (travel_time)
- Extracurricular Activities (extra_activities)
- Study Method (study_method)
- Math Score (math_score)
- Science Score (science_score)
- English Score (english_score)
- Overall Score (overall_score)
- Final Grade (final_grade)
Dataset Download
The notebook references Student_Performance.csv, but it does not provide a public dataset URL. Add the verified dataset source link here if available, or include the CSV in your repository where redistribution is permitted.
Input Features
The model uses 14 input features:
- Age
- Gender
- School Type
- Parent Education
- Study Hours
- Attendance Percentage
- Internet Access
- Travel Time
- Extracurricular Activities
- Study Method
- Math Score
- Science Score
- English Score
- Overall Score
student_id is excluded from model training.
Target Variable
Final Grade (final_grade) — a six-class categorical target encoded as:
Grade	Encoded Label
A	6
B	5
C	4
D	3
E	2
F	1


Machine Learning Algorithms
The notebook compares these classification algorithms:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- AdaBoost Classifier
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- LightGBM Classifier
- XGBoost Classifier
Selected model: Gradient Boosting Classifier.
Data Preprocessing
- Checked for and removed duplicate records.
- Checked for missing values.
- Encoded categorical features using one-hot encoding and category mappings.
- Used median imputation in the preprocessing workflow.
- Split the cleaned dataset into 80% training data and 20% testing data (random_state=42).
- Used a ColumnTransformer to prepare numerical and categorical inputs for modeling.
Model Evaluation
Evaluation includes:
- Accuracy
- Balanced Accuracy
- Precision, Recall, and F1-score
- Confusion Matrix
- ROC-AUC and Average Precision for multiclass model comparison
- 5-fold stratified cross-validation for the final Gradient Boosting model
Model Comparison (Test Accuracy)
Model	Accuracy
Gradient Boosting	99.60%
Decision Tree	99.47%
XGBoost	99.40%
Random Forest	99.33%
LightGBM	99.23%


Final Gradient Boosting Results
- Test Accuracy: 99.60%
- Test Balanced Accuracy: 99.46%
- 5-Fold CV Accuracy: 99.71% ± 0.10%
- 5-Fold CV Macro F1: 99.71% ± 0.07%
Modeling note: overall_score is included among the inputs. Verify that this score is available when predictions are made and is not derived directly from the final-grade label; otherwise, reported performance may overestimate real-world predictive ability.

Technologies Used
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
- Google Colab
- Pyngrok (for sharing the Streamlit app from Colab)
Project Workflow
1. Data Collection
2. Data Inspection and Cleaning
3. Exploratory Data Analysis (EDA)
4. Categorical Encoding and Feature Preparation
5. Train–Test Split
6. Classification Model Training
7. Model Comparison and Evaluation
8. Cross-Validation and Best Model Selection
9. Model Saving with Joblib
10. Student Grade Prediction through Streamlit
Streamlit Application
The notebook contains code to generate a Streamlit Student Grade Predictor app. Users can enter academic and personal-study information to see:
- Predicted final grade (A–F)
- Model confidence
- Predicted probabilities across all six grade classes
The trained model is saved as student_grade_model.joblib, and the app code is written to app.py in the Colab environment.
How to Run
1. Open the notebook Student__Performance_in (3).ipynb in Google Colab.
2. Upload the required Student_Performance.csv dataset to the notebook runtime.
3. Run the notebook cells to clean the data, train/evaluate models, and save student_grade_model.joblib.
4. Run the notebook cell that writes /content/app.py.
5. Use the Streamlit and Pyngrok launch cells in the notebook to open the app in Colab.
Note: The app currently loads the model from /content/student_grade_model.joblib, a Colab-specific path. Update this path if running Streamlit locally or deploying elsewhere. An ngrok link is temporary and requires the Colab runtime to remain active.
Author
