# 🏬 Wholesale Customer Channel Classification

## 📌 Project Overview

This project aims to classify wholesale customers into:

- **HORECA** (Hotel/Restaurant/Café)
- **Retail**

based on their annual spending across different product categories.

The goal is to help businesses identify customer segments and improve:
- Marketing strategy
- Inventory planning
- Pricing decisions
- Sales optimization

---

## 📊 Dataset Information

The dataset contains annual spending (Monetary Units) in the following categories:

- Fresh
- Milk
- Grocery
- Frozen
- Delicassen

Target Variable:
- Channel (HORECA / Retail)

Note: `Region` and `Detergents_Paper` were removed during preprocessing.

---

## 🔎 Machine Learning Workflow

This project follows a complete ML workflow:

### 1️⃣ Data Understanding
- Checked missing values
- Checked class distribution
- Performed descriptive statistics

### 2️⃣ Exploratory Data Analysis (EDA)
- Univariate analysis
- Bivariate analysis
- Correlation matrix
- Outlier detection using boxplots

### 3️⃣ Data Preprocessing
- Removed unnecessary columns (Region, Detergents_Paper)
- Applied feature scaling (StandardScaler)
- Train-test split (Stratified)

### 4️⃣ Model Building
Compared multiple classification algorithms:

- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Naive Bayes

### 5️⃣ Hyperparameter Tuning
Used **GridSearchCV (5-fold cross-validation)**  
Evaluation metric: **F1-score**

### 6️⃣ Final Model Selection
KNN was selected based on:
- Highest Cross-Validation F1-score
- Strong test performance
- Good generalization

---

## 🏆 Model Performance

| Model | CV F1 Score |
|--------|-------------|
| KNN | 0.92 |
| Naive Bayes | 0.91 |
| Logistic Regression | 0.91 |
| Decision Tree | 0.89 |

Final Test F1-score (KNN): ~0.91+

---

## 🚀 Deployment

The final model was deployed using **Streamlit**.

The app allows users to input spending values and predict:

- HORECA
- Retail

The model is saved using `pickle` as a serialized pipeline.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn


