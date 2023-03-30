#!/bin/bash
# Send a JSON POST request with the file contents and display the response body
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
