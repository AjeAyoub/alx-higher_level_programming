#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL
curl -s -o response.txt -w "%{http_code}" "$1"