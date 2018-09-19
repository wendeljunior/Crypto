import socket
import threading
import sys
import rc4

class Servidor:
    #nome do host onde a aplicacao esta a rodar
    host = '127.0.0.1'
    #porta padrao
    porta = 5354
    #Tipo de endereço com os quais o socket ira se conectar: IP v4
    dominio = socket.AF_INET
    #Tipo de comunicacao entre os nos: TCP
    tipo = socket.SOCK_STREAM
    conexoes = []
    nos = []
    chave = "segredo"

    def __init__(self):
        #socket servidor TCP/IP
        skt = socket.socket(self.dominio, self.tipo)
        skt.bind((self.host, self.porta))
        #Ouvindo conexoes para o socket
        skt.listen(5)

        while(True):
            socketCliente, endereco = skt.accept()
            ipCliente = endereco[0]
            portaCliente = endereco[1]
            threadServidor = threading.Thread(target=self.gerenciar, args=(socketCliente, endereco))
            threadServidor.daemon = True
            threadServidor.start()
            self.conexoes.append(socketCliente)
            print(str(ipCliente) + ':' + str(portaCliente), "conectado")
            self.atualizarNos()

    def gerenciar(self, socketCliente, endereco):
        while(True):
            try:
                #recebe 1024 bytes por vez do cliente
                dados = socketCliente.recv(1024)

                if not dados:
                    print(str(endereco[0]) + ':' + str(endereco[1]), "desconectado")
                    self.conexoes.remove(socketCliente)
                    self.nos.remove(endereco[0])
                    socketCliente.close()
                    self.atualizarNos()
                    break

            except OSError:
                print(str(endereco[0]) + ':' + str(endereco[1]), "desconectado")
                socketCliente.close()
                break

            # enviando mensagem para os clientes, exceto o próprio remetente
            for con in self.conexoes:
                if (con != socketCliente):
                    con.send(dados)

    def atualizarNos(self):
        no_str = ""
        for no in self.nos:
            no_str = no_str + no + ","

        for conexao in self.conexoes:
            conexao.send(b'\x11' + bytes(no_str, 'utf-8'))

class Cliente:
    porta = 5354
    chave = "segredo"

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
                print('alguém entrou na conversa')

            print("destinatario: " + dados.decode('utf-8'))

    def enviarMensagem(self, skt):
        while(True):
            try:
                texto = input("")
                #texto_encriptado = rc4.encriptar(self.chave, texto_encriptado)
                skt.send(bytes(texto, 'utf-8'))
            except EOFError:
                print('Você saiu da conversa')
                break

if(len(sys.argv)>1):
    client = Cliente(sys.argv[1])
else:
    servidor = Servidor()
