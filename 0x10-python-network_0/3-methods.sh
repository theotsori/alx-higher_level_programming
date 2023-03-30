#!/bin/bash
# Use curl to send an OPTIONS request and display the allowed methods
curl -s -I -X OPTIONS "$1" | awk '/Allow/ {print $2}'
