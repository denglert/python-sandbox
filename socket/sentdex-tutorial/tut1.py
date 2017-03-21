import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

target_domain = 'www.bbc.co.uk'
target_port   = 80

target_ip = socket.gethostbyname(target_domain) 
print(target_ip)

request = "GET / HTTP/1.1\nHost: "+target_domain+"\n\n"

s.connect( (target_domain, target_port) )
s.send( request.encode() )

result = s.recv(4096)
#print(result)

while (len(result) > 0):
    #result = s.recv(1024)
    result = s.recv(128)
    print(result)
