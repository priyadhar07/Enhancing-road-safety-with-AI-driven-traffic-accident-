# -*- coding: utf-8 -*-
"""Copy of phase 2 code

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sSwijV4wDt_xPZrA4fgHxoT8Yn-hC8l2
"""

import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Step 1: Generate synthetic data
# Features: [speed, weather_condition, visibility, is_night]
# Labels: 1 = accident, 0 = no accident

def generate_data(samples=500):
    data = []
    labels = []
    for _ in range(samples):
        speed = random.randint(20, 120)  # km/h
        weather = random.choice([0, 1, 2])  # 0 = clear, 1 = rain, 2 = fog
        visibility = random.randint(1, 10)  # 1 (low) to 10 (clear)
        is_night = random.choice([0, 1])

        # Accident probability logic (simplified)
        accident = 1 if (
            speed > 90 and (weather == 1 or weather == 2) and visibility < 5
        ) or (is_night and visibility < 4) else 0

        data.append([speed, weather, visibility, is_night])
        labels.append(accident)
    return data, labels

# Generate data
X, y = generate_data()

# Step 2: Split into training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 3: Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 4: Evaluate model
predictions = model.predict(X_test)
print("Model Evaluation:\n")
print(classification_report(y_test, predictions))

# Step 5: Predict new accident risk
def predict_accident(speed, weather, visibility, is_night):
    input_data = [[speed, weather, visibility, is_night]]
    result = model.predict(input_data)[0]
    status = "High Risk of Accident" if result == 1 else "Low Risk of Accident"
    print(f"Prediction: {status}")
    return result

# Test prediction
print("\nNew Prediction:")
predict_accident(speed=100, weather=2, visibility=3, is_night=1)  # fog, low visibility at night
