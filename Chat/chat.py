import socket
import threading
import sys
import urllib.request

class Servidor:
    host = '127.0.0.1'
    porta = 5354
    conexoes = []
    nos = []


    def __init__(self):
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.bind((self.host, self.porta))
        skt.listen(1)

        while(True):
            conexao, endereco = skt.accept()
            threadServidor = threading.Thread(target=self.gerenciar, args=(conexao, endereco))
            threadServidor.daemon = True
            threadServidor.start()
            self.conexoes.append(conexao)
            print(str(endereco[0]) + ':' + str(endereco[1]), "conectado")
            self.atualizarNos()

    def gerenciar(self, conexao, endereco):
        while(True):
            dados = conexao.recv(1024)
            for con in self.conexoes:
                con.send(dados)
            if not dados:
                print(str(endereco[0]) + ':' + str(endereco[1]), "desconectado")
                self.conexoes.remove(conexao)
                self.nos.remove(endereco[0])
                conexao.close()
                self.atualizarNos()
                break

    def atualizarNos(self):
        no_str = ""
        for no in self.nos:
            no_str = no_str + no + ","

        for conexao in self.conexoes:
            conexao.send(b'\x11' + bytes(no_str, 'utf-8'))

class Cliente:
    ip_externo = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    host = ip_externo
    porta = 5354

    def __init__(self, enderecoIP):
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.connect((enderecoIP, self.porta))
        threadCliente = threading.Thread(target=self.enviarMensagem, args=(skt, ))
        threadCliente.daemon = True
        threadCliente.start()

        while(True):
            try:
                dados = skt.recv(1024)
            except KeyboardInterrupt:
                break
            if not dados:
                break
            if (dados[0:1] == b'\x11'):
                print('lista de nós atualizda')
            print(str(dados), 'utf-8')

    def enviarMensagem(self, skt):
        while(True):
            skt.send(bytes(input(""), 'utf-8'))

if(len(sys.argv)>1):
    client = Cliente(sys.argv[1])
else:
    servidor = Servidor()
