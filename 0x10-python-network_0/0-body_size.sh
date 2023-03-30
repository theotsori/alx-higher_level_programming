#!/bin/bash

url=$1
response=$(curl -sI "$url" | grep -i content-length | awk '{print $2}')
echo "$response"
