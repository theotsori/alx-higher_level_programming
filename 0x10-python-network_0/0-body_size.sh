#!/bin/bash
# Send request to the url and save the response

response=$(curl -sI $1)

# Extract the Content-Length header from the response and remove whitespace
content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

# Output the size of the response body in bytes
echo "$content_length"
