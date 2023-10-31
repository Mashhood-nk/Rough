import os
import pandas as pd

def read_file():
    files = [file for file in os.listdir() if file.endswith(('.xlsx', '.csv'))]

    if not files:
        print("No CSV or XLSX files found.")
        return None

    # Pick the first file and rename it to 'InputData'
    file_to_rename = files[0]
    new_file_name = 'InputData' + os.path.splitext(file_to_rename)[1]

    os.rename(file_to_rename, new_file_name)

    if new_file_name.lower().endswith('.xlsx'):
        df = pd.read_excel(new_file_name)
    else:
        df = pd.read_csv(new_file_name)

    print(f"Loaded '{file_to_rename}' as 'InputData' and read it into a DataFrame.")
    return df