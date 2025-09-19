import requests

def fetch_github_profile(username: str):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=5&sort=updated"

    user_data = requests.get(user_url).json()
    repos_data = requests.get(repos_url).json()

    return {"profile": user_data, "repos": repos_data}
