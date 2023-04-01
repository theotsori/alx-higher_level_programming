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
        res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        res_dict = res.json()
        if res_dict:
            print("[{}] {}".format(res_dict.get("id"), res_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
