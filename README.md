# 🎓 AI Employability Prediction System

An end-to-end Machine Learning project that predicts student employability using academic performance, technical skills, internships, certifications, communication skills, and career readiness indicators.

This project was built using:

* Python
* Scikit-learn
* Logistic Regression
* Streamlit
* Pandas
* Seaborn
* Matplotlib

---

# 🚀 Project Overview

Traditional placement prediction systems mainly focus on GPA and academic marks.

This project extends beyond academics and incorporates modern employability indicators such as:

* Programming skills
* Internship experience
* Tool proficiency
* Certifications
* Communication skills
* Teamwork ability
* Career clarity
* Domain knowledge
* Learning motivation

The final system predicts whether a student is:

* ✅ Employable
* ❌ Needs Improvement

along with prediction confidence.

---

# 📊 Dataset

Dataset Used:

* Undergraduate Employability Dataset

Main Features:

* GPA
* Programming_Skill
* Internship_Count
* Certification_Count
* Communication_Skill
* Domain_Knowledge
* Tool_Proficiency
* Teamwork_Ability
* Career_Clarity
* Learning_Motivation
* Networking_Activity
* Project_Experience
* And more...

Target:

* Employable / Not Employable

---

# 🧠 Machine Learning Workflow

## 1. Data Preprocessing

Performed:

* Missing value handling
* Median imputation
* Feature scaling using StandardScaler
* Binary target engineering
* Train-test split
* Cross-validation

---

## 2. Exploratory Data Analysis (EDA)

EDA included:

* Feature distributions
* Correlation heatmaps
* Employability score distribution
* Class balance analysis
* Feature importance analysis

---

## 3. Model Training

Models experimented with:

* Logistic Regression
* Random Forest
* XGBoost

Final selected model:

* Logistic Regression Pipeline

Why?

* Best cross-validation F1 score
* Stable performance
* High interpretability

---

# 📈 Model Performance

## Cross Validation Results

| Metric         | Score  |
| -------------- | ------ |
| Mean F1 Score  | 0.88   |
| Accuracy       | High   |
| Generalization | Strong |

The model demonstrated strong performance across cross-validation folds.

---

# 🔍 Key Insights

The model identified the following as the strongest employability indicators:

* GPA
* Programming Skill
* Internship Experience
* Certification Count
* Core Subject Knowledge
* Domain Knowledge
* Communication Skills

The project also explores the growing importance of practical skills over purely academic performance in modern hiring trends.

---

# 🖥️ Streamlit Web Application

The project includes a fully interactive Streamlit frontend.

Users can:

* Enter skill and academic details
* Predict employability status
* View confidence score
* Receive improvement suggestions

Example Output:

```text
Employability Probability: 91%
Status: Employable
```

---

# 🛠️ Technologies Used

| Category             | Tools               |
| -------------------- | ------------------- |
| Programming          | Python              |
| ML Framework         | Scikit-learn        |
| Data Analysis        | Pandas, NumPy       |
| Visualization        | Matplotlib, Seaborn |
| Frontend             | Streamlit           |
| Model Serialization  | Joblib              |
| Notebook Environment | Google Colab        |

---

# 📂 Project Structure

```plaintext
placement_prediction/
│
├── model/
│   └── employability_model.pkl
│
├── notebooks/
│   └── Employability_Prediction_model_.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ▶️ Run Locally

## 1. Clone Repository

```bash
git clone <your-repository-link>
cd placement_prediction
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Streamlit App

```bash
streamlit run app.py
```

---

# 📦 requirements.txt

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
xgboost
etc...
```

---

# 🔮 Future Improvements

Planned upgrades:

* SHAP explainability
* Advanced feature engineering
* Hyperparameter tuning
* PDF report generation
* Real-time analytics dashboard
* Skill-gap recommendation engine
* Cloud deployment

---

# 🌐 Deployment

Recommended platforms:

* Streamlit Community Cloud
* Render
* Hugging Face Spaces

---

# 📌 Learning Outcomes

Through this project, I learned:

* End-to-end ML workflow
* Data preprocessing
* Feature engineering
* Cross-validation
* Imbalanced classification handling
* Model evaluation
* Feature importance analysis
* Streamlit application development
* Model deployment workflow

---

# 📧 Contact

If you found this project useful or would like to collaborate, feel free to connect.

---

# ⭐ Acknowledgment

This project was built for learning and portfolio development purposes to explore AI-driven employability prediction systems using modern Machine Learning techniques.
