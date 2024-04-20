import requests
import re

def get_instagram_user_id(username):

    profile_url = f"https://www.instagram.com/{username}/"

    response = requests.get(profile_url)

    page_source = response.text

    pattern = r"profilePage_([0-9]+)"
    match = re.search(pattern, page_source)

    if match:
        user_id = match.group(1)
        return user_id

    return None

username = input("Enter username: ")

user_id = get_instagram_user_id(username)

print("Instagram User ID:", user_id)

