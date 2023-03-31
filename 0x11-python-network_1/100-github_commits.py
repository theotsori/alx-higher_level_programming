#!/usr/bin/python3
"""
Script that takes two arguments and uses GitHub API
to list 10 most recent commits
"""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)

    if response.status_code == 200:
        for commit in response.json()[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f'Request failed with status code {response.status_code}')
