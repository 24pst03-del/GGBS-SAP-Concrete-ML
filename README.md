# Machine Learning Prediction of Concrete Strength using GGBS and SAP

## Project Overview

This project uses Machine Learning techniques to predict the **compressive strength of concrete** using sustainable materials such as **Ground Granulated Blast Furnace Slag (GGBS)** and **Super Absorbent Polymer (SAP)**.

The aim is to analyze how these materials influence the mechanical properties of concrete and develop predictive models for concrete strength.

---

## Dataset Description

The dataset contains experimental data related to concrete mix design with the following parameters:

* Cement content (kg/m³)
* GGBS replacement percentage
* SAP content
* Water-cement ratio
* Compressive strength (MPa)
* Split tensile strength
* Flexural strength
* Water absorption

The dataset consists of approximately **500 samples of concrete mix data**.

---

## Project Objectives

* Analyze the effect of GGBS and SAP on concrete properties
* Perform data analysis and visualization
* Develop machine learning models to predict compressive strength
* Compare the performance of different ML models

---

## Machine Learning Models Used

The following machine learning models are implemented in this project:

* Linear Regression
* Random Forest Regressor
* Artificial Neural Network (ANN)
* XGBoost Regressor

These models help predict the compressive strength of concrete based on mix design parameters.

---

## Project Structure

GGBS-SAP-Concrete-ML

dataset
  ggbs_sap_concrete_dataset_500_github_ready.csv

src
  01_load_dataset.py
  02_data_cleaning.py
  03_statistical_analysis.py
  04_visualization.py
  05_correlation_heatmap.py
  06_feature_scaling.py
  07_linear_regression.py
  08_random_forest.py
  09_ann_model.py
  10_xgboost_model.py

requirements.txt
README.md

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow
* XGBoost

---

## How to Run the Project

1. Download or clone the repository

2. Install required libraries

pip install -r requirements.txt

3. Run any machine learning script

Example:

python src/07_linear_regression.py

---

## Applications

This project can be used for:

* Sustainable concrete research
* Civil engineering machine learning applications
* Concrete mix design optimization
* Academic research projects

---

## Author

Chellapriya B
Structural Engineering Student
