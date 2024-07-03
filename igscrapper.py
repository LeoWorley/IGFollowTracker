import instaloader
import os
import json
from datetime import datetime

# Load config from config.json
with open('config.json') as f:
    config = json.load(f)

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in to Instagram
username = config['username']
password = config['password']
L.login(username, password)

# Get profile of the target user
target_username = config['targer_username']
profile = instaloader.Profile.from_username(L.context, target_username)

# Fetch and print followers
followers = profile.get_followers()
followers_list = [follower.username for follower in followers]

# Fetch following
following = profile.get_followees()
following_list = [following.username for following in following]

print("Followers: ", followers_list)
print("Following: ", following_list)

# Path to save list of followers
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f'{target_username}_followers_{current_date}.csv'
path = config['path_to_save'] + '/' + filename

# Find new followers comparing with the last list in the path