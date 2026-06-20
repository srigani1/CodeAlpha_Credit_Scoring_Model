# CodeAlpha Credit Scoring Model

A machine learning based Credit Risk Prediction web application built using Streamlit and Random Forest Classifier.

## Project Overview

This project predicts whether a loan applicant has low, medium, or high credit risk based on applicant and loan details. The model is trained separately and saved as a `.pkl` file, so the Streamlit app loads faster during startup.

## Features

- Credit risk prediction using Machine Learning
- Fast loading using pre-trained model file
- Light and dark theme support
- User-friendly Streamlit interface
- Risk score and confidence display
- Applicant summary
- Feature importance visualization
- Downloadable credit report
- Export report as PDF after prediction

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Random Forest Classifier
- Pickle
- ReportLab

## Files

- `app.py` - Main Streamlit application
- `credit_risk_model.pkl` - Pre-trained machine learning model
