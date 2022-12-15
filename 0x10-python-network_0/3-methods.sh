#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
