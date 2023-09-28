#!/bin/bash
# display the allowed methods from a response
curl -sI "$1" | grep -oP "(?<=Allow: )[A-Z, ]+"
