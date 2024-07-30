import os
import json
from instagram_utils import create_instaloader_instance, login, get_profile, get_followers, get_following
from file_utils import save_list_to_csv, compare_and_save_differences

# Load config from config.json
with open('config.json') as f:
    config = json.load(f)

# Create an instance of Instaloader and login
L = create_instaloader_instance()
login(L, config['username'], config['password'])

# Print tarjet username
print("Target username: ", config['target_username'])
# Get profile of the target user
profile = get_profile(L, config['target_username'])

# Fetch followers and following
# Ask the user if they want to fetch followers
if input("Do you want to fetch followers? (y/n): ") == 'y':
    followers_list = get_followers(profile)
    print("Followers: ", followers_list)

# Ask the user if they want to fetch following
if input("Do you want to fetch following? (y/n): ") == 'y':
    following_list = get_following(profile)
    print("Following: ", following_list)

print("Followers: ", followers_list)
print("Following: ", following_list)

# Save lists to CSV files
followers_path = save_list_to_csv(followers_list, config['path_to_save'], f'{config["target_username"]}_followers')
following_path = save_list_to_csv(following_list, config['path_to_save'], f'{config["target_username"]}_following')

# Compare followers and save differences
_, new_followers, lost_followers = compare_and_save_differences(followers_list, config['path_to_save'], f'{config["target_username"]}_followers')

print(f"Followers list saved to {followers_path}")
print(f"Following list saved to {following_path}")

if new_followers:
    print(f"New followers: {new_followers}")
if lost_followers:
    print(f"Lost followers: {lost_followers}")