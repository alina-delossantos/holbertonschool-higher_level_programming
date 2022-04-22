#!/bin/bash
# Prints allowed methods for rq
curl -is $1 | grep Allow: | cut -d' ' -f2-
