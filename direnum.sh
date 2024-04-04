#!/bin/bash

url="127.0.0.1"
file_out="out.txt" # output file
delay_ms=100
protocol="https" # https or http
word_list="words.txt"

dirb "$protocol://$url" "$word_list" -z delay_ms >> file_out | tail -f file_out
