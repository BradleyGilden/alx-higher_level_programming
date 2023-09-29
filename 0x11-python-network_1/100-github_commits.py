#!/usr/bin/python3

"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    headers = {
        "X-GitHub-Api-Version": "2022-11-28",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(
        f'https://api.github.com/repos/{owner}/{repo}/commits', headers=headers
        )
    try:
        for user in response.json():
            user_name = user.get('commit').get('author').get('name')
            print(f"{user.get('sha')}: {user_name}")
    except Exception:
        pass
