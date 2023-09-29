#!/usr/bin/python3

"""
a Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import requests


if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:", f"type: {type(response.text)}",
          f"content: {response.text}", sep='\n')
