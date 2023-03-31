#!/bin/bash
# Sends a GET request to a URL and displays the body of the response if the status code is 200
curl -s "$1" -o /dev/null -w "%{http_code}\n" | grep -q 200 && curl -s "$1"
