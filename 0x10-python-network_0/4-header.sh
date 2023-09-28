#!/bin/bash
# specifies a header variable in request
curl -sH "X-School-User-Id: 98" -X GET "$1"
