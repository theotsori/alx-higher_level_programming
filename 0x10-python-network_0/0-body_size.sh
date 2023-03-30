#!/bin/bash
# URL body size
[[ $# -eq 0 ]] && response=$(curl -s -w "%{size_download}" -o /dev/null "$1"); echo "$response"
