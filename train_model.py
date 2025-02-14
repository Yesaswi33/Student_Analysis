import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data = pd.read_csv('student_performance.csv')

# Separate features and target
X = data.drop('Performance', axis=1)
y = data['Performance']

# Handle missing values
X.fillna(X.mean(), inplace=True)

# Encode categorical target if necessary
y = y.map({'Excellent': 3, 'Good': 2, 'Average': 1, 'Needs Improvement': 0})

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Save the trained model
joblib.dump(model, 'student_model.pkl')
