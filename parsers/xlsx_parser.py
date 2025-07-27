import pandas as pd

def read_xlsx(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')
    return df.astype(str).values.flatten().tolist()
