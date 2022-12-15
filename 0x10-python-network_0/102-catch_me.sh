#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
