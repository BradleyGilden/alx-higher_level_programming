#!/usr/bin/python3

"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
    You must use Basic Authentication with a personal access token as password
    to access to your information (only read:user permission is needed).
    The first argument will be your username.
    The second argument will be your password (in your case, a personal access
    token as password).
    You must use the package requests and sys

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import sys
import requests


if __name__ == '__main__':
    uname = sys.argv[1]
    token = sys.argv[2]
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(f'https://api.github.com/users/{uname}',
                            headers=headers)
    print(response.json().get('id'))
