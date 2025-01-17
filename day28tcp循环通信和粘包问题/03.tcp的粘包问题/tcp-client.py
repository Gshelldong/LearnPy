import socket

client = socket.socket()
client.connect(('127.0.0.1',8080))

client.send(b'first')
client.send(b'secend')
client.send(b'thred')