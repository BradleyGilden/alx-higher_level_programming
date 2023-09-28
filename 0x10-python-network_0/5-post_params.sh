#!/bin/bash
# creates a post request with the parameters email and subject
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
