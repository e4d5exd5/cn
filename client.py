import time, socket, sys

s = socket.socket()


port = 1234

s.connect(("127.0.0.1", port))



while True:
    message = input(str("Me : "))
    s.send(message.encode())
    message = s.recv(1024)
    message = message.decode()
    print(message)