from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load dataset
df = pd.read_csv('Cleaned_data.csv')

# Load your trained model
model = pickle.load(open('RidgeModel.pkl', 'rb'))   # not pipe

@app.route('/')
def index():
    locations = sorted(df['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    total_sqft = float(request.form.get('feet'))

    # Input format for prediction
    input_df = pd.DataFrame([[location, total_sqft, bath, bhk]], 
                            columns=['location', 'total_sqft', 'bath', 'bhk'])

    # Prediction
    prediction = model.predict(input_df)[0]*1e5

    return str(np.round(prediction,2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
