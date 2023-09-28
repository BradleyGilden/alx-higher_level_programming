#!/usr/bin/env bash
# get content length of get request
curl -s "$1" | wc -c
