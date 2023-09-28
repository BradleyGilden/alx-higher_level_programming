#!/bin/bash
# JSON POST request to a URL passed as the first argument
curl -d "@${2}" -H "Content-Type: application/json" -X POST "$1"
