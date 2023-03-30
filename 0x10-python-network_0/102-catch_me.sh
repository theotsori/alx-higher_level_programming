#!/bin/bash
# Send a POST request to the specified URL with data for server to respond "You got me!"
curl -s -X POST -d "user_id=98" -H "Referer: http://0.0.0.0:5000/catch_me" http://0.0.0.0:5000/catch_me
