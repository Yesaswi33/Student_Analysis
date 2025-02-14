# Student_Analysis
Student Performance Predictor

This project is a Flask-based web application that predicts student performance based on factors such as attendance, credit points, CGPA, extra-curricular activities, and skills known. It utilizes a machine learning model to classify performance levels and display results on a web interface.

Project Overview

The application follows a three-layered architecture:

Frontend (index.html) – A simple web form where users enter student details.
Backend (app.py) – A Flask server that processes user inputs and interacts with the trained model.
Machine Learning (train_model.py) – A Python script that trains and saves a prediction model.
How It Works

User Input – The user provides details such as attendance percentage, CGPA, credit points, etc., in the web form (index.html).
Data Processing – The form data is sent to the Flask backend (app.py) via a POST request.
Model Prediction – app.py loads the trained model (train_model.py output) and predicts the student's performance.
Result Display – The predicted performance, level, and badge are shown on the webpage.
Project Structure

|-- index.html          # Frontend - User Input Form & Result Display
|-- app.py              # Backend - Flask Server & Model Handling
|-- train_model.py      # Machine Learning - Model Training & Saving
|-- model.pkl           # Saved Trained Model (Generated after training)
|-- README.md           # Project Documentation
Setup & Execution

1. Install Dependencies
Ensure you have Python installed, then run:

pip install flask scikit-learn pandas
2. Train the Model
Before running the app, train the model if it's not already trained:

python train_model.py
This generates model.pkl, a saved machine learning model.

3. Run the Flask App
python app.py
Then, open http://127.0.0.1:5000/ in your web browser.

