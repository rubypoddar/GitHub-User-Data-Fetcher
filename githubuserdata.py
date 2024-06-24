import requests
import re

def extract_links_from_text(text):
    """
    Function to extract links from a text string using regex.
    """
    return re.findall(r'https?://\S+', text)

def get_github_user_stats(username, fetch_followers=False):
    # GitHub API endpoint for user details
    user_url = f"https://api.github.com/users/{username}"
    
    # Requesting user details
    user_response = requests.get(user_url)
    
    if user_response.status_code == 200:
        user_data = user_response.json()
        
        # Extracting necessary user details
        user_stats = {
            "Username": user_data.get("login"),
            "Name": user_data.get("name"),
            "Company": user_data.get("company"),
            "Blog": user_data.get("blog"),
            "Location": user_data.get("location"),
            "Email": user_data.get("email"),
            "Bio": user_data.get("bio"),
            "Twitter Username": user_data.get("twitter_username"),
            "Public Repos": user_data.get("public_repos"),
            "Public Gists": user_data.get("public_gists"),
            "Followers": user_data.get("followers"),
            "Following": user_data.get("following"),
            "Created At": user_data.get("created_at"),
            "Updated At": user_data.get("updated_at"),
            "Profile URL": user_data.get("html_url"),
            "Avatar URL": user_data.get("avatar_url"),
            "Hireable": user_data.get("hireable"),
            "Number of Stars": 0,  # Initialize to 0
            "Number of Forks": 0,  # Initialize to 0
            "Number of Commits": 0,  # Placeholder for commit count, initialize to 0
            "Followers Names": [],  # Initialize to empty list
            "Following Names": [],  # Initialize to empty list
            "Repo Names": [],  # Initialize to empty list
            "Bio Links": [],  # Initialize to empty list
            "Profile Readme": ""  # Initialize to empty string
        }
        
        # Fetch additional stats such as stars, forks, and commits
        repos_url = f"https://api.github.com/users/{username}/repos"
        repos_response = requests.get(repos_url)
        
        if repos_response.status_code == 200:
            repos_data = repos_response.json()
            user_stats["Number of Stars"] = sum(repo.get("stargazers_count", 0) for repo in repos_data)
            user_stats["Number of Forks"] = sum(repo.get("forks_count", 0) for repo in repos_data)
            user_stats["Number of Commits"] = sum(repo.get("open_issues_count", 0) for repo in repos_data)
            user_stats["Repo Names"] = [repo.get("full_name") for repo in repos_data]
        
        # Fetch followers if requested
        if fetch_followers:
            followers_url = f"https://api.github.com/users/{username}/followers"
            followers_response = requests.get(followers_url)
            if followers_response.status_code == 200:
                followers_data = followers_response.json()
                user_stats["Followers Names"] = [follower.get("login") for follower in followers_data]
        
        # Fetch following
        following_url = f"https://api.github.com/users/{username}/following"
        following_response = requests.get(following_url)
        if following_response.status_code == 200:
            following_data = following_response.json()
            user_stats["Following Names"] = [followed.get("login") for followed in following_data]
        
        # Extract links from bio, blog, and repository URLs
        bio_links = extract_links_from_text(user_stats["Bio"] or "")
        blog_links = extract_links_from_text(user_stats["Blog"] or "")
        repo_links = [repo.get("html_url") for repo in repos_data]
        
        all_links = bio_links + blog_links + repo_links
        user_stats["Bio Links"] = all_links
        
        # Fetch profile readme content if available
        readme_url = f"https://raw.githubusercontent.com/{username}/{username}/master/README.md"
        readme_response = requests.get(readme_url)
        if readme_response.status_code == 200:
            user_stats["Profile Readme"] = readme_response.text
        
        return user_stats
    
    else:
        print(f"Failed to fetch user data for {username}. Status code: {user_response.status_code}")
        try:
            error_message = user_response.json().get("message")
            print(f"Error message: {error_message}")
        except:
            print("Failed to parse error message.")
        return None

def print_user_stats(user_stats):
    if user_stats:
        for key, value in user_stats.items():
            if isinstance(value, list):
                print(f"{key}: {', '.join(value)}")
            elif isinstance(value, dict):
                print(f"{key}:")
                for k, v in value.items():
                    print(f"  - {k}: {v}")
            elif key == "Profile Readme":
                print(f"{key}:")
                print(value)  # Print the readme content as is
            else:
                print(f"{key}: {value}")
    else:
        print("User not found or error in fetching data.")

# Main function to interactively fetch GitHub user data
def main():
    while True:
        username = input("Enter a GitHub username (type 'exit' to quit): ")
        if username.lower() == 'exit':
            break
        
        fetch_followers = input("Do you want to fetch followers? (yes/no): ").lower() == 'yes'
        
        user_stats = get_github_user_stats(username, fetch_followers=fetch_followers)
        print_user_stats(user_stats)
        print("\n")

if __name__ == "__main__":
    main()

