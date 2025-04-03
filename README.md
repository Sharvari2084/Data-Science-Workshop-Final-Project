**Project Title: Fuel Consumption Prediction Using Multiple Linear Regression**
 

**1. Introduction:**
  
Objective: This project aims to predict fuel consumption based on multiple vehicle-related parameters using a machine learning approach. By leveraging historical data, the 
model can estimate fuel usage, helping users optimize fuel efficiency.

Problem Statement: Fuel consumption is a critical factor affecting transportation efficiency, environmental sustainability, and operational costs. Predicting fuel usage 
accurately can help individuals, businesses, and policymakers make informed decisions regarding vehicle efficiency, fuel economy, and sustainability measures.

Dataset Description: This dataset contains features like vehicle model name, engine size, cylinders, fuel consumption, CO2 emissions, smog rating, etc.for various car 
models.
 

**2. Data Collection & Preprocessing**

Data Source: Fuel consumption dataset


**3. Model Development**
   
Algorithm Used: Multiple Linear Regression

Formula for Prediction: Y = b0 + b1X1 + b2X2 + b3X3

Where:\
Y = Predicted Fuel Consumption

X1,X2,X3 = Engine size, No of cylinders, CO2 emissions

b0 = Intercept

b1,b2,b3 = Regression Coefficients


**4. Model Deployment**

Tools Used: Flask

Process:

-Developed a Flask API (app.py) to serve predictions 

-Integrated HTML & CSS for the frontend 

-Used pickle to save and load the trained model 

**5. Steps to Run the Deployed Model**

1) Clone the repository
   
    git clone <repository_link>\
    cd fuel-consumption-prediction
   
2. Create and Activate a Virtual Environment

    python -m venv venv_name \
    venv_name\Scripts\activate
        
3) Install dependencies 

   eg. pip install scikit-learn

4) Run the Flask app

   python app.py

5)Access the Web Interface

  - Open http://127.0.0.1:5000/ in a browser\
  - Input vehicle details and get predicted fuel consumption






 
 
