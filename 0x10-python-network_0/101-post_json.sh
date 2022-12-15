#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
