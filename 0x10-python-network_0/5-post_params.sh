#!/bin/bash
# Post params in server
url=$1

curl -s -X POST "$url" -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -L
