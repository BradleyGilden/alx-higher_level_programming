#!/usr/bin/python3

"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display the
    id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty

Author: Bradley Dillion Gilden
Date: 29-09-2023
"""
import sys
import requests


if __name__ == '__main__':
    data = {"q": ""} if len(sys.argv) < 2 else {"q": sys.argv[1]}
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data)
        rjson = response.json()
        if response.status_code < 400 and rjson != {} and type(rjson) != list:
            print(f"[{rjson.get('id')}] {rjson.get('name')}")
        else:
            print('No result')
    except (requests.exceptions.JSONDecodeError, ValueError):
        print("Not a valid JSON")
