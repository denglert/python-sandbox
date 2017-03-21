
### A) performance_test2 on default
~ 15000 reqs/sec

### B) performance_test2 + nc localhost 25000, fib(40)
~ 300 reqs/sec

### C) performance_test2 + python3 -i fib.py fib(40) 
~ 14000 reqs/sec

**Take-away messages:**
- The GIL gives priority to CPU intensive calculations. B)
- The operating system gives priority to short running tasks. C)
