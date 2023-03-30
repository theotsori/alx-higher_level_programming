#!/bin/bash
# Send a GET request to the URL using curl, and store the response in a variable
[[ $# -eq 0 ]] && [[ $(curl -s -w "%{http_code}" "$1") -eq 200 ]] && curl -s "$1" || curl -s -w "%{http_code}" "$1"
