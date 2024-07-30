import pandas as pd
from datetime import datetime
import os

def save_list_to_csv(data_list, path, filename_prefix):
    print(f'{filename_prefix}: {data_list}')
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f'{filename_prefix}_{current_date}.csv'
    path_to_save = f'{path}/{filename}'
    pd.DataFrame(data_list).to_csv(path_to_save, index=False, header=False)
    return path_to_save

def load_list_from_csv(filepath):  # Function to load list from CSV
    if os.path.exists(filepath):
        return pd.read_csv(filepath, header=None)[0].tolist()
    return []

def find_latest_csv(path, filename_prefix):  # New function to find the latest CSV file
    files = [f for f in os.listdir(path) if f.startswith(filename_prefix) and f.endswith('.csv')]
    if not files:
        return None
    latest_file = max(files, key=lambda f: datetime.strptime(f[len(filename_prefix)+1:-4], "%Y-%m-%d"))
    return os.path.join(path, latest_file)

def compare_and_save_differences(new_list, path, filename_prefix):  # Updated function to compare and save differences
    current_date = datetime.now().strftime("%Y-%m-%d")
    new_filename = f'{filename_prefix}_{current_date}.csv'
    new_file_path = f'{path}/{new_filename}'
    
    previous_file_path = find_latest_csv(path, filename_prefix)  # Find the latest CSV file
    previous_list = load_list_from_csv(previous_file_path) if previous_file_path else []  # Load previous list if available

    new_followers = list(set(new_list) - set(previous_list))
    lost_followers = list(set(previous_list) - set(new_list))
    
    if new_followers:
        new_followers_filename = f'new_followers_{current_date}.csv'
        new_followers_path = f'{path}/{new_followers_filename}'
        pd.DataFrame(new_followers).to_csv(new_followers_path, index=False, header=False)
    
    if lost_followers:
        lost_followers_filename = f'lost_followers_{current_date}.csv'
        lost_followers_path = f'{path}/{lost_followers_filename}'
        pd.DataFrame(lost_followers).to_csv(lost_followers_path, index=False, header=False)
    
    return new_file_path, new_followers, lost_followers