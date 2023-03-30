#!/bin/bash
# Send the GET request and display the body of the response
curl -H "X-School-User-Id: 98" "$1" | cat
