#!/usr/bin/python3

"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    data = urllib.parse.urlencode({"email": value}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
