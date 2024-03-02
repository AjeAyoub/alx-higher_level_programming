#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL
curl -s -o response.txt -w "%{http_code}" "$1" | {
    read -r status_code
    if [ "$status_code" == "200" ]; then
        cat response.txt
    fi
    rm -f response.txt
}
