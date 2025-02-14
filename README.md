# 🎓 Student Performance Predictor  

A **Flask-based web application** that predicts student performance based on **Attendance, CGPA, Credit Points, Extra-Curricular Activities, and Skills Known**.  
It uses a **machine learning model (Random Forest Classifier)** trained on real student data to generate predictions.  

🔗 **Live Demo:** [Student Performance Predictor](https://student-performance-predictor-egcl.onrender.com)  

---

## 📂 **Project Structure**  
/Student_Analysis │-- app.py # Flask backend (loads trained ML model) │-- train_model.py # ML training script (creates model.pkl) │-- student_performance.csv # Dataset used for training │-- model.pkl # Saved trained ML model │-- index.html # Frontend UI (HTML form) │-- static/ # CSS & assets (if any) │-- templates/ # Flask templates │-- requirements.txt # Dependencies │-- Procfile # Deployment configuration for Render │-- README.md # Project documentation


---

## 🚀 **Features**
✅ **Predicts performance** using real-world student data  
✅ **Uses machine learning** (Random Forest model) for accurate classification  
✅ **Assigns badges** (Gold, Silver, Bronze, No Badge) dynamically  
✅ **Simple UI** with real-time performance feedback  
✅ **Live Deployment** on Render  

---

## 🛠️ **Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Yesaswi33/Student_Analysis.git
cd Student_Analysis
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Model
If you modify student_performance.csv, retrain the model:

python train_model.py
This creates a model.pkl file.

4️⃣ Run Flask App Locally
python app.py
Visit http://127.0.0.1:5011/ in your browser.

🚀 Deployment on Render

This app is live at:
🔗 Student Performance Predictor

1️⃣ Push Your Code to GitHub
git add .
git commit -m "Updated model/UI"
git push origin main
2️⃣ Deploy on Render
Go to Render Dashboard → Click "New Web Service"
Connect your GitHub repository
Set Build Command:
pip install -r requirements.txt
Set Start Command:
gunicorn app:app
Click Deploy 🎉
✅ Now your app will be live with every GitHub update!

📦 Usage Guide

🔹 User Inputs
Attendance (%) (e.g., 85)
Credit Points (e.g., 25)
CGPA (e.g., 7.5)
Extra-Curricular Activities (Yes/No)
Skills Known (e.g., 5)
🔹 Output Predictions
The app predicts Performance Level & Badge:

Performance	Badge
Excellent	Gold
Good	Silver
Average	Bronze
Poor	No Badge
It also provides personalized improvement suggestions based on the prediction.

🤝 Contributing

Want to improve this project? Follow these steps:

Fork the repo
Create a new branch (git checkout -b feature-branch)
Commit changes (git commit -m "Added new feature")
Push to GitHub (git push origin feature-branch)
Open a Pull Request 🚀
⚖️ License

This project is open-source and available under the MIT License.

✨ Author & Acknowledgment

👨‍💻 Developed by: Yesaswi
📌 Status: ✅ Live & Working


