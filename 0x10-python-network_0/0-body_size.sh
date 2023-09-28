#!/usr/bin/env bash
# get content length of get request

length=$(curl -sI "$1" | grep -oP '(?<=Content-Length:\s)\d+')
echo "$length"
