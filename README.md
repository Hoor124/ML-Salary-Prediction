# Salary Prediction Machine Learning Project

## Project Overview

This project develops a machine learning application that predicts salary based on years of professional experience.

The project covers the complete machine learning workflow, including:

- Data loading
- Data exploration
- Data preprocessing
- Train-test splitting
- Regression model training
- Model evaluation
- Model serialization
- Streamlit application development
- Deployment

## Dataset

The dataset contains two main variables:

- Experience Years
- Salary

## Machine Learning Models

The following regression models were evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression

## Evaluation Metrics

The models were evaluated using:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

## Application

The Streamlit application allows users to enter their years of experience and receive a predicted salary.

## Project Structure

ML_Project/
- data/
  - salary_dataset.csv
- model/
  - salary_model.pkl
- notebooks/
  - model_training.ipynb
- app.py
- requirements.txt
- README.md
- .gitignore

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Streamlit
- GitHub