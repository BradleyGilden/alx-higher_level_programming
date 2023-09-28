#!/bin/bash
# makes a specific request to 0.0.0.0:5000/catch_me to find a secret message
curl -H "Origin: School" -d "user_id=98" -X PUT  0.0.0.0:5000/catch_me_2 -sL
