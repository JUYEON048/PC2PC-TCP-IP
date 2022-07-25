# server,.py를 먼저 켜줘야한다.

import os
from socket import*

cnt = 0

ssock = socket(AF_INET, SOCK_STREAM)
ssock.connect(("10.10.0.31", 9008))

ssock.send("hi".encode())

'''
sock.bind(("10.10.0.12", 8000))
ssock.listen(0)

conn, addr = ssock.accept()
print("connected by", addr)

cnt = 0


while cnt < 10:
	ssock.send('hi'.encode())
	cnt = cnt + 1


print("dd")

conn, addr = ssock.accept()
print("connected by", addr)

ssock.close()
'''
ssock.close()