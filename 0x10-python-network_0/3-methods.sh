#!/bin/bash
# Use curl to send an OPTIONS request and display the allowed methods
curl -sI "$1" | grep -i Allow
