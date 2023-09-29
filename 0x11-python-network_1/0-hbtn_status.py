#!/usr/bin/python3

"""
a Python script that fetches https://alx-intranet.hbtn.io/status

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        result = response.read()
        print("Body response:", f"type: {type(result)}", f"content: {result}",
              f"utf8 content: {result.decode('UTF-8')}", sep='\n')
