#!/bin/sh
while test true
do
sleep 5
/usr/local/bin/bridge_server -p 80 -u http://nginx3
done
