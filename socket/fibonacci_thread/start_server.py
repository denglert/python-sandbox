#!/usr/bin/env python

import server

#server.fib_server_single(  ('',25000) )
server.fib_server_threading( ('',25001) )

#server.fib_server( ('',25000) )
