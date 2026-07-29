# 🌸 Iris Dataset Classification using Decision Tree

A simple Machine Learning project that demonstrates how to classify the **Iris flower dataset** using a **Decision Tree Classifier** from Scikit-learn. The project also includes data visualization of petal and sepal dimensions.

---

## 📌 Project Overview

The Iris dataset is one of the most popular datasets for learning Machine Learning concepts. This project:

- Loads the Iris dataset
- Splits the dataset into training and testing sets
- Trains a Decision Tree classifier
- Evaluates model performance
- Visualizes the dataset using scatter plots

---

## 📂 Project Structure


Iris-DecisionTree/
│── iris_dataset.csv
│── Iris_dataset.py
│── Petal_length_vs_Width.JPG
│── Sepal_length_vs_Width.JPG
│── README.md


---

## 📊 Dataset

The Iris dataset contains **150 samples** of iris flowers divided into **three species**:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

Each sample contains four features:

| Feature | Description |
|----------|-------------|
| Sepal Length | Length of sepal (cm) |
| Sepal Width | Width of sepal (cm) |
| Petal Length | Length of petal (cm) |
| Petal Width | Width of petal (cm) |

Target variable:

- 0 → Setosa
- 1 → Versicolor
- 2 → Virginica

---

## ⚙️ Technologies Used

- Python 3.x
- Scikit-learn
- Matplotlib

---

## 📦 Installation

Clone the repository:

```bash
git clone [https://github.com/swatantrablr9-design/AI-SelfTraining-ML.git]

Install the required packages:

pip install scikit-learn matplotlib
▶️ Running the Project

Run the Python script:

python Iris_dataset.py

The script will:

Load the dataset
Train the Decision Tree model
Predict test data
Print model accuracy
Display classification report
Generate visualization plots
📈 Model Workflow
Load Dataset
      │
      ▼
Train-Test Split (80%-20%)
      │
      ▼
Decision Tree Training
      │
      ▼
Prediction
      │
      ▼
Accuracy & Classification Report
      │
      ▼
Visualization
📊 Data Visualization
Petal Length vs Petal Width

The petal dimensions clearly separate the three Iris species.

Sepal Length vs Sepal Width

Sepal measurements show greater overlap between species compared to petal measurements.

📋 Sample Output
Accuracy: 1.0

              precision    recall  f1-score   support

      Setosa       1.00      1.00      1.00
  Versicolor       1.00      1.00      1.00
   Virginica       1.00      1.00      1.00

    accuracy                           1.00

Actual accuracy may vary slightly depending on the train-test split.

📚 Key Concepts Demonstrated
Supervised Machine Learning
Decision Tree Classification
Data Visualization
Train-Test Split
Model Evaluation
Classification Report

🚀 Future Improvements
Random Forest Classifier
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
Hyperparameter Tuning
Confusion Matrix
Decision Tree Visualization
Feature Importance Analysis

📖 References
Scikit-learn Documentation: https://scikit-learn.org/
Iris Dataset: https://archive.ics.uci.edu/ml/datasets/iris

👨‍💻 Author
Swatantra Wadhwani

Machine Learning | Artificial Intelligence | Python
