# ⛽ Fuel Consumption Prediction Using Multiple Linear Regression
 
## 1. Introduction

### Objective
The objective of this project is to **predict fuel consumption** based on multiple vehicle-related parameters using a **machine learning approach**.  
By leveraging historical vehicle data, the model estimates fuel usage, helping users analyze fuel efficiency and make informed decisions.

### Problem Statement
Fuel consumption is a critical factor influencing **transportation efficiency, environmental sustainability, and operational costs**.  
Accurate prediction of fuel usage can assist individuals, businesses, and policymakers in improving vehicle efficiency, reducing fuel expenses, and supporting sustainability initiatives.

### Dataset Description
The dataset contains information for various car models, including:
- Vehicle model name  
- Engine size  
- Number of cylinders  
- Fuel consumption  
- CO₂ emissions  
- Smog rating  

This data is used to train a regression model for fuel consumption prediction.

 

## 2. Data Collection & Preprocessing

### Data Source
- Fuel Consumption Dataset

### Preprocessing Steps
- Removal of irrelevant columns
- Handling missing values
- Selection of key numerical features
- Preparation of cleaned data suitable for model training


---

## 3. Model Development

### Algorithm Used
- **Multiple Linear Regression**

Formula for Prediction: Y = b0 + b1X1 + b2X2 + b3X3

Where:\
Y = Predicted Fuel Consumption

X1,X2,X3 = Engine size, No of cylinders, CO2 emissions

b0 = Intercept

b1,b2,b3 = Regression Coefficients


**4. Model Deployment**

# 4. Model Deployment

### Tools Used
- **Flask (Python Web Framework)**

### Deployment Process
- Developed a Flask application (`app.py`) to serve predictions
- Integrated **HTML and CSS** for the frontend interface
- Used **pickle** to save and load the trained machine learning model
- Enabled real-time prediction through a web-based interface


## 5. Steps to Run the Deployed Model
```bash
Step 1: Clone the Repository

git clone <repository_link>
cd fuel-consumption-prediction
   
Step 2: Create and Activate a Virtual Environment
python -m venv venv_name
venv_name\Scripts\activate
        
Step 3: Install Dependencies
pip install scikit-learn flask pandas numpy

Step 4: Run the Flask Application
python app.py

Step 5: Access the Web Interface
Open the browser and go to:

http://127.0.0.1:5000/
Enter vehicle details
Get the predicted fuel consumption instantly






 
 
