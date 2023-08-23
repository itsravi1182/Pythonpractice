import pandas as pd

def read_csv_to_dataframes(file_path, filename):
    data = pd.read_csv(file_path + filename).transpose().iloc[:,-3:]
      
    return data


