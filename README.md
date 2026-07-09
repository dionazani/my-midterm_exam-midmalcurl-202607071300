# my-midtem_exam-remalcurl-202607071300
---

A machine learning research project for detecting malicious URLs using **lexical feature engineering**, **Genetic Algorithm-based feature selection**, and **Tree-Based Ensemble Learning**. This project compares the performance of **Random Forest (Bagging)** and **XGBoost (Boosting)** on a public malicious URL dataset. **Developed as part of a midterm examination**.

---

## 📖 Project Information

| Item | Description |
|------|-------------|
| **Course** | Computational Intelligence and Machine Learning |
| **Development Environment** | Ubuntu WSL 2, Visual Studio Code, Git |
| **Programming Language** | Python |
| **Research Type** | Comparative Machine Learning Study |
| **Dataset** | Public Malicious URL Dataset (Kaggle) |

---

This repository contains a machine learning research project for malicious URL detection using lexical feature engineering and Genetic Algorithm-based feature selection. The study compares two Tree-Based Ensemble Learning approaches: **Random Forest (Bagging)** and **XGBoost (Boosting)**.

---

## 📂 Project Structure

The repository is organized into a modular machine learning pipeline, covering the complete workflow from data preparation to model training and evaluation.

```text
dataset/
├── raw/                  # Original dataset
└── processed/            # Cleaned dataset ready for modeling

notebooks/
├── 01_eda_and_preprocessing.ipynb
├── 02_feature_engineering_ga.ipynb
├── 03_model_training_rf.ipynb
└── 04_model_training_xgboost.ipynb
```

### 📁 Directory Description

| Directory / File | Description |
|------------------|-------------|
| `dataset/raw/` | Stores the original dataset downloaded from the public source. |
| `dataset/processed/` | Contains the cleaned and preprocessed dataset used for feature engineering, model training, and evaluation. |
| `notebooks/01_eda_and_preprocessing.ipynb` | Performs Exploratory Data Analysis (EDA), data cleaning, preprocessing, and binary label transformation. |
| `notebooks/02_feature_engineering_ga.ipynb` | Implements lexical feature extraction and Genetic Algorithm-based feature selection. |
| `notebooks/03_model_training_rf.ipynb` | Trains and evaluates the Random Forest classifier. |
| `notebooks/04_model_training_xgboost.ipynb` | Trains, tunes, and evaluates the XGBoost classifier, followed by performance comparison. |
