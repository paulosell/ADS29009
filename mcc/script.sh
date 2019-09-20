#!/bin/bash
if [ $1 = "python" ]; then
    python3 server.py
else
   gcc server.c -o server; ./server;
fi