#!/usr/bin/env python

"""
Requests/sec counter of fast requests
"""

import socket
import time
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ('localhost', 25000) )

n = 0

def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'reqs/sec')
        n = 0

threading.Thread(target=monitor).start()

while True:
    start = time.time()
    sock.send(b'1')
    reps = sock.recv(100)
    n += 1
