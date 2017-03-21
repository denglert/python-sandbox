#!/usr/bin/env python

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ('localhost', 25000) )

while True:
    start = time.time()
    sock.send(b'30')
    reps = sock.recv(100)
    end = time.time()

    dt = end - start

    print(dt)
