#!/usr/bin/python3

"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.
You must use requests

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
