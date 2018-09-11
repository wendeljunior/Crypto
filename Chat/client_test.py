import threading
import socket

#---------------------------------------------------#
#---------INITIALIZE CONNECTION VARIABLES-----------#
#---------------------------------------------------#
HOST = "YOUR EXTERNAL IP ADDRESS HERE"
PORT = 8011
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#---------------------------------------------------#
#----------------CONNECTION MANAGEMENT--------------#
#---------------------------------------------------#

def ReceiveData():
    try:
        s.connect((HOST, PORT))
        print('conectado')
    except:
        print('não foi possível conectar')
        return
    
    while 1:
        try:
            data = s.recv(1024)
        except:
            print('parceiro de conversa desconectou')
            break
        if data != '':
            print('notificacao')
                
        else:
            print('parceiro desconectou')
            break
    #s.close()

t = threading.Thread(target=ReceiveData)
t.start()


