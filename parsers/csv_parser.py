import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.astype(str).values.flatten().tolist()  # Convert to list of strings
