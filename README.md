# ⚡ AI Energy Consumption Predictor (End-to-End MLOps)

Welcome to my first End-to-End Machine Learning project! This repository contains a complete pipeline for predicting daily energy consumption based on weather and calendar data.

## 🚀 Project Overview
Instead of just building a model in a Jupyter Notebook, I focused on creating a production-ready, modular MLOps pipeline. The project predicts daily electricity consumption using inputs like temperature, humidity, and whether it's a weekend.

## 🛠️ Tech Stack & Architecture
* **Data Engineering:** Python, Pandas (Synthetic Data Generation & EDA)
* **Model Training:** Scikit-Learn, XGBoost (`xgboost_model.pkl`)
* **Backend API:** FastAPI & Uvicorn (RESTful API deployment)
* **Frontend UI:** Streamlit (Interactive Web Application)
* **Version Control:** Git & GitHub

## 📂 Project Structure
* `data/` : Contains the raw CSV dataset.
* `notebooks/` : Jupyter notebooks for experimentation and EDA.
* `src/` : Modular python scripts (`data_ingestion.py`, `data_preprocessing.py`, `model_training.py`).
* `models/` : Saved `.pkl` files (Model and Scaler).
* `src/app.py` : The FastAPI backend server.
* `src/frontend.py` : The Streamlit frontend user interface.

## 🔮 Future Enhancements
* Implementing Time-Series Forecasting (e.g., ARIMA or Prophet) for monthly predictions.
* Deploying the API and Frontend using Docker & AWS/Render.
