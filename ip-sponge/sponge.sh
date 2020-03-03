#!/bin/bash

# SCRIPT TO SOAK UP ALL IP ADDRESSES IN SUBNET

# GET CURRENT IP ADDRESS (PRIMARY)
IP="$(ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p')"

echo $IP
