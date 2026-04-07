# src/preprocess.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(file_path):
    """
    Load dataset, encode categorical features, scale numeric features.
    Returns features (X) and target (y)
    """
    # Load dataset
    df = pd.read_csv(file_path)

    # Check for 'label' column
    if 'label' not in df.columns:
        raise ValueError("Dataset must have a 'label' column.")

    # Encode categorical columns
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    # Split features and target
    X = df.drop('label', axis=1)
    y = df['label']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y
