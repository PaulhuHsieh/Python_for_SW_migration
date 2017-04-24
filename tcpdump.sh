#!/bin/bash
tcpdump -i eth5 "port 38583" > ./data/gb.txt 2> ./38583.txt &
declare -i pid1=$!

sleep 2

kill $pid1
