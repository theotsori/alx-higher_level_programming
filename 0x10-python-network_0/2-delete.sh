#!/bin/bash
# Deletes a response
[[ $# -eq 0 ]] && { echo "Please provide a URL"; exit 1; }; curl -X DELETE -s -w '\nHTTP status code: %{http_code}\n' "$1"
