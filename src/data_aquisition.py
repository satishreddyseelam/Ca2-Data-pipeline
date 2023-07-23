import requests

def fetch_repository_data(token):
    headers = {
        'Authorization': f'Token {token}',
        'Accept': 'application/vnd.github.v3+json'  # Specify the API version in the request header
    }
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'stars:>0',
        'per_page': 100
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        raise Exception('Failed to fetch repository data')

# Provide your GitHub API token here
github_token = 'your_github_api_token'

try:
    repository_data = fetch_repository_data(github_token)
    # Now you can work with the fetched repository data
    print(repository_data)
except Exception as e:
    print(e)

