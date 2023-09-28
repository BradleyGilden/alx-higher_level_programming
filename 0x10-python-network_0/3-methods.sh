#!/bin/bash
# display the allowed methods from a response
curl "$1" | grep -oP "(?<=Allow: )[A-Z, ]+"
