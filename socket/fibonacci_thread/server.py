#!/usr/bin/env python

import socket
import fib
import threading
from concurrent.futures import ProcessPoolExecutor as Pool


### --- Simple Fibonacci server

def fib_server_single(address):

    print("Fibonacci server started.")

    # - Create socket
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # - Settings socket options
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    # - Bind socket to address
    sock.bind(address)

    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        fib_handler_single(client)


def fib_server_pool(address):

    print("Fibonacci server started.")

    # - Create pool
    pool = Pool(4)

    # - Create socket
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # - Settings socket options
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    # - Bind socket to address
    sock.bind(address)

    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        #fib_handler_pool(pool, client)
        threading.Thread( target=fib_handler_pool, args=(pool,client,), daemon=True ).start()

### --- Fibonacci server implemented with threading

def fib_server_threading(address):

    print("Fibonacci server started.")

    # - Create socket
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    # - Settings socket options
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

    # - Bind socket to address
    sock.bind(address)

    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        threading.Thread( target=fib_handler_single, args=(client,), daemon=True ).start()


###################################################

def fib_handler_single(client):
    while True:
        # - Request
        req = client.recv(100)
        if not req:
            break

        # print(req)
        # print(req.decode("utf-8") )
        
        #req = req.decode("utf-8")

        try:
            value = int(req)
            n = int(req)

            result = fib.fib(n)

            resp = str(result).encode('ascii') + b'\n\n'
            client.send(resp)

        except ValueError:
            print("Not a number request.")
            resp = 'Please type in a integer number'.encode('ascii') + b'\n'
            client.send(resp)

    print("Closed")


def fib_handler_pool(pool, client):

    while True:
        # - Request
        req = client.recv(100)
        if not req:
            break

        try:
            value = int(req)
            n = int(req)

            future = pool.submit(fib.fib, n)
            result = future.result()

            resp = str(result).encode('ascii') + b'\n\n'
            client.send(resp)

        except ValueError:
            print("Not a number request.")
            resp = 'Please type in a integer number'.encode('ascii') + b'\n'
            client.send(resp)

    print("Closed")
