import instaloader

def create_instaloader_instance():
    return instaloader.Instaloader()

def login(loader, username, password):
    loader.login(username, password)

def get_profile(loader, target_username):
    return instaloader.Profile.from_username(loader.context, target_username)

def get_followers(profile):
    return [follower.username for follower in profile.get_followers()]

def get_following(profile):
    return [following.username for following in profile.get_followees()]