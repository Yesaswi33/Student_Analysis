from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Improved prediction logic considering all input factors
def predict_performance(attendance, credit_points, cgpa, extra_curricular, skills_known):
    # Assigning weights to each factor
    score = (cgpa * 4) + (attendance * 0.5) + (credit_points * 1.5) + (extra_curricular * 2) + (skills_known * 1)

    # Classifying performance based on total score
    if score >= 40:
        return "Excellent", "Gold"
    elif score >= 30:
        return "Good", "Silver"
    elif score >= 20:
        return "Average", "Bronze"
    else:
        return "Needs Improvement", "No Badge"

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    level = None
    badge = None

    if request.method == 'POST':
        # Retrieve and convert form data
        attendance = float(request.form['attendance'])
        credit_points = float(request.form['credit_points'])
        cgpa = float(request.form['cgpa'])
        extra_curricular = int(request.form['extra_curricular'])
        skills_known = int(request.form['skills_known'])

        # Get prediction
        prediction, badge = predict_performance(attendance, credit_points, cgpa, extra_curricular, skills_known)
        level = prediction  # Level and prediction are the same

    return render_template('index.html', prediction=prediction, level=level, badge=badge)

if __name__ == '__main__':
    app.run(debug=True, port=5011)
