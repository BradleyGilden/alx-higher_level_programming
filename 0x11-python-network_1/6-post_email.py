#!/usr/bin/python3

"""
a Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response. You must use requests

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, {"email": email})
    print(response.text)
