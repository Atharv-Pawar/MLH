import requests

def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching user data")
        return None

    return response.json()


def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching repos")
        return None

    return response.json()


def analyze_repos(repos):
    total_stars = 0
    languages = {}
    top_repo = None
    max_stars = 0

    for repo in repos:
        total_stars += repo["stargazers_count"]

        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

        if repo["stargazers_count"] > max_stars:
            max_stars = repo["stargazers_count"]
            top_repo = repo["name"]

    most_used_lang = max(languages, key=languages.get) if languages else "N/A"

    return total_stars, most_used_lang, top_repo

def latest_repos(repos):
    if not repos:
        return None
    return max(repos, key=lambda x: x["updated_at"])

def max_forks(repos):
    if not repos:
        return None

    return max(repos, key=lambda x: x.get("forks_count", 0))

username = input("Enter GitHub username: ")

user = get_user_data(username)
repos = get_repos(username)

if user and repos:
    total_stars, most_used_lang, top_repo = analyze_repos(repos)

    print(f"\nUser: {user['name']}")
    print(f"Followers: {user['followers']}")
    print(f"Public Repos: {user['public_repos']}")
    print(f"Total Stars: {total_stars}")
    print(f"Most Used Language: {most_used_lang}")
    print(f"Top Repo: {top_repo}")
    latest = latest_repos(repos)
    forked = max_forks(repos)

    print(f"Latest Repository: {latest['name']}")
    print(f"Max Forked Repo: {forked['name']} (Forks: {forked['forks_count']})")