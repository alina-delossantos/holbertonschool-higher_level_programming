#!/bin/bash
# Sends POST rq with srver with data
curl -s -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' $1
