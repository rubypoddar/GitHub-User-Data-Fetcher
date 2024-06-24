# GitHub User Data Fetcher

[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/rubypoddar/GitHub-User-Data-Fetcher)](https://github.com/rubypoddar/GitHub-User-Data-Fetcher/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/rubypoddar/GitHub-User-Data-Fetcher)](https://github.com/rubypoddar/GitHub-User-Data-Fetcher/issues)
[![GitHub stars](https://img.shields.io/github/stars/rubypoddar/GitHub-User-Data-Fetcher)](https://github.com/rubypoddar/GitHub-User-Data-Fetcher/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/rubypoddar/GitHub-User-Data-Fetcher)](https://github.com/rubypoddar/GitHub-User-Data-Fetcher/network)

GitHub User Data Fetcher is a Python script that retrieves comprehensive user information from GitHub using its API. It fetches basic user details, repository statistics, follower/following lists, and extracts links from bio, blog, and repository URLs. Additionally, it attempts to fetch and display the user's profile README if available.

## Features

- **Basic User Details**: Fetches username, name, company, location, email, bio, and more.
- **Repository Statistics**: Retrieves stats like number of public repositories, gists, stars, forks, etc.
- **Followers and Following**: Optionally fetches lists of followers and following users.
- **Link Extraction**: Extracts links from user bio, blog, and repository URLs.
- **Profile README**: Displays the user's profile README content if accessible.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rubypoddar/GitHub-User-Data-Fetcher.git
   ```
2. Navigate into the project directory:
   ```bash
   cd GitHub-User-Data-Fetcher
   ```

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python github_user_data_fetcher.py
   ```
2. Enter a GitHub username when prompted.
3. Choose whether to fetch followers (yes/no).

## Dependencies

- **requests**: Used for making HTTP requests to the GitHub API.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Author

- GitHub: [rubypoddar](https://github.com/rubypoddar)
- Email: rubypoddar101@gmail.com
```
graph TD;
    A[Start] --> B{Enter username (exit to quit)}
    B --> C{Username == 'exit' (yes/no)}
    C(no) --> D{Fetch followers? (yes/no)}
    D(yes) --> E{fetch_followers = True}
    D(no) --> F{fetch_followers = False}
    E, F --> G{Get user data (get_github_user_stats)}
    G --> H{Status code == 200 (yes/no)}
    H(no) --> I{Print error details}
    I1[Status code] --> I2{Print status code}
    I2 --> I3{Try to parse error message}
    I3(success) --> I4{Print error message}
    I3(fail) --> I5{Print 'Failed to parse error message'}
    I --> J[End]
    H(yes) --> K{Extract basic user details (Username, Name, etc.)}
    K --> L{Get additional repository stats (repos)}
    L --> M{Status code == 200 (yes/no)}
    M(no) --> N{Handle error (same as step I)}
    N --> O[End]
    M(yes) --> P{Extract stats from each repository (stars, forks)}
    P --> Q{Fetch followers (if requested)}
    Q --> R{Status code == 200 (yes/no)}
    R(no) --> N
    R(yes) --> S{Extract follower usernames}
    S --> T{Fetch following users}
    T --> U{Status code == 200 (yes/no)}
    U(no) --> N
    U(yes) --> V{Extract following usernames}
    V --> W{Extract links from bio, blog, and repository URLs}
    W1[Bio text] --> W2{Extract links using regex}
    W3[Blog URL (if provided)] --> W2
    W4[Loop through each repository URL] --> W5{Extract repository URL} --> W2
    W --> X{Get profile readme (if available)}
    X --> Y{Status code == 200 (yes/no)}
    Y(no) --> Z[End]
    Y(yes) --> AA{Get readme content}
    AA --> AB{Add readme content to user stats}
    W, AB --> AC{Print user stats (print_user_stats)}
    AC1{Check if user_stats is empty} --> AC2{Loop through each key-value pair}
    AC3{Check if value is a list} --> AC4{Join list elements with commas} --> AC5{Print key and joined list}
    AC3(no) --> AC6{Check if value is a dictionary}
    AC6(yes) --> AC7{Print key} --> AC8{Loop through each key-value pair in dictionary} --> AC9{Print sub-key and sub-value}
    AC3(no) --> AC10{Check if key is 'Profile Readme'}
    AC10(yes) --> AC11{Print key} --> AC12{Print readme content}
    AC3(no) --> AC13{Print key and value}
    AC1(yes) --> AC14{Print 'User not found or error in fetching data'}
    AC --> J[End]
```
---
This flowchart outlines the process flow and decision-making steps for fetching GitHub user data and handling different scenarios.

### Flowchart Explanation

1. **Start (A)**:
   - The process begins with the user starting the program.

2. **Enter username (B)**:
   - Prompt the user to enter a GitHub username.
   
3. **Username == 'exit' (C)**:
   - Check if the user entered 'exit' to quit the program.
   - **(no)**: If not 'exit', proceed to fetch followers.

4. **Fetch followers? (D)**:
   - Ask whether followers should be fetched.
   - **(yes)**: If yes, set `fetch_followers` to True.
   - **(no)**: If no, set `fetch_followers` to False.

5. **Get user data (E, F)**:
   - Depending on the previous decision (`fetch_followers`), either fetch followers or skip.

6. **Status code == 200 (H)**:
   - Check if the HTTP request to fetch user data was successful.
   - **(yes)**: Proceed to extract user details.
   - **(no)**: If not successful, proceed to handle the error.

7. **Print error details (I)**:
   - If there's an error fetching user data, print details about the error.

8. **Extract basic user details (K)**:
   - If user data fetch was successful, extract basic details like Username, Name, etc.

9. **Get additional repository stats (L)**:
   - Fetch additional stats about the user's repositories.
   - **(yes)**: If successful, proceed to extract stats.
   - **(no)**: If not, handle error similar to step I.

10. **Handle error (N)**:
    - Handle errors during repository stats fetching.

11. **Extract stats from each repository (P)**:
    - If repository stats fetch was successful, proceed to extract stats like stars and forks.

12. **Fetch followers (Q)**:
    - Check if followers need to be fetched.
    - **(yes)**: If required, fetch follower usernames.
    - **(no)**: Skip fetching followers.

13. **Extract follower usernames (S)**:
    - If followers were fetched successfully, extract usernames.

14. **Fetch following users (T)**:
    - Fetch users that the GitHub user is following.

15. **Extract following usernames (V)**:
    - If following users were fetched successfully, extract usernames.

16. **Extract links from bio, blog, and repository URLs (W)**:
    - Extract links from the user's bio, blog, and repository URLs.

17. **Get profile readme (X)**:
    - Check if the user has a profile README available.

18. **Status code == 200 (Y)**:
    - Check if the request to fetch profile README was successful.
    - **(yes)**: Proceed to fetch and add README content to user stats.
    - **(no)**: Skip fetching README content.

19. **Print user stats (AC)**:
    - After collecting all data, print the user statistics.

20. **End (J)**:
    - End of the process flow.

### Summary
This flowchart guides the process of fetching and handling GitHub user data through a series of steps, including user input validation, error handling, data extraction, and final output. It ensures a structured approach to interacting with GitHub's API and presenting relevant user information. Adjustments can be made based on specific project needs or additional functionalities desired.



---
the provided Python script, which interacts with the GitHub API to fetch user data and process it accordingly.

### Code Explanation

#### 1. Imports and Function Definition

```python
import requests
import re
```

- **requests**: This library is used to send HTTP requests to the GitHub API endpoints.
- **re**: This module provides support for regular expressions (regex), which are used to extract links from text.

#### 2. `extract_links_from_text` Function

```python
def extract_links_from_text(text):
    """
    Function to extract links from a text string using regex.
    """
    return re.findall(r'https?://\S+', text)
```

- **Purpose**: This function extracts URLs from a given text string using a regular expression.
- **Parameters**: `text` (string) - The text from which URLs need to be extracted.
- **Returns**: A list of URLs found in the text.

#### 3. `get_github_user_stats` Function

```python
def get_github_user_stats(username, fetch_followers=False):
    # GitHub API endpoint for user details
    user_url = f"https://api.github.com/users/{username}"
    
    # Requesting user details
    user_response = requests.get(user_url)
    
    if user_response.status_code == 200:
        # Process user data if request is successful
        user_data = user_response.json()
        
        # Initialize user_stats dictionary with necessary keys
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
            # Process repository data if request is successful
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
                # Process followers data if request is successful
                followers_data = followers_response.json()
                user_stats["Followers Names"] = [follower.get("login") for follower in followers_data]
        
        # Fetch following
        following_url = f"https://api.github.com/users/{username}/following"
        following_response = requests.get(following_url)
        if following_response.status_code == 200:
            # Process following data if request is successful
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
            # Process readme content if request is successful
            user_stats["Profile Readme"] = readme_response.text
        
        return user_stats
    
    else:
        # Handle failed request to fetch user data
        print(f"Failed to fetch user data for {username}. Status code: {user_response.status_code}")
        try:
            error_message = user_response.json().get("message")
            print(f"Error message: {error_message}")
        except:
            print("Failed to parse error message.")
        return None
```

- **Purpose**: This function retrieves GitHub user data, including basic information, repository details, follower information, and bio links.
- **Parameters**: 
  - `username` (string): The GitHub username for which data is to be fetched.
  - `fetch_followers` (boolean, optional): Determines whether to fetch follower usernames.
- **Returns**: 
  - `user_stats` (dictionary): A dictionary containing various user data fields such as username, name, company, etc.
  - Returns `None` if there was an error fetching the data.

#### 4. `print_user_stats` Function

```python
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
```

- **Purpose**: This function prints the fetched user statistics in a readable format.
- **Parameters**: `user_stats` (dictionary): The dictionary containing user data.
- **Prints**: 
  - For lists, it prints each item separated by commas.
  - For dictionaries, it prints each key-value pair with indentation.
  - For the profile readme, it prints the content directly.
  - If `user_stats` is `None`, it prints an error message indicating that the user was not found or there was an error fetching data.

#### 5. `main` Function

```python
def main():
    while True:
        username = input("Enter a GitHub username (type 'exit' to quit): ")
        if username.lower() == 'exit':
            break
        
        fetch_followers = input("Do you want to fetch followers? (yes/no): ").lower() == 'yes'
        
        user_stats = get_github_user_stats(username, fetch_followers=fetch_followers)
        print_user_stats(user_stats)
        print("\n")
```

- **Purpose**: This function is the entry point of the program for interactive use.
- **Behavior**:
  - Prompts the user to enter a GitHub username.
  - Asks whether to fetch followers.
  - Calls `get_github_user_stats` to fetch and process user data.
  - Calls `print_user_stats` to display the fetched data in a formatted manner.
  - Continues until the user types 'exit'.

#### 6. `__main__` Block

```python
if __name__ == "__main__":
    main()
```

- **Purpose**: This block ensures that the `main` function is executed only when the script is run directly (not imported as a module).

### Summary

The provided script interacts with the GitHub API to fetch user data, handles errors, and prints the fetched data in a readable format. It uses functions to modularize different aspects of the data fetching and processing, making the code more organized and easier to maintain. Adjustments can be made to enhance error handling or add more functionalities based on specific project requirements.


---
The output of the Python script, when run interactively, allows users to input a GitHub username and choose whether to fetch followers. Here's a summary of how the output would look based on the functions described:

### Sample Output Explanation

1. **Prompt for Input:**
   ```
   Enter a GitHub username (type 'exit' to quit): octocat
   Do you want to fetch followers? (yes/no): yes
   ```

2. **Fetching User Data:**
   - The script sends requests to the GitHub API to retrieve details about the user `octocat`, including basic profile information, repository statistics, and optionally followers.

3. **Processing and Displaying Data:**
   - If the requests are successful (`status_code == 200`), the script formats the retrieved data into a dictionary (`user_stats`).
   - It prints various details such as username, name, company, location, number of repositories, followers, etc.
   - Bio links, blog links, and repository URLs are extracted and displayed as well.

4. **Example Output:**
   ```
   Username: octocat
   Name: The Octocat
   Company: GitHub
   Blog: https://www.github.com/blog
   Location: San Francisco
   Email: null
   Bio: Hello World
   Twitter Username: null
   Public Repos: 8
   Public Gists: 8
   Followers: 1677
   Following: 9
   Created At: 2011-01-25T18:44:36Z
   Updated At: 2021-06-29T01:05:21Z
   Profile URL: https://github.com/octocat
   Avatar URL: https://avatars.githubusercontent.com/u/583231?v=4
   Hireable: true
   Number of Stars: 0
   Number of Forks: 0
   Number of Commits: 0
   Followers Names: [follower1, follower2, ...]
   Following Names: [following1, following2, ...]
   Repo Names: [repo1, repo2, ...]
   Bio Links: [https://www.github.com/blog, https://github.com/octocat/repo1, ...]
   Profile Readme:
   # Hello

   This is a sample README.

   ```

5. **Error Handling:**
   - If there's an issue fetching user data (`status_code != 200`), an appropriate error message is displayed, along with any available error details from GitHub's API response.

6. **Exiting the Program:**
   - To exit the program, the user can type `exit` when prompted for a username.

### Summary

The script provides an interactive way to fetch and display GitHub user data using the GitHub API. It leverages functions to handle HTTP requests (`requests` library), process JSON responses, extract relevant information (using `re` for regex-based URL extraction), and format the output for readability. This modular approach ensures that the code is organized, maintainable, and can easily accommodate future enhancements or modifications.
