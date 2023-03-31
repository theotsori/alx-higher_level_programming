#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        response_dict = response.json()
        if response_dict:
            print("[{}] {}".format(response_dict.get("id"), response_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
