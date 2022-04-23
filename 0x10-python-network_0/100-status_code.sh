#!/bin/bash
# Shows status code HTTP request
curl -s -o /dev/null -w "%{http_code}" $1
