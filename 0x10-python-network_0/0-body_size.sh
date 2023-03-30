#!/bin/bash
# URL body size
curl -s -w "%{size_download}\n" -o /dev/null "$1"
