# Fast Math
# This program socketed to the specified server and evaluated math problems.
# It's not the smartest, since it evaluates arbibtrary code sent over the network, but it
# sufficed for this challenge.

import os
import sys
import socket
import time

host = "12.157.27.229"
port = 8082

# connect our socket
remote_ip = socket.gethostbyname(host)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((remote_ip, port))

#
while True:
    try:
        problem = str(s.recv(1024), "utf-8")
        print(problem)  # we print out the problem mostly so that when the flag is sent we can see it.
        math = problem.split("of ")[1].split("?")[0] # take advantage that every problem has the form "of ... ?"
        ans = eval(math)
        print(ans)
        s.send(bytearray(str(ans) + "\n", "utf-8"))  # not sending \n annoyed the server and it wouldn't respond to us.
    except: 
        print('No data available')
        sys.exit()
