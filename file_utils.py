import pandas as pd
from datetime import datetime

def save_list_to_csv(data_list, path, filename_prefix):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f'{filename_prefix}_{current_date}.csv'
    path_to_save = f'{path}/{filename}'
    pd.DataFrame(data_list).to_csv(path_to_save, index=False, header=False)
    return path_to_save