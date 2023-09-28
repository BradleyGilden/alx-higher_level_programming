#!/bin/bash
# get content length of get request
curl -sI "$1" | grep -oP '(?<=Content-Length:\s)\d+'
