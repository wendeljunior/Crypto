import socket

servidor = socket.gethostname()
porta_servidor = 5354

mensagem = [b'Eae! Qual eh a boa?']

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect((servidor, porta_servidor))

for linha in mensagem:
    skt.send(linha)
    dados = skt.recv(1024)
    print('Cliente recebeu:', dados)

skt.close()
