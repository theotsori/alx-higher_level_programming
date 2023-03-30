#!/bin/bash

# Send a GET request to the URL using curl, and store the response in a variable
response=$(curl -sSL -w "%{http_code}" $1)

# Extract the status code from the response
status_code=$(echo "$response" | tail -c 4)

# Check if the status code is 200, and display the body of the response if it is
if [ "$status_code" == "200" ]; then
  curl -sSL $1
else
  echo "Error: Response status code was not 200"
  exit 1
fi
