import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket has created with successful')

host = 'localhost'
port = 5432

s.bind((host, port))

mensagem = 'Server: Hello Brazil'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Server sending a message...')
        s.sendto(dados +(mensagem.encode()), end)

