import socket
import threading
import sys

class Servidor:
    localhost = socket.gethostname()
    porta = 5354
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexoes = []

    def __init__(self):
        self.skt.bind((self.localhost, self.porta))
        self.skt.listen(1)

    def gerenciar(self, conexao, endereco):
        while(True):
            dados = conexao.recv(1024)
            for con in self.conexoes:
                con.send(dados)
            if not dados:
                self.conexoes.remove(conexao)
                conexao.close()
                break

    def executar(self):
        while(True):
            conexao, endereco = self.skt.accept()
            threadServidor = threading.Thread(target=self.gerenciar, args=(conexao,endereco))
            threadServidor.daemon = True
            threadServidor.start()
            self.conexoes.append(conexao)
            print(self.conexoes)

class Cliente:
    localhost = socket.gethostname()
    porta = 5354
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, enderecoIP):
        self.skt.connect((enderecoIP, self.porta))
        threadCliente = threading.Thread(target=self.enviarMensagem)
        threadCliente.daemon = True
        threadCliente.start()

        while(True):
            dados = self.skt.recv(1024)
            if not dados:
                break
            print(dados)

    def enviarMensagem(self):
        while(True):
            self.skt.send(bytes(input(""), 'utf-8'))

if(len(sys.argv)>1):
    client = Cliente(sys.argv[1])
else:
    servidor = Servidor()
    servidor.executar()

