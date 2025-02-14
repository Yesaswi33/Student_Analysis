from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your model or any necessary data
# For simplicity, assuming a simple condition for prediction based on input

def predict_performance(attendance, credit_points, cgpa, extra_curricular, skills_known):
    # Example prediction logic (replace with actual model or logic)
    if cgpa > 8.0 and attendance > 75:
        return "Excellent", "Gold"
    elif cgpa > 6.0 and attendance > 60:
        return "Good", "Silver"
    else:
        return "Needs Improvement", "Bronze"

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    level = None
    badge = None
    if request.method == 'POST':
        # Retrieve data from the form
        attendance = float(request.form['attendance'])
        credit_points = float(request.form['credit_points'])
        cgpa = float(request.form['cgpa'])
        extra_curricular = int(request.form['extra_curricular'])
        skills_known = int(request.form['skills_known'])
        
        # Get prediction
        prediction, level = predict_performance(attendance, credit_points, cgpa, extra_curricular, skills_known)
        badge = level
    
    return render_template('index.html', prediction=prediction, level=level, badge=badge)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  


