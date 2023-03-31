#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter and diplays
the response body decoded in utf-8
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode("utf-8")

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
