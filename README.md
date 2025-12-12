# 🏠 House Price Predictor
A web-based application that predicts the price of a house based on user inputs like location, size, and number of bedrooms. This project demonstrates the integration of machine learning with a Flask backend and a responsive frontend.
```
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-1.1.2-orange?logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24-green?logo=scikit-learn&logoColor=white)
````


## Project Structure
```
house-price-predictor/
│
├── app.py                 # Main Flask application
├── Ridgemodel.pkl              # Trained machine learning model
├── templates/
│   └── index.html         # HTML page for input form
├── static/
│   ├── css/
│   └── js/
├── data/
│   └── Cleaned_data.csv     # Dataset used for training
├── notebook/
│   └── house-price-predictor.ipynb # Jupyter Notebook for training the model
├── requirements.txt       # Python dependencies
└── README.md

````


## Features
```
- Predicts house prices based on location, total square footage, and number of bedrooms.
- Responsive user interface.
- Clean and simple input form.
- Error handling for missing or invalid inputs.
- Easily deployable locally or on cloud platforms.
```

## Technologies Used
```
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Other Tools:** Jupyter Notebook for data analysis, Git for version control
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/house-price-predictor.git
```

## 2.Navigate into the project directory
```
cd house-price-predictor
```
## 3.Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
## 4.Install required packages:
```
pip install -r requirements.txt
```
## 5.Run the Flask app:
```
python app.py

```
## Model Details
```
. Type: Regression (e.g., Linear Regression / Random Forest)
. Input Features: Location, total square footage, bedrooms, bathrooms
. Performance Metrics: R² Score, MAE, RMSE (add your metrics here)
```
