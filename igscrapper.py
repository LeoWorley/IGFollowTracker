import os
import json
from instagram_utils import create_instaloader_instance, login, get_profile, get_followers, get_following
from file_utils import save_list_to_csv

# Load config from config.json
with open('config.json') as f:
    config = json.load(f)

# Create an instance of Instaloader and login
L = create_instaloader_instance()
login(L, config['username'], config['password'])

# Get profile of the target user
profile = get_profile(L, config['target_username'])

# Fetch followers and following
followers_list = get_followers(profile)
following_list = get_following(profile)

print("Followers: ", followers_list)
print("Following: ", following_list)

# Save lists to CSV files
followers_path = save_list_to_csv(followers_list, config['path_to_save'], f'{config["target_username"]}_followers')
following_path = save_list_to_csv(following_list, config['path_to_save'], f'{config["target_username"]}_following')

print(f"Followers list saved to {followers_path}")
print(f"Following list saved to {following_path}")