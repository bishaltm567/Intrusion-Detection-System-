# src/detect_intrusion.py
import joblib
import pandas as pd
from preprocess import load_and_preprocess

# Load trained model
model = joblib.load('../models/intrusion_model.pkl')
print("Trained model loaded successfully!")

# Load new data (replace with new network traffic data)
X_new, y_new = load_and_preprocess('../data/KDDCup99.csv')  # Can be replaced by actual live data

# Make predictions
predictions = model.predict(X_new)

# Show first 20 predictions
for i, pred in enumerate(predictions[:20]):
    print(f"Sample {i+1}: Predicted = {pred}")
