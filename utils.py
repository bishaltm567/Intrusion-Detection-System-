# src/utils.py
import pandas as pd

def save_predictions(predictions, output_file='predictions.csv'):
    """
    Save predictions to a CSV file
    """
    df = pd.DataFrame(predictions, columns=['prediction'])
    df.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")
