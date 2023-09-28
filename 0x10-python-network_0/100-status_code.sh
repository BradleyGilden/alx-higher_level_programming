#!/bin/bash
# displays only the status code of a response without pipes or redirects
curl -s -o /dev/null -w "%{http_code}" "$1"
