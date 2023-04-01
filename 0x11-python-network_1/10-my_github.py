#!/usr/bin/python3
"""
Script that takes your Github credentials and uses
the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    re = requests.get('https://api.github.com/user', auth=(username, password))
    if re.status_code == 200:
        print(re.json()['id'])
    else:
        print('None')
